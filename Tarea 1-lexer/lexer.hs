import Data.Char

data Token =
  LlaveI Char
  |LlaveD Char
  |ParentesisI Char
  |ParentesisD Char
  |PuntoyComa Char
  |EnteroKw String
  |ReturnKw String
  |Entero String
  |ID String
  deriving (Show)


isKw :: [Char] -> Token
isKw s 
  | s == "return" = ReturnKw s
  | s == "int" = EnteroKw s
  | otherwise = ID s

tokenize :: String -> [Token]
tokenize "" = []
tokenize (c:cs)
  | isSpace c = tokenize cs
  | c == '{' = (LlaveI c) : tokenize cs
  | c == '}' = (LlaveD c) : tokenize cs
  | c == '(' = (ParentesisI c) : tokenize cs
  | c == ')' = (ParentesisD c) : tokenize cs
  | c == ';' = (PuntoyComa c) : tokenize cs  
  | isAlpha c = let (i,cs') = span isAlphaNum cs in (isKw (c : i)) : tokenize cs'
  | isDigit c = let (n,cs') = span isDigit cs in (Entero (c : n)) : tokenize cs' --No reconoce bien los numeros, e.g. 123abc lo toma como válido y lo separa en 123 y abc
  | otherwise = error $ "caracter no válido " ++ show c

main = print (tokenize "int main(){return 2;}")
