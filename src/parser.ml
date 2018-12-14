(* Mauritio Esparza, parser para AST de C *)
type exp = Const of int

type statement = Return of exp

type fun_decl = Fun of string * statement

type prog = Prog of fun_decl

type ast = 
	  Root of prog * ast
	| Node

(* 	

<program> ::= <function>
<function> ::= "int" <id> "(" ")" "{" <statement> "}"
<statement> ::= "return" <exp> ";"
<exp> ::= <int>

<> no terminales
"" terminales
*) 

(* val getConstant : exp -> int = <fun>
Recibe una expresión Constant of int y regresa su valor numérico, o su contenido*)
let get_value_of_exp expr =
	match expr with
	(Const i) -> i

let get_exp_of_statement state =
	match state with
	(Return e) -> e

let get_stmnt_of_funct fund =
	match fund with
	(Fun (_, st)) -> st

let get_funct_name fund =
	match fund with
	(Fun (str, _)) -> str

let get_funct_of_prog pro =
	match pro with
	(Prog f) -> f

let get_prog_of_ast asynt =
	match asynt with
	(Root (prog,_)) -> prog

let exp_to_string exp =
	match exp with
	(Const i) -> print_string "Exp is Constant of value: ";print_int i

let stat_to_string stat =
	match stat with
	(Return e) -> "Return statement"

let print_ast ast =
	match ast with
	  Root (prog,_) ->
		let program = prog in
		let fun_decl = get_funct_of_prog program in
		let statement = get_stmnt_of_funct fun_decl in
		let expression = get_exp_of_statement statement in
		print_string "Root:       Program";print_newline ();
		print_string "Function:   ";print_string (get_funct_name (fun_decl));print_newline ();
		print_string "Statement:  ";print_string (stat_to_string (statement));print_newline ();
		print_string "Expression: ";exp_to_string (expression);print_newline ();
	| Node -> print_string "Empty AST";print_newline ()


let parse_exp toklist = (*parse_exp va a sacar más tokens de la lista*)
	match toklist with
	| (Tokens.Int x) -> (Const x)


let rec parse_statement toklist =
	match toklist with
	  [] -> Return(Const 0)
	| Tokens.ReturnKeyword::expre::Tokens.Semicolon::rest -> Return (parse_exp expre)


(* Verifica que se cierre un corchete, el programador debe asegurarse de que se abra, preferiblemente desde el pattern matching*)
let rec brace_closes toklist =
	match toklist with
	  [] -> false
	| h::t -> if h = Tokens.CloseBrace then true else brace_closes t

(*Quita el primer corchete que cierra de la lista de tokens*)
let rec drop_one_closebrace oldli newli =
	match oldli with
	[] -> []
	|h::t -> if h = Tokens.CloseBrace
			then newli@t
			else drop_one_closebrace t ((newli)@[h])


let parse_function_declaration toklist =
	match toklist with
	  [] -> Fun("Empty Program",Return(Const 0))
	| Tokens.IntKeyword::Tokens.MainKeyword::Tokens.OpenParen::Tokens.CloseParen::Tokens.OpenBrace::rest -> 
		if brace_closes rest = true
			then Fun("Main",parse_statement (drop_one_closebrace rest [])) 
		else Fun("CloseBrace Missing",Return(Const 0))
	| Tokens.IntKeyword::(Tokens.Id s)::Tokens.OpenParen::Tokens.CloseParen::Tokens.OpenBrace::rest -> 
		if brace_closes rest = true
			then Fun((Tokens.getId (List.nth toklist 1)),parse_statement (drop_one_closebrace rest [])) 
		else Fun("CloseBrace Missing",Return(Const 0))


let parse_program toklist = (*Aquí entra todo*)
	match toklist with
	  [] -> Node
	| _ -> let ast = Root(Prog (parse_function_declaration toklist), Node) in ast