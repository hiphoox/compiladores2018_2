pub struct Exp {
  pub Const: i64,
  pub unop: bool,
}
pub struct Statement {
  pub Return: Exp,
}
pub struct Fun_decl {
  pub nombre: String,
  pub st: Statement,
}
pub struct Prog {
  pub prog: Fun_decl,
}

pub fn new_prog(x: Fun_decl)->Prog{
let new=Prog{ prog:x};
new
}
pub fn new_fn(st: Statement,name: String)->Fun_decl{
let new= Fun_decl{nombre:name,st:st};
new
}

pub fn new_st(exp: Exp)-> Statement{
let new= Statement{Return:exp};
new
}

pub fn new_exp(int:i64, u:bool)->Exp{
  let new= Exp{Const:int,unop:u};
  new
} 

pub fn print_tree(tree: Prog)->Prog{
println!("-------------impresión del arbol----------------------");
if tree.prog.st.Return.unop==false{
println!("prog->function {:?}->return-> constant: {:?}",tree.prog.nombre,tree.prog.st.Return.Const);
}else{
 println!("prog->function {:?}->return-> constant: -{:?}",tree.prog.nombre,tree.prog.st.Return.Const); 
}
tree
}



