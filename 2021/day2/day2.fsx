open System.IO

let lines =
    File.ReadAllLines("in.txt")
    |> Array.toList
    |> List.map (fun instr -> ((instr.Split " ").[0], (instr.Split " ").[1] |> int))

let rec part1 =
    function
    | ((a, b), []) -> a * b
    | ((a, b), ("forward", x) :: xs) -> part1 ((a + x, b), xs)
    | ((a, b), ("down", x) :: xs) -> part1 ((a, b + x), xs)
    | ((a, b), ("up", x) :: xs) -> part1 ((a, b - x), xs)
    | _ -> 0

let rec part2 =
    function
    | ((a, b, _), []) -> a * b
    | ((a, b, c), ("forward", x) :: xs) -> part2 ((a + x, b + c * x, c), xs)
    | ((a, b, c), ("down", x) :: xs) -> part2 ((a, b, c + x), xs)
    | ((a, b, c), ("up", x) :: xs) -> part2 ((a, b, c - x), xs)
    | _ -> 0

part1 ((0, 0), lines) |> printfn "Part 1: %A"
part2 ((0, 0, 0), lines) |> printfn "Part 2: %A"
