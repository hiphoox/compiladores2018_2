open Printf
open Str 

let rec implode c =
    let buf = Buffer.create 16 in 
        List.iter (Buffer.add_char buf) c;
        Buffer.contents buf

let rec explode_inner s i =
    if (String.length s ) = i then [] else
        s.[i]::explode_inner s (i+1)

let explode s = explode_inner s 0

let ejemplo = "hola H C"
let a = explode ejemplo;;

let b = implode a;;

List.iter (printf "%c /") a;;