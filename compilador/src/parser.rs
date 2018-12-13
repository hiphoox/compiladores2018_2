use ast::*;



pub fn parsear(tokens: Vec<&str>)-> Prog{
if tokens.len()==0{
    println!("error, lexer vacio");
    unreachable!();

}  
let ast: Prog= new_prog(funcion(tokens));
ast
}



pub fn funcion(tokens: Vec<&str>)-> Fun_decl{
if tokens[0] != "IntKeyword"{
println!("eror, falta IntKeyword");
unreachable!();
}else if tokens[1] != "identifier" || tokens[2]!="main"{
println!("error en la declaración de funcion");
unreachable!();
}else if tokens[3] != "OpenParen"|| tokens[4]!="CloseParen"{
println!("faltan parentesis al main");
unreachable!();
}else if tokens[5] !="OpenBrace"{
println!(" no se abrio llave para el statement");
unreachable!();
}

let temp = &tokens[6..];
let ast: Fun_decl=new_fn(statement(temp.to_vec()),"main".to_string());
if tokens[tokens.len() - 2] != "SemiColon" || tokens[tokens.len() -1] != "CloseBrace"{
println!("error en cerrar funcion");
unreachable!();
}
ast
}



pub fn statement(tokens: Vec<&str>)->Statement{
 
  if tokens[0] != "ReturnKeyword"{
  println!("error, falta return");
  unreachable!();
  }
   let tempo= &tokens[1..];
let temp: Statement=new_st(operator(tempo.to_vec())); 
temp
}

pub fn operator(tokens: Vec<&str>)-> Exp{
let mut con=0;
let bole: bool;
    for n in &tokens{
        if n == &"Negation".to_string() || n == &"Bitwise complement".to_string() {
        con = con+1;
        }
    }
    if con%2==0{
         bole = false;
    }else{
         bole = true;
    }
    let tempo= &tokens[(con)..];
    let exp= exp(tempo.to_vec(),bole);
    exp
    }
pub fn exp(tokens: Vec<&str>,b:bool)->Exp{
if tokens[0]!= "int"{
      println!("error en valor del return");
      unreachable!();
}
let temp: i64;
let tempo=tokens[1].to_string();
temp=tempo.parse().unwrap();
let expr: Exp=new_exp(temp,b);
expr
}
