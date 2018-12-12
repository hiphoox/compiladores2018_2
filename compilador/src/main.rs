extern crate compilador;
use compilador::lex::*;
use compilador::parser::*;
use compilador::ast::*;




fn main(){
  //let re=Regex::new(r"[^0-9a-zA-Z(){}+; ]").unwrap();
   println!("holocrayolo");
   let s="int main() {
    return 2;
    }";



    //let programa = re.replace_all(s,"");
    let tokens: Vec<&str> =lex(&s);

    println!("{:?}",tokens);
    let ast:Prog = parsear(tokens);
    print_tree(ast);
  
}
