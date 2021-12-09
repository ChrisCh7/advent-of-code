open System.IO

let lines =
    File.ReadAllLines("in.txt")
    |> Array.toList
    |> List.map (fun line ->
        line
        |> Seq.toList
        |> List.map string
        |> List.map int)

let width = lines.Head.Length
let mutable heightMap = [ List.replicate (width + 2) 9 ]

List.iter (fun line -> heightMap <- heightMap @ [ 9 :: line @ [ 9 ] ]) lines

heightMap <- heightMap @ [ List.replicate (width + 2) 9 ]

let part1 (heightMap: int list list) =
    let mutable lowPoints = []

    for i in [ 1 .. heightMap.Length - 2 ] do
        for j in [ 1 .. heightMap.Head.Length - 2 ] do
            if heightMap.[i].[j - 1] > heightMap.[i].[j]
               && heightMap.[i].[j + 1] > heightMap.[i].[j]
               && heightMap.[i - 1].[j] > heightMap.[i].[j]
               && heightMap.[i + 1].[j] > heightMap.[i].[j] then
                lowPoints <- lowPoints @ [ heightMap.[i].[j] ]

    List.sum lowPoints + lowPoints.Length
    |> printfn "Part 1: %A"

let rec groupSize (x: int) (y: int) (visited: Map<int * int, bool>) (heightMap: int list list) =
    let mutable size = 0
    let mutable visited = visited

    if x >= 0
       && x <= heightMap.Head.Length - 1
       && y >= 0
       && y <= heightMap.Length - 1
       && not (Map.containsKey (x, y) visited)
       && heightMap.[y].[x] <> 9 then
        visited <- visited |> Map.add (x, y) true
        size <- 1
        let right = groupSize (x + 1) y visited heightMap
        size <- size + fst right
        visited <- snd right
        let left = groupSize (x - 1) y visited heightMap
        size <- size + fst left
        visited <- snd left
        let down = groupSize x (y + 1) visited heightMap
        size <- size + fst down
        visited <- snd down
        let up = groupSize x (y - 1) visited heightMap
        size <- size + fst up
        visited <- snd up

    (size, visited)

let part2 (heightMap: int list list) =
    let mutable visited = Map.empty

    let mutable sizes = []

    for x in [ 0 .. heightMap.Head.Length - 1 ] do
        for y in [ 0 .. heightMap.Length - 1 ] do
            let size, visitedGroup = groupSize x y visited heightMap
            visited <- visitedGroup

            if size <> 0 then
                sizes <- sizes @ [ size ]

    sizes
    |> List.sortDescending
    |> List.take 3
    |> List.reduce (*)
    |> printfn "Part 2: %A"

part1 heightMap
part2 heightMap
