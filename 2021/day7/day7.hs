module Main where

import Data.List
import System.IO

main :: IO ()
main = do
  contents <- readFile "in.txt"
  let positions = map (\pos -> read pos :: Int) $ wordsWhen (== ',') contents
  putStrLn $ "Part 1: " ++ show (part1 positions)
  putStrLn $ "Part 2: " ++ show (part2 positions)

part1 :: [Int] -> Int
part1 positions = foldl (\acc pos -> acc + abs (pos - medianPos)) 0 positions
  where
    medianPos = median positions

part2 :: [Int] -> Int
part2 positions = foldl (\acc pos -> acc + fuel pos meanPos) 0 positions
  where
    meanPos = mean positions

fuel :: Int -> Int -> Int
fuel position meanPos = fst $ foldl (\acc _ -> (uncurry (+) acc, snd acc + 1)) (0, 1) [0 .. abs (position - meanPos) - 1]

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s = case dropWhile p s of
  "" -> []
  s' -> w : wordsWhen p s''
    where
      (w, s'') = break p s'

median :: [Int] -> Int
median l =
  if even (length ls)
    then ls !! ((length ls `div` 2) - 1)
    else ls !! (length ls `div` 2)
  where
    ls = sort l

mean :: [Int] -> Int
mean l = sum l `div` length l
