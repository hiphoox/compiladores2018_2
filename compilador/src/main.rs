extern crate compilador;
use compilador::lex::*;
extern crate regex;
use self::regex::Regex;



fn main(){
   println!("holocrayolo");
   let s="int main() {
    return 2;
}";
    let re=Regex::new(r"[^0-9a-zA-Z(){}+; ]").unwrap();
    let programa = re.replace_all(s,"");
    let tokens: Vec<&str> =lex(&programa);

    println!("{:?}",tokens);


}
