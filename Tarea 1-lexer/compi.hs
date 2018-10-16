import Data.Char
import System.Environment
import System.Process


data UnaryOp = Plus | Minus | Neg
    deriving (Show, Eq)

data Token = UniOp UnaryOp
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

operator :: Char -> UnaryOp
operator c | c == '+' = Plus
           | c == '-' = Minus
           | c == '~' = Neg 

tokenize :: String -> [Token]
tokenize [] = []
tokenize (c : cs) 
    | elem c "+-~" = UniOp (operator c) : tokenize cs
    | c == '('  = LParen : tokenize cs
    | c == ')'  = RParen : tokenize cs
    | c == '{'  = LBrac : tokenize cs
    | c == '}'  = RBrac : tokenize cs
    | c == ';'  = Semicolon : tokenize cs
    | isDigit c = entero c cs
    | isAlpha c = is_Id_Kw c cs
    | isSpace c = tokenize cs
    | otherwise = error $ "Error de sintaxis. Input " ++ [c] ++ "no valido"

is_Id_Kw :: Char -> String -> [Token]
is_Id_Kw c cs = let (name, cs') = span isAlphaNum cs in
                  case (c:name) of
                  "return" -> ReturnKw : tokenize cs'
                  "int" -> IntKw : tokenize cs'
                  otherwise -> Ident (c:name) : tokenize cs'

entero :: Char -> String -> [Token]
entero c cs = 
   let (digs, cs') = span isDigit cs in
      Entero (read (c : digs)) : tokenize cs'

--AST
data UnOp=Min|Pls|Cmp
      deriving (Show, Eq)
data Exp= Const Int|Unary UnOp Exp
      deriving (Show, Eq)
data Tipo = IntType
      deriving (Show, Eq)
data Statement = ReturnVal Exp
      deriving (Show, Eq)
data Identifier = ID String
      deriving (Show, Eq)
data FunParam = Param Tipo Identifier
      deriving (Show, Eq)
data FunBod = Body Statement
      deriving (Show, Eq)
data FunDec = Funcion (Tipo, Identifier, FunBod)
      deriving (Show, Eq)
data Prog = Program FunDec
      deriving (Show, Eq)

--Parser

lookAhead :: [Token] -> Token
lookAhead [] = TokEnd
lookAhead (t:ts) = t

restoLista :: [Token] -> [Token]
restoLista [] = error "Error, se espera un token"
restoLista (t:ts) = ts

parse_funParam :: [Token] -> ([FunParam], [Token])
parse_funParam (c:cs)=
   case c of
      RParen -> ([], cs)
      _ -> error "Error durante el parseo, se esperaba )"

parse_num :: Token -> Exp
parse_num (Entero x) = Const x

parse_exp :: [Token] -> (Exp, [Token])
parse_exp tokens=
   let (c, cs) = (lookAhead tokens, restoLista tokens) in
   case c of
      (Entero x) -> (parse_num (Entero x), cs)
      UniOp Plus -> let (exp, rest) = parse_exp cs in (Unary Pls exp, rest)
      UniOp Minus -> let (exp, rest) = parse_exp cs in (Unary Min exp, rest)
      UniOp Neg -> let (exp, rest) = parse_exp cs in (Unary Cmp exp, rest)
      _ -> error "Token no válido o inexistente en parse_exp"

parse_statements :: [Token] -> (Statement, [Token])
parse_statements (c:cs)=
   case c of
      ReturnKw -> let (exp, cs') = (parse_exp cs) in
                     case lookAhead cs' of
                        Semicolon-> (ReturnVal exp, restoLista cs')
                        _-> error "Se esperaba ;"
      _ -> error "Se esperaba devolver una expresion"

parse_funBody :: [Token] -> FunBod
parse_funBody tokens =
   let (statements, rest)= parse_statements tokens in
      let (c, cs) = (lookAhead rest, restoLista rest) in
         case c of
            RBrac-> let (c', cs') = (lookAhead cs, restoLista cs) in
                        case c' of
                           TokEnd-> Body statements
                           _->error "Error " 
            _ -> error "Se esperaba }"

makeBody :: [Token] -> FunBod
makeBody tokens =
           let(c, cs) = (lookAhead tokens, restoLista tokens) in
            case c of
               LBrac -> parse_funBody cs
               _ -> error "Se esperaba {"

parse_fun :: [Token] -> FunDec
parse_fun tokens=
   let (funType, cs) = (lookAhead tokens, restoLista tokens) in
      case funType of
         IntKw -> let (fun_name, cs') = (lookAhead cs, restoLista cs) in
                     case fun_name of
                        (Ident x) -> let (isParen, cs'') =  (lookAhead cs', restoLista cs') in
                                       case isParen of
                                          LParen -> let (params, cs''') = parse_funParam cs'' in
                                             case params of
                                                []->Funcion (IntType, ID x, makeBody cs''')
                                                _-> error "Error de parseo, argumentos no válidos"
                        _-> error "Error de parseo, Identificador no válido"
         _-> error "Error de parseo, tipo de la función no válido"



parser :: [Token] -> Prog
parser tokens= Program (parse_fun tokens)

--Generador

generator :: Prog -> String
generator program=
   let main = ".globl main\n" in
      case program of
         (Program x) -> case x of
            Funcion(IntType, (ID y), Body z)-> let (genH, genT) = (main ++ id y ++ ":\nmovl $", ", %eax \nret\n") in
               case z of
                  ReturnVal (Const i) -> genH ++ show i ++ genT
                  ReturnVal (Unary Pls (Const i)) -> genH ++ show i ++ genT
                  ReturnVal (Unary Min (Const i)) -> genH ++"-"++show i ++ genT
                  ReturnVal (Unary Cmp (Const i)) -> genH ++"~"++show i ++ genT
                  _->error "Error en la generacion de codigo de return"

main = do args <- getArgs
          file <- readFile (args!!0)
          writeFile "cfile.s" (generator (parser (tokenize file)))
          createProcess(proc "gcc" ["cfile.s", "-o", "exe"])
