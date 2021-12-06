module Main where

import System.IO

main :: IO ()
main = do
  contents <- readFile "in.txt"
  let depths = map (\line -> read line :: Int) $ lines contents
  putStrLn $ "Part 1: " ++ show (day1 depths)
  putStrLn $ "Part 2: " ++ show (day2 depths)

day1 :: [Int] -> Int
day1 depths = foldl (\acc i -> if (depths !! i) > (depths !! (i - 1)) then acc + 1 else acc) 0 [1 .. length depths - 1]

day2 :: [Int] -> Int
day2 depths = foldl (\acc i -> if sum3 depths i > sum3 depths (i - 1) then acc + 1 else acc) 0 [3 .. length depths - 1]

sum3 :: [Int] -> Int -> Int
sum3 depths i = depths !! i + depths !! (i - 1) + depths !! (i - 2)
