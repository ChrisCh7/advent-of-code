module Main where

import qualified Data.Set as S
import qualified Data.List as L
import System.IO

main :: IO()
main = do
    contents <- readFile "in.txt"
    let numbers = map (\line -> read line :: Int) $ lines contents
    print $ "Part 1: " ++ show (day1 numbers 2)
    print $ "Part 2: " ++ show (day1 numbers 3)

day1 :: [Int] -> Int -> Int
day1 xs n = product numbers
    where sums = map (\nr -> (nr, sum nr)) $ sequence $ take n $ repeat xs
          numbers = fst $ maybe (take n $ repeat 0, 0) id $ L.find (\x -> (snd x) == 2020) $ sums