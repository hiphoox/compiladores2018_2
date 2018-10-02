
use std::ptr;


pub struct nodo{  //estructura nodo del arbol
  dato: String,
  hijos: Vec<*const nodo>,
  padre: *const nodo,
}

impl nodo{ // se especifican las funciones que puede hacer elelemento nodo
    fn new(dat: &str)-> nodo{
          nodo{
            dato: dat.to_string(),
            hijos: Vec::new(),
            padre: ptr::null(),
          }
    }
    fn agregar_hijo(mut self, hijo: nodo){//genera un apuntador al nodo y lo guarda en hijos
          let apun = &hijo as *const nodo;
          self.hijos.push(apun);
    }
    fn obtener_hijos(self)-> Vec<*const nodo>{
          self.hijos
    }
    fn obtener_padre (self)-> *const  nodo{
          self.padre
    }
    }



pub fn parcear(tokens: Vec<&str>)->nodo{
    let mut AST = nodo::new("programa"); //se crea el nodo inicial
    for i in 0..tokens.len(){
    match tokens[i]{

          "identifier"=>{ let temp=nodo::new(tokens[i+1]);
                AST.agregar_hijo(temp);
          },
          "ReturnKeyword"=>{ let temp=nodo::new(tokens[i]);
          Ast.agregar_hijo(temp);
          }
          "int"=>{ let temp=nodo::new(tokens[i+i]);
          Ast.agregar_hijo(temp);
          }
          &_=> ,

    }
}
AST
}
