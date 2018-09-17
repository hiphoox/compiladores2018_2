let read_lines file process = 
    let in_ch = open_in file in 
    let rec read_line() = 
    let line = try input_line in_ch with End_of_file -> exit 0 
    in (* process line in this block, then read the next line *) 
     process line; 
     read_line(); 
in read_line();; 

read_lines "../Pruebas/code.c" print_endline;; 