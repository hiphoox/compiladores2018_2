extern crate regex;

use self::regex::Regex;


pub fn lex( programa: &str) -> Vec<&str>{
    let tok: Vec<&str> = programa.split(' ').collect();// se divide la cadena por  espacios
    println!("{:?}",tok);
    let reid = Regex::new(r"[A-Za-z][A-Za-z
    _]*").unwrap();//se declaran las expresiones regulares en estas 3 lineas
    let reint = Regex::new(r"[0-9]+").unwrap();
    let rechar= Regex::new(r"[(){};]").unwrap();
    let reneg= Regex::new(r"[~!/-]").unwrap();
    let mut tokf = vec!();//se crea "token final" para ir incertando ahi el resultado del lexer
    for mut x in tok{// ciclo en el que se irán analizando elemento por elemento para etiquetarlo



      if reid.is_match(x){// en caso de encontrar algo de identificadores:
            let cap =reid.captures(x).unwrap();// se obtiene primero la captura de los identificadore
          
            match cap.get(0).map_or("", |m| m.as_str()) {//se reviza si  es alguna de nuestras 2 keywords
                      "int" => tokf.push("IntKeyword"),
                      "return" => tokf.push("ReturnKeyword"),
                      _=> {tokf.push("identifier");// de no ser ninguna se guarda la etiqueta "identificador"
                      tokf.push(cap.get(0).map_or("", |m| m.as_str()));},// seguido del identificador en si
            }

      }
      if reneg.is_match(x){//en caso de encontrar algun caracter de negación
             for cap in reneg.captures_iter(x){//se inicia un ciclo, ya que puede haber mas de uno
              match cap.get(0).map_or("", |m| m.as_str()){// captura de uno en uno y compara, guardando la etiqueta correspondiente
                  "-"=> tokf.push("Negation"),
                  "!"=> tokf.push("Logical negation"),
                  "~"=> tokf.push("Bitwise complement"),
                  _=> println!("error :("),// si es un caracter no aceptado, imprime error
              }
              }


      }
      if reint.is_match(x){//en caso de encontrar un entero, se guarda  el numero de uno o mas digitos encontrado
          let cap =reint.captures(x).unwrap();
              println!("{}",cap.get(0).map_or("", |m| m.as_str()));
              tokf.push("int");
              tokf.push(cap.get(0).map_or("", |m| m.as_str()));
      }
      if rechar.is_match(x){//en caso de encontrar algun caracter hace lo siguiente

            for cap in rechar.captures_iter(x){//se inicia un ciclo, ya que puede haber mas de uno
              match cap.get(0).map_or("", |m| m.as_str()){// captura de uno en uno y compara, guardando la etiqueta correspondiente
                  "{" => tokf.push("OpenBrace"),
                  "}"=> tokf.push("CloseBrace"),
                  "("=> tokf.push("OpenParen"),
                  ")"=> tokf.push("CloseParen"),
                  ";"=> tokf.push("SemiColon"),
                  _=> println!("error :("),// si es un caracter no aceptado, imprime error
              }
              }

              }

    }
    tokf
}
