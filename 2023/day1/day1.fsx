open System.IO
open System.Text.RegularExpressions


let isNumber (input: string) =
    match System.Int32.TryParse(input) with
    | true, _ -> true
    | false, _ -> false

let replaceNumbers (input: string) =
    input
        .Replace("one", "1")
        .Replace("two", "2")
        .Replace("three", "3")
        .Replace("four", "4")
        .Replace("five", "5")
        .Replace("six", "6")
        .Replace("seven", "7")
        .Replace("eight", "8")
        .Replace("nine", "9")

let lines = File.ReadAllLines("in.txt") |> Array.toList

let pattern =
    Regex(@"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", RegexOptions.Compiled)

let mutable sumP1 = 0
let mutable sumP2 = 0

for line in lines do
    let matches =
        pattern.Matches line |> Seq.map (fun m -> m.Groups[1].Value) |> Seq.toList

    let matchesP1 = matches |> List.filter isNumber
    sumP1 <- sumP1 + System.Int32.Parse(matchesP1.Head + matchesP1[matchesP1.Length - 1])

    let matchesP2 = matches |> List.map replaceNumbers
    sumP2 <- sumP2 + System.Int32.Parse(matchesP2.Head + matchesP2[matchesP2.Length - 1])

printfn "Part 1: %A" sumP1
printfn "Part 2: %A" sumP2
