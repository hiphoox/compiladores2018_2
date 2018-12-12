use ast::*;

pub fn gen_exp(exp: &Exp)-> String{
    let ens: String=format!(" movl {} %eax",exp.Const.to_string());
    println!("{}",ens);
    ens
}
pub fn gen_st(st: &Statement)->String{
     let ens: String=" ret".to_string();
    let exp: String = gen_exp(&st.Return);
    ens
}
pub fn gen_fn(fun: &Fun_decl)->String{
     let ens: String= format!("_{}:",fun.nombre);
     println!("{}",ens);
    let st: String= gen_st(&fun.st);
    ens
}
pub fn gen_code(pg: &Prog)->String{
    let ens: String= "    .golbl _main".to_string();
    println!("{}",ens);
    let fun: String= gen_fn(&pg.prog);
    ens
}
