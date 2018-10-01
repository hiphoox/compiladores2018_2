extern crate compilador;
use compilador::lex::*;
extern crate regex;
use self::regex::Regex;



fn main(){
  let re=Regex::new(r"[^0-9a-zA-Z(){}+; ]").unwrap();
   println!("holocrayolo");
   let s="int main() {
    return 222;
    }";

  

    let programa = re.replace_all(s,"");
    let tokens: Vec<&str> =lex(&programa);

    println!("{:?}",tokens);


}
