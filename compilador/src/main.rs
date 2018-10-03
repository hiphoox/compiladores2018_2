extern crate compilador;
use compilador::lex::*;
use compilador::parser::*;
//extern crate regex;
//use self::regex::Regex;



fn main(){
  //let re=Regex::new(r"[^0-9a-zA-Z(){}+; ]").unwrap();
   println!("holocrayolo");
   let s="int main() {
    return 2;
    }";



    //let programa = re.replace_all(s,"");
    let tokens: Vec<&str> =lex(&s);

    println!("{:?}",tokens);
    let ast:Vec<&str> = parsear(tokens);
    println!("{:?}",ast);


}
