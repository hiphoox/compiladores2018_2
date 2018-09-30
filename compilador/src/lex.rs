extern crate regex;
use self::regex::Regex;


pub enum Token{
    OpenBrace,
    CloseBrace,
    OpenParen,
    CloseParen,
    SemiColon,
    Identifier,
    IntKeyword,
    MainKeyword,
    ReturnKeyword,
    Int,

}





pub fn lex(programa: &str) -> Vec<&str>{
    let tok: Vec<&str> = programa.split(' ').collect();
    let reid = Regex::new(r"[A-Za-z][A-Za-z0-9_]*").unwrap();
    let reint = Regex::new(r"[0-9]").unwrap();
    let _rechar= Regex::new(r"[[:punct:]]").unwrap();
    let mut tokf = vec!();
    for x in tok{
      if reid.is_match(x){
          let cap =reid.captures(x).unwrap();
          println!("{}",cap.get(0).map_or("", |m| m.as_str()));
          match cap.get(0).map_or("", |m| m.as_str()) {
            "int" => tokf.push("IntKeyword"),
            "main" => tokf.push("MainKeyword"),
            "return" => tokf.push("ReturnKeyword"),
            _=> println!("id no encontrado"),
          }

      }
      if reint.is_match(x){
        let cap =reint.captures(x).unwrap();
        println!("{}",cap.get(0).map_or("", |m| m.as_str()));
        tokf.push(cap.get(0).map_or("", |m| m.as_str()));
      }
    }
    tokf
}
