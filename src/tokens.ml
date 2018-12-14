type token =
	| OpenBrace
	| CloseBrace
	| OpenParen
	| CloseParen
	| Semicolon 
	| IntKeyword
	| MainKeyword
	| ReturnKeyword
	| Id of string
	| Int of int 
	| Error

let getInt tok =
	match tok with
	Int i -> i

let getId tok =
	match tok with
	Id str -> str