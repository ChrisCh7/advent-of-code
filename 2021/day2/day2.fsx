open System.IO

let lines =
    File.ReadAllLines("in.txt")
    |> Array.toList
    |> List.map (fun instr ->
        [ (instr.Split " ").[0]
          (instr.Split " ").[1] ])

let part1 (instructions: string list list) =
    let mutable pos = [ 0; 0 ]

    List.iter
        (fun instr ->
            match instr with
            | [ "forward"; x ] -> pos <- [ pos.[0] + (x |> int); pos.[1] ]
            | [ "down"; x ] -> pos <- [ pos.[0]; pos.[1] + (x |> int) ]
            | [ "up"; x ] -> pos <- [ pos.[0]; pos.[1] - (x |> int) ]
            | _ -> ())
        instructions

    printfn "Part 1: %A" (pos.[0] * pos.[1])

let part2 (instructions: string list list) =
    let mutable pos = [ 0; 0; 0 ]

    List.iter
        (fun instr ->
            match instr with
            | [ "forward"; x ] ->
                pos <-
                    [ pos.[0] + (x |> int)
                      pos.[1] + pos.[2] * (x |> int)
                      pos.[2] ]
            | [ "down"; x ] ->
                pos <-
                    [ pos.[0]
                      pos.[1]
                      pos.[2] + (x |> int) ]
            | [ "up"; x ] ->
                pos <-
                    [ pos.[0]
                      pos.[1]
                      pos.[2] - (x |> int) ]
            | _ -> ())
        instructions

    printfn "Part 2: %A" (pos.[0] * pos.[1])

part1 lines
part2 lines
