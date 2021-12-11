module Main where

import Data.Foldable
import Data.List
import qualified Data.Map as Map
import System.IO

main :: IO ()
main = do
  contents <- readFile "in.txt"
  let lines' = map (map ((\digit -> read digit :: Int) . (: []))) $ lines contents
  let width = length (head lines')
  let heightmap = replicate (width + 2) 9 : map (\line -> 9 : line ++ [9]) lines' ++ [replicate (width + 2) 9]
  putStrLn $ "Part 1: " ++ show (part1 heightmap)
  putStrLn $ "Part 2: " ++ show (part2 heightmap)

part1 :: [[Int]] -> Int
part1 heightmap = sum lowPoints + length lowPoints
  where
    lowPoints =
      foldl
        ( \acc i ->
            acc
              ++ foldl
                ( \acc' j ->
                    if heightmap !! i !! (j - 1) > heightmap !! i !! j
                      && heightmap !! i !! (j + 1) > heightmap !! i !! j
                      && heightmap !! (i - 1) !! j > heightmap !! i !! j
                      && heightmap !! (i + 1) !! j > heightmap !! i !! j
                      then acc' ++ [heightmap !! i !! j]
                      else acc'
                )
                []
                [1 .. length (head heightmap) - 2]
        )
        []
        [1 .. length heightmap - 2]

part2 :: [[Int]] -> Int
part2 heightmap = product $ lastN' 3 sizes'
  where
    sizes' = nub $ sort $ fst sizes
    sizes =
      foldl
        ( \acc i ->
            case foldl
              ( \acc' j ->
                  case groupSize i j (snd acc') heightmap 0 "initial" of
                    (s, v) -> if s /= 0 then (s : fst acc', v `Map.union` snd acc') else (fst acc', v `Map.union` snd acc')
              )
              ([], Map.empty)
              [0 .. length heightmap -1] of
              (ac, v) -> (fst acc ++ ac, snd acc `Map.union` v)
        )
        ([], Map.empty)
        [0 .. length (head heightmap) -1]

groupSize :: Int -> Int -> Map.Map (Int, Int) Bool -> [[Int]] -> Int -> String -> (Int, Map.Map (Int, Int) Bool)
groupSize x y visited heightmap size direction
  | x `elem` [0 .. length (head heightmap) -1] && y `elem` [0 .. length heightmap -1] && Map.notMember (x, y) visited && heightmap !! y !! x /= 9 =
    case direction of
      "initial" ->
        case groupSize (x + 1) y (visited `Map.union` Map.fromList [((x, y), True)]) heightmap 1 "right" of
          (sr, vr) ->
            case groupSize (x - 1) y vr heightmap (1 + sr) "left" of
              (sl, vl) ->
                case groupSize x (y + 1) vl heightmap (1 + sr + sl) "down" of
                  (sd, vd) ->
                    case groupSize x (y - 1) vd heightmap (1 + sr + sl + sd) "up" of
                      (su, vu) -> (1 + sr + sl + sd + su, vu)
      _ -> groupSize x y visited heightmap size "initial"
  | otherwise = (0, visited)

lastN' :: Int -> [a] -> [a]
lastN' n xs = foldl' (const . drop 1) xs (drop n xs)