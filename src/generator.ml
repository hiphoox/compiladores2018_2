(* Mauricio Esparza. Generador de código ensamblador para c*)

let ast_fun_name (n,_,_) = n

let ast_ret_val (_,i,_) = string_of_int i

let ast_statement (_,_,s) = Parser.stat_to_string s

let ast_to_asm_channel ch astdata =
	match astdata with
	(_,_,state) -> if state = "Return statement"
	then 
	output_string ch ".globl _"; output_string ch (ast_fun_name astdata);	(*.globl _<fun_name>*)
	output_char ch '\n';
	output_char ch '_'; output_string ch (ast_fun_name astdata); (* _<fun_name> *)
	output_char ch '\n';
	output_string ch "movl $"; output_string ch (ast_ret_val astdata);
	output_string ch ", %eax";
	output_char ch '\n';
	output_string ch "ret"

let ast_to_asm_to_file astdata filename =
	let channel = open_out filename in
	ast_to_asm_channel channel astdata ;
	close_out channel

let get_data ast =
	match ast with
	  (Parser.Root (prog,_)) ->
		let program = prog in
		let fun_decl = Parser.get_funct_of_prog program in
		let statement = Parser.get_stmnt_of_funct fun_decl in
		let expression = Parser.get_exp_of_statement statement in
		let fun_name = Parser.get_funct_name (fun_decl) in
		let ret_val = Parser.get_value_of_exp (expression) in
		let ast_data = (fun_name,ret_val,Parser.stat_to_string statement) in
		ast_data

	| (Parser.Node) -> print_string "Empty AST";("",0,"")

let generate_code asynt output_filename = (* Aquí llega el AST del parser *)
	let ast_data = get_data asynt in
	if output_filename = "" 
	then ast_to_asm_to_file ast_data "Output.asm"
	else ast_to_asm_to_file ast_data output_filename
	
(*Texto deseado:
	.globl _<fun_name>
	_<fun_name>
	movl $<ret_val>, %eax
	ret
*)