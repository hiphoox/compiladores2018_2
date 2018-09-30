extern crate compilador;
use compilador::lex::*;


fn main(){
   println!("holocrayolo");
   let s="int main() {
    return 2;
}"; 
    let tokens: Vec<Token> =lex(s);



}
