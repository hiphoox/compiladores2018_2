/* Esto es un comenario*/
let variable = 123;

let id = x => x;
let add = (x, y) => x + y;

let _resultado = add(3, 4);
Js.log("asdasdasdas");

type color =
  | Red
  | Green
  | Blue;

let stringOfColor = (c: color) =>
  switch (c) {
  | Red => "red"
  | Green => "green"
  | Blue => "blue"
  };

Js.log(stringOfColor(Green));

type tree =
  | Leaf
  | Node(int, tree, tree);

let rec sum = item =>
  switch (item) {
  | Leaf => 0
  | Node(value, left, right) => value + sum(left) + sum(right)
  };

let miArbol =
  Node(
    1,
    Node(7, Node(4, Leaf, Leaf), Node(6, Leaf, Leaf)),
    Node(5, Node(10, Leaf, Leaf), Node(60, Leaf, Leaf)),
  );

let resultado = sum(miArbol);
Js.log(resultado);

let times2 = (x: int) => x * 2;
let twice = (s: string) => s ++ s;

let result = 4 |> times2 |> string_of_int |> twice;
Js.log({j|Result: $result|j});

let _items = Belt.Set.Int.fromArray([|3, 5, 2, 5, 4, 6, 2|]);

let items = [1, 2, 3, 4, 5];
let items2 = [0, ...items];
Js.log(items2);

let itme2 = [];
let [head, ...tail] = itme2;

Js.log(head);
Js.log(tail);
Js.log(items);