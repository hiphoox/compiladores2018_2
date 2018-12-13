extern crate compilador;

use compilador::lex::*;
use compilador::parser::*;
use compilador::ast::*;
use compilador::gen::*;
use std::fs::OpenOptions;
use std::fs::write;
use std::fs::read_to_string;




fn main(){
  let file = OpenOptions::new()
            .read(true)
            .write(true)
            .create(true)
            .open("assembly.s");
  
   let s=read_to_string("prueba.c").expect("no se pudo leer el archivo");

    let tokens: Vec<&str> =lex(&s);
    println!("------------impresion de los tokens-------------");
    println!("{:?}",tokens);
    let ast:Prog = parsear(tokens);
    let ast:Prog=print_tree(ast);
    let code: String=gen_code(&ast);
    println!("------------impresion del codigo-------------");
    print!("{}",&code);
    write("assembly.s", code).expect("no se pudo generar assembly.s");
    
  
}
