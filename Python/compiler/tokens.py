from enum import Enum, unique

#creando enumeracion de tokens
@unique
class Token(Enum):
	OpenBrace =  "{"
	CloseBrace = "}"
	OpenParen = "("
	CloseParen = ")"
	Semicolon = ";"
	IntKeyword = "int"
	CharKeyword = "char"
	ReturnKeyword = "return"
	BitwiseComplement = "~"
	LogicalNegation = "!"
	Plus = "+"
	Minus = "-"
	Multiplication = "*"
	Division = "/"

@unique
class UnaryOp(Enum):
	BitwiseComplement = Token.BitwiseComplement
	LogicalNegation = Token.LogicalNegation

@unique
class BinaryOp(Enum):
	Addition = Token.Plus
	Subtraction = Token.Minus
	Multiplication = Token.Multiplication
	Division = Token.Division