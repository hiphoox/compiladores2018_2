let a_lista s = 
    let rec a_lista_rec substr substr_len =
        match substr with
        | "" -> [] | _ -> (String.get substr 0)::a_lista_rec (String.sub substr 1 (substr_len - 1)) (substr_len - 1)
    in
a_lista_rec s (String.length s)
	let rec a_cadena chars =
		match chars with
		| [] -> "" | c::cs -> String.make 1 c ^ a_cadena cs