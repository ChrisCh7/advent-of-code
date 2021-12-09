module Main where

import System.IO

main :: IO ()
main = do
  contents <- readFile "in.txt"
  let depths = map (\line -> read line :: Int) $ lines contents
  putStrLn $ "Part 1: " ++ show (part1 depths)
  putStrLn $ "Part 2: " ++ show (part2 depths)

part1 :: [Int] -> Int
part1 depths = foldl (\acc i -> if (depths !! i) > (depths !! (i - 1)) then acc + 1 else acc) 0 [1 .. length depths - 1]

part2 :: [Int] -> Int
part2 depths = foldl (\acc i -> if sum3 depths i > sum3 depths (i - 1) then acc + 1 else acc) 0 [3 .. length depths - 1]

sum3 :: [Int] -> Int -> Int
sum3 depths i = depths !! i + depths !! (i - 1) + depths !! (i - 2)
