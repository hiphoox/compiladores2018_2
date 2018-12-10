{-
Autor: Galván Bazán Raúl
Materia: Compiladores
Semestre: 2019-1

Descripción: Programa que compila el lenguaje c. Acepta expresiones matemáticas
como suma, resta, multipicación, división, negación, negación lógica, complemento
a uno o un sólo número.
-}

import Data.Char
import System.Environment
import System.Process

{-
   LEXER
En esta parte se definen los tipos de datos utilizados. Primero se creó
un tipo de datos para los operadores unarios y binarios y después se
creó el tipo de datos Token para representar los tokens utilizados.
-}
data Operator = Plus | Minus | Div | Times | Neg | Cmp
   deriving (Show, Eq)

data Token = Op Operator
            | LParen
            | RParen
            | LBrac
            | RBrac
            | Semicolon
            | IntKw
            | ReturnKw
            | Ident String
            | Entero Int
            | TokEnd
    deriving (Show, Eq)
{-
La función operador acepta un caracter que representa un operador
y devuelve el Token asociado,
-}
operator :: Char -> Operator
operator c | c == '+' = Plus
           | c == '-' = Minus
           | c == '*' = Times
           | c == '/' = Div
           | c == '~' = Cmp
           | c == '!' = Neg

{-
La función tokenize es la función principal para realizar el análisis
léxico. Recorre de manera recursiva la lista de tokens que recibe como
argumento y va reemplazando los caractere con el token correspondiente.
-}
tokenize :: String -> [Token]
tokenize [] = []
tokenize (c : cs) 
    | elem c "+-~*/!" = Op (operator c) : tokenize cs
    | c == '('  = LParen : tokenize cs
    | c == ')'  = RParen : tokenize cs
    | c == '{'  = LBrac : tokenize cs
    | c == '}'  = RBrac : tokenize cs
    | c == ';'  = Semicolon : tokenize cs
    | isDigit c = entero c cs
    | isAlpha c = is_Id_Kw c cs
    | isSpace c = tokenize cs
    | otherwise = error $ "Error de sintaxis. Input " ++ [c] ++ "no valido"

{-
La función is_Id_Kw auxilia a la función tokenize. Reconoce las cadenas
identificadas como palabras reservadas o que pueden ser interpretadas
como identificadores y devuelve el token correspondiente.
-}
is_Id_Kw :: Char -> String -> [Token]
is_Id_Kw c cs = let (name, cs') = span isAlphaNum cs in
                  case (c:name) of
                  "return" -> ReturnKw : tokenize cs'
                  "int" -> IntKw : tokenize cs'
                  otherwise -> Ident (c:name) : tokenize cs'

{-
La función entero identifica si una secuencia de caracteres es un
número entero y devuelve el token correspondiente.
-}
entero :: Char -> String -> [Token]
entero c cs = 
   let (digs, cs') = span isDigit cs in
      Entero (read (c : digs)) : tokenize cs'


{-
----AST---

En esta parte se construyen los tipos de datos necesarios para crear
el árbol de sintaxis.
-}

--Tipo de la función (sólo int por el momento)
data Tipo = IntType
         deriving (Show, Eq)

--Identificador de la función
data Identifier = ID String
         deriving (Show, Eq)

--Operadores unarios
data UnaryOp = UPlus 
               | UMinus 
               | UNeg 
               | UCmp
            deriving(Show, Eq)

--Sirve para construir expresiones
data Expression = Trm Term 
                  |SumNode Expression Expression
                  |MinNode Expression Expression
               deriving(Show, Eq)

--Sirve para construir términos
data Term = Fac Factor 
            |MulNode Term Term
            |DivNode Term Term
         deriving(Show, Eq)

--Sirve para construir factores
data Factor= Unary UnaryOp Factor
            |Exp Expression --Expression
            |Const Int
         deriving(Show, Eq)

--El árbol que representa al programa
data Tree=  ProgramNode Tree
            |FunctionNode Tipo Identifier Tree
            |Statement Expression 
         deriving (Show, Eq)

{-
----Parser-----

En esta parte se definen las funciones necesarias para realizar el 
análisis sintáctico. Primero se definen las funciones lookAhead y
restoLista, que devuelven la cabeza y cola de una lista de tokens, pero
tienen opciones para lidiar con listas vacías.
-}
lookAhead :: [Token] -> Token
lookAhead [] = TokEnd
lookAhead (t:ts) = t

restoLista :: [Token] -> [Token]
restoLista [] = error "Error, se espera un token"
restoLista (t:ts) = ts

{-
La función unaryOpNode devuelve un nodo que contiene un factor con
operador unario.
-}
unaryOpNode::Operator -> Factor -> Factor
unaryOpNode op fac =
   case op of
      Plus -> Unary UPlus fac
      Minus -> Unary UMinus fac
      Neg -> Unary UNeg fac
      Cmp -> Unary UCmp fac
      _->  error "Operador no válido"

{-
La función parseFactor devuelve un factor según la sintaxis
<factor> ::= "(" <expression> ")" 
             | <unaryOp> <factor> 
             | <entero>
También devuelve una lista que corresponde al resto de los tokens
que se deben parsear.
-}
parseFactor::[Token]->(Factor, [Token])
parseFactor (c:cs) =
   case c of
      (Entero x) -> (Const x, cs)
      (Op y)-> let (fac, cs') = parseFactor cs in
               ((unaryOpNode y fac), cs')
      LParen -> let (exp, cs') = parseExpression cs in
         let rparen = lookAhead cs' in
            case rparen of
               RParen -> (Exp exp, restoLista cs')
               _ -> error "Se esperaba un )"
      _ -> error "No se reconoce la expresión"

{-
La función parseTerm devuelve un término según la sintaxis 
<term> ::= <factor> { ("*" | "/") <factor> }
También devuelve una lista que corresponde al resto de los tokens
que se deben parsear. Llama a la función parseFactor y después se
apoya en la función binMulDivNode.
-}
parseTerm::[Token] -> (Term, [Token])
parseTerm tok =
   let (leftFactor, cs) = parseFactor tok in
         binMulDivNode cs (Fac leftFactor)

{-
La función binMulDivNode recorre la lista de tokens de manera recursiva
para buscar las operaciones de multiplicación y división (posiblemente
consecutivas). Si no se encuentra ninguna de las operaciones mencionadas,
la función devuelve el mismo factor y lista de tokens que recibió.
-}
binMulDivNode:: [Token]-> Term -> (Term, [Token])
binMulDivNode tokens left =
   let op = lookAhead tokens in
      case op of
         (Op y) -> let (right, cs) = parseFactor (restoLista tokens) in
            case op of
               Op Times -> let node = MulNode left (Fac right) in
                  binMulDivNode cs node
               Op Div -> let node = DivNode left (Fac right) in
                  binMulDivNode cs node
               _-> (left, tokens)
         _-> (left, tokens)

{-
Igual que la función binMulDivNode pero para operacions de suma y resta.
-}
binSumMinNode:: [Token]-> Expression -> (Expression, [Token])
binSumMinNode tokens left =
   let op = lookAhead tokens in
      case op of
         (Op y) -> let (right, cs) = parseTerm (restoLista tokens) in
            case op of
               Op Plus -> let node = SumNode left (Trm right) in
                  binSumMinNode cs node
               Op Minus -> let node = MinNode left (Trm right) in
                  binSumMinNode cs node
               _-> error "Operador no válido"
         _-> (left, tokens)

{-
La función parseExpression se encarga de construir un nodo correspondiente
a una expresión. Primero llama a la función parseTerm y después se apoya
en la función binSumMinNode para reconocer las operaciones de suma y resta.
-}
parseExpression::[Token] -> (Expression, [Token])
parseExpression tok =
   let (leftTerm, cs) = parseTerm tok in
      binSumMinNode cs (Trm leftTerm)

{-
La función parseStatement se encarga de construir un nodo correspondiente
a los enunciados de la función
-}
parseStatement :: [Token] -> (Tree, [Token])
parseStatement (c:cs)=
   case c of
      ReturnKw -> let (statement, cs') = (parseExpression cs) in
                     case lookAhead cs' of
                        Semicolon-> (Statement statement, restoLista cs')
                        _-> error "Se esperaba ;"
      _ -> error "Se esperaba devolver una expresion"

{-
La función parse_funBody se encarga de construir el cuerpo de una función.
-}
parse_funBody :: [Token] -> Tree
parse_funBody tokens =
   let (statements, rest)= parseStatement tokens in
      let (c, cs) = (lookAhead rest, restoLista rest) in
         case c of
            RBrac-> let (c', cs') = (lookAhead cs, restoLista cs) in
                        case c' of
                           TokEnd-> statements
                           _->error "Error en el parseo" 
            _ -> error "Se esperaba }"

{-La función makeBody se encarga de construir el nodo correspondiente al
cuerpo de una función. Se apoya en la función parse_funBody para checar
que la sintaxis sea correcta.
-}
makeBody :: [Token] -> Tree
makeBody tokens =
           let(c, cs) = (lookAhead tokens, restoLista tokens) in
            case c of
               LBrac -> parse_funBody cs
               _ -> error "Se esperaba {"

{-
La función parse_funParam sirve para hacer el parsea de los argumentos
de una función. En este momento no es de gran utilidad, sólo checa que 
no haya argumentos.
-}
parse_funParam :: [Token] -> ([Token], [Token])
parse_funParam (c:cs)=
   case c of
      RParen -> ([], cs)
      _ -> error "Error durante el parseo, se esperaba )"

{-
La función parseFunction se encarga de recabar todos los datos 
correspondientes a una función (tipo, identificador, argumentos, cuerpo)
y genera el nodo correspondiente.
-}
parseFunction::[Token] -> Tree
parseFunction tok =
   let (funType, cs) = (lookAhead tok, restoLista tok) in
      case funType of
         IntKw -> let (fun_name, cs') = (lookAhead cs, restoLista cs) in
                     case fun_name of
                        (Ident x) -> let (isParen, cs'') =  (lookAhead cs', restoLista cs') in
                                       case isParen of
                                          LParen -> let (params, cs''') = parse_funParam cs'' in
                                             case params of
                                                []->FunctionNode IntType (ID x) (makeBody cs''')
                                                _-> error "Error de parseo, argumentos no válidos"
                        _-> error "Error de parseo, Identificador no válido"
         _-> error "Error de parseo, tipo de la función no válido"


--El nodo raíz
data Prog = Program Tree
      deriving (Show, Eq)

{-
La función parser es la función principal para realizar el análisis
sintáctico. Recibe una lista de tokens como argumento y regresa un 
árbol que representa el programa de entrada.
-}
parser :: [Token] -> Prog
parser tokens= Program (parseFunction tokens)

{-
-----Generador-------

El generador se encarga de traducir el árbol construido por el parser
a lenguaje ensamblador.
NOTA: en este archivo se utilizó la sintaxis correspondiente a la
arquitextura x86 de Intel.
-}

{-
La función generator es la función principal para general el código ensamblador.
-}
generator :: Prog -> String
generator program=
   let main = ".globl main\n" in
      case program of
         (Program x) -> case x of
            (FunctionNode IntType (ID y) (Statement z))-> let funName = id y ++":\n" in
               let statement = evalExpression  z ++ "ret\n" in
                  main ++ funName ++ statement

{-
La función evalExpression se encarga de evaluar los nodos reconocidos como
expresiones. Si la expresión recibida se reconoce como un término entonces
se llama a la función evalTerm. Si la expresión es un nodo de suma o
resta entonces se evalúan las ramas de manera recursiva.
-}
evalExpression:: Expression -> String
evalExpression exp =
   case exp of
      (Trm term) -> 
         case term of
            (Fac factor) -> evalFactor (Fac factor)
            (MulNode le ri) -> evalTerm (Trm term)
            (DivNode le ri) -> evalTerm (Trm term)
      (SumNode le ri)-> let (s1, s2) = (evalExpression le, evalExpression ri) in
         s1 ++ "push %ax\n" ++ s2 ++ "pop %cx\n" ++ "addl %ecx, %eax\n"
      (MinNode le ri)-> let (s1, s2) = (evalExpression le, evalExpression ri) in
         s2 ++ "push %ax\n" ++ s1 ++ "pop %cx\n" ++ "subl %ecx, %eax\n"

{-
La función evalTerm se encarga de evaluar los nodos reconocidos como
términos. Si se reconoce que la expresión de entrada es un factor se
llama a la función evalFactor. Si la expresión es un nodo de multiplicación
o división entonces se evalúan las ramas de manera recursiva.
-}
evalTerm::Expression -> String
evalTerm (Trm term) =
   case term of
      (Fac factor) -> evalFactor (Fac factor)
      (MulNode le ri) -> let (s1, s2) = (evalTerm (Trm le), evalTerm (Trm ri)) in
         s1 ++ "push %ax\n" ++ s2 ++ "pop %cx\n" ++ "imul %ecx, %eax\n"
      (DivNode le ri) -> let (s1, s2) = (evalTerm (Trm le), evalTerm (Trm ri)) in
         s2++"movl %eax, %ecx\n" ++ s1 ++ "xor %edx, %edx\n" ++ "idivl %ecx\n"

{-
La función evalFactor se encarga de evaluar los nodos reconocidos como factores.
Si el factor factor consiste de varios operadores unarios que se anteponen a un
factor entonces se evalúa el factor de manera recursiva.
-}
evalFactor::Term->String
evalFactor (Fac factor)=
   case factor of 
      (Const x) -> "movl $" ++ show x ++ ", %eax\n"
      (Unary op  cons) -> let factor' = evalFactor (Fac cons) in
         case op of
            UPlus -> factor'
            UMinus -> factor' ++ "neg %eax\n"
            UCmp -> factor' ++ "not %eax\n"
            UNeg -> factor' ++ "cmpl $0, %eax\nmovl $0, %eax\nsete %al \n"
      (Exp expression) -> evalExpression expression

{-
Función Principal.
Forma de uso: <nombreFunción> <nombreArchivo.c>
La variable args contiene los argumentos de la función (nombre del archivo
c que se desea compilar).
Se lee el archivo y se ejecutan, en el orden mencionados, las funciones:
1- tokenizer
2- parser
3- generator
4- Se llama a gcc para general el archivo ensamblador
NOTA: Se utilizó gcc para la arquitectura intel x86
-}

main = do args <- getArgs
          file <- readFile (args!!0)
          writeFile "outComp.s" (generator (parser (tokenize file)))
          createProcess(proc "gcc" ["outComp.s", "-o", "out"])
