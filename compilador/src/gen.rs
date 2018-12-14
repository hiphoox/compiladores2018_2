use ast::*;


pub fn gen_exp(exp: &Exp)-> String{
    let final_exp:String;
    let ens: String=format!(" movl ${}, %eax",exp.Const.to_string());
    let sete: String="sete %al".to_string();
    let neg:String=format!(" neg %eax");
    if exp.ln_exist==false{
    if exp.unop==true {
        final_exp=format!("{}
    {}",ens,neg);
    }else{
        final_exp=ens;
    }
    }else{
        if exp.lg==true{
                if exp.unop==true {
                final_exp=format!("cmpl $1, %eax
    {}
    {}
    {}",ens,neg,sete);
                }else{
                final_exp=format!("cmpl $1, %eax
    {}
    {}",ens,sete);
                }
        }else{
                    if exp.unop==true {
                final_exp=format!("cmpl $0, %eax
    {}
    {}
    {}",ens,neg,sete);
                }else{
                final_exp=format!("cmpl $0, %eax
    {}
    {}",ens,sete);
                }
        }
    } 

    final_exp
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
