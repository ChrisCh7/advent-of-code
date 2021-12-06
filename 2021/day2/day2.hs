module Main where

import System.IO

main :: IO ()
main = do
  contents <- readFile "in.txt"
  let instructions = map (\line -> (head (words line), read (last (words line)) :: Int)) $ lines contents
  putStrLn $ "Part 1: " ++ show (part1 (0, 0) instructions)
  putStrLn $ "Part 2: " ++ show (part2 (0, 0, 0) instructions)

part1 :: (Int, Int) -> [(String, Int)] -> Int
part1 (a, b) [] = a * b
part1 (a, b) (("forward", x) : xs) = part1 (a + x, b) xs
part1 (a, b) (("down", x) : xs) = part1 (a, b + x) xs
part1 (a, b) (("up", x) : xs) = part1 (a, b - x) xs

part2 :: (Int, Int, Int) -> [(String, Int)] -> Int
part2 (a, b, c) [] = a * b
part2 (a, b, c) (("forward", x) : xs) = part2 (a + x, b + c * x, c) xs
part2 (a, b, c) (("down", x) : xs) = part2 (a, b, c + x) xs
part2 (a, b, c) (("up", x) : xs) = part2 (a, b, c - x) xs
