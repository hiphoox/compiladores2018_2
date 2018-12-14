try
	begin match Sys.argv with
	[|_; nombre|] -> 
		let toks = Lexer.toks_from_filename nombre in
		let ast = Parser.parse_program toks in
		let code_gen = Generator.generate_code ast "" in
		print_string "--  Token List --";
		print_newline ();
		Lexer.print_toklist toks;
		print_newline ();
		print_string "--    AST   -- (Pretty Printed)";
		print_newline ();
		Parser.print_ast ast;
		print_newline ();
		print_string "-- Code Output --";
		print_newline ();
		print_string "Code Generated in file: Output.asm";
		print_newline ()

	|[|_; nombre; "-o"; output_filename|] ->
		let toks = Lexer.toks_from_filename nombre in
		let ast = Parser.parse_program toks in
		let outfile = String.concat "" [output_filename;".asm"] in
		let code_gen = Generator.generate_code ast outfile in
		print_string "--  Token List --";
		print_newline ();
		Lexer.print_toklist toks;
		print_newline ();
		print_string "--    AST   -- (Pretty Printed)";
		print_newline ();
		Parser.print_ast ast;
		print_newline ();
		print_string "-- Code Output --";
		print_newline ();
		print_string "Code Generated in file: ";print_string outfile;
		print_newline ()

	|[|_; "-l"; nombre|] ->
		let toks = Lexer.toks_from_filename nombre in
		print_string "--  Token List --";
		print_newline ();
		Lexer.print_toklist toks
	
	|[|_; "-p"; nombre|] ->
		let toks = Lexer.toks_from_filename nombre in
		let ast = Parser.parse_program toks in
		print_string "--    AST   -- (Pretty Printed)";
		print_newline ();
		Parser.print_ast ast

	|[|_; "-g"; nombre|] ->
		let toks = Lexer.toks_from_filename nombre in
		let ast = Parser.parse_program toks in
		let code_gen = Generator.generate_code ast "" in
		print_string "-- Code Output --";
		print_newline ();
		print_string "Code Generated in file: Output.asm";
		print_newline ()

	|[|_; "-g"; nombre; "-o"; output_filename|] ->
		let toks = Lexer.toks_from_filename nombre in
		let ast = Parser.parse_program toks in
		let outfile = String.concat "" [output_filename;".asm"] in
		let code_gen = Generator.generate_code ast outfile in
		print_string "-- Code Output --";
		print_newline ();
		print_string "Code Generated in file: ";print_string outfile;
		print_newline ()

	|_ ->
		print_string "Usage:  ./nqcc <opc> <filename>";
		print_newline ();
		print_string "<Opc>:";
		print_newline ();
		print_string "-l -> lexer";
		print_newline ();
		print_string "-p -> parser";
		print_newline ();
		print_string "-g -> code generator";
		print_newline ();
		print_string "-o <output_filename> if using code generator like: ./nqcc -g <filename> -o <output_filename>";
		print_newline ()
	end
with
	e -> 
		print_string "Ocurrio un error: ";
		print_string (Printexc.to_string e);
		print_newline ();
		exit 1