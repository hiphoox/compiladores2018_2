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
	Negation = "-"
	BitwiseComplement = "~"
	LogicalNegation = "!"

@unique
class UnaryOp(Enum):
	Negation = Token.Negation
	BitwiseComplement = Token.BitwiseComplement
	LogicalNegation = Token.LogicalNegation