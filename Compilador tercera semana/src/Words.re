let tradu = (t: string) =>{
    switch(t){
    | "ReturnKeyword" => "ret"
    | "Negation" => "neg"
    | "Bitwise" => "not"
    | "Multiplication" => "mul"
    | "Division" => "div"
    | "Addition" => "add"
      };
  };

let registro = (n: int) => {
    switch(n){
    | 0 => "%eax"
    | 1 => "%ebx"
    | 2 => "%ecx"
    | 3 => "%edx"
    }
};