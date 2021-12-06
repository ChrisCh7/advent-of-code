open System.IO

let lines =
    File.ReadAllLines("in.txt")
    |> Array.toList
    |> List.map int

let part1 (depths: int list) =
    [ 1 .. depths.Length - 1 ]
    |> List.fold
        (fun acc i ->
            if depths.[i] > depths.[i - 1] then
                acc + 1
            else
                acc)
        0
    |> printfn "Part 1: %A"

let part2 (depths: int list) =
    let mutable nrIncreases = 0
    let mutable prevSum = 0

    for n in [ 0 .. depths.Length - 3 ] do
        if prevSum = 0 then
            prevSum <- depths.[n] + depths.[n + 1] + depths.[n + 2]
        else
            let currentSum =
                depths.[n] + depths.[n + 1] + depths.[n + 2]

            if currentSum > prevSum then
                nrIncreases <- nrIncreases + 1

            prevSum <- currentSum

    printfn "Part 2: %A" nrIncreases

part1 lines
part2 lines
