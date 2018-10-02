

pub struct nodo{
  dato: String,
  hijos: Vec<nodo>,
}

impl nodo{
    fn new(dat: &str)-> nodo{
          nodo{
            dato: dat.to_string(),
            hijos,
          }
    }

    fn agregar_hijo(hijo: nodo,padre: nodo){
          padre.hijos.push(hijo);
    }
    fn abrir_hijos(padre: nodo)-> Vec<nodo>{
      padre.hijos
    }
    fn agregar_hasta_abajo(hijo: nodo,padre: nodo){
        if padre.hijos.len() != 0{
          let nodos: Vec<_> = nodo::abrir_hijos(padre);
          nodo::agregar_hasta_abajo(hijo, nodos[0]);
          }
        nodo::agregar_hijo(hijo,padre);
    }
}

pub fn parcear(tokens: Vec<&str>)->nodo{
    let AST = nodo::new("programa");
    let mut temp: String;
    let mut program: nodo;
    let mut function_declaration: nodo;
    let mut statement: nodo;
    let mut exp: nodo;
    for i in tokens.len(){
        match tokens[i]{

        "identifier"=>{ nodo::agregar_hijo(nodo::new(tokens[i+1]),AST);
        temp= tokens[i-1];},
        "returnkeyword" =>{ nodo::agregar_hijo(nodo::new(tokens[i]),AST);
        nodo::agregar_hasta_abajo(nodo::new(tokens[i+1]),AST);

        },



        }
    }
    AST

}
