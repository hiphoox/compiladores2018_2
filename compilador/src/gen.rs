use ast::*;


pub fn gen_exp(exp: &Exp)-> String{
    let ens: String=format!(" movl {} %eax",exp.Const.to_string());
    ens
}
pub fn gen_st(st: &Statement)->String{
     let ens: String=format!("{}
     {}"," ret".to_string(),gen_exp(&st.Return));
    ens
}
pub fn gen_fn(fun: &Fun_decl)->String{
    let ens: String= format!("_{}:
    {}",fun.nombre,gen_st(&fun.st));
    ens
}
pub fn gen_code(pg: &Prog)->String{
    let ens: String=format!( "    .golbl _main
    {}",gen_fn(&pg.prog));
    ens
}
