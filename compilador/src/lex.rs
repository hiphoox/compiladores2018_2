extern crate regex;
use self::regex::Regex;




pub fn lex( programa: &str) -> Vec<&str>{
    let tok: Vec<&str> = programa.split(' ').collect();
    println!("{:?}",tok);
    let reid = Regex::new(r"[A-Za-z][A-Za-z0-9_]*").unwrap();
    let reint = Regex::new(r"[0-9]+").unwrap();
    let rechar= Regex::new(r"[(){};]").unwrap();
    let mut tokf = vec!();
    for mut x in tok{
      if reid.is_match(x){
            let cap =reid.captures(x).unwrap();
            println!("{}",cap.get(0).map_or("", |m| m.as_str()));
            match cap.get(0).map_or("", |m| m.as_str()) {
                      "int" => tokf.push("IntKeyword"),
                      "return" => tokf.push("ReturnKeyword"),
                      _=> {tokf.push("identifier");
                      tokf.push(x);},
            }

      }
      if reint.is_match(x){
          let cap =reint.captures(x).unwrap();
              println!("{}",cap.get(0).map_or("", |m| m.as_str()));
              tokf.push(cap.get(0).map_or("", |m| m.as_str()));
      }
      if rechar.is_match(x){
      let rechar= Regex::new(r"[(){};]").unwrap();
            for cap in rechar.captures_iter(x){
              match cap.get(0).map_or("", |m| m.as_str()){
                  "{" => tokf.push("OpenBrace"),
                  "}"=> tokf.push("CloseBrace"),
                  "("=> tokf.push("OpenParen"),
                  ")"=> tokf.push("CloseParen"),
                  ";"=> tokf.push("SemiColon"),
                  _=> println!("error :("),
              }
              }

              }

    }
    tokf
}
