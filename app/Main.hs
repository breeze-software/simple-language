module Main where
import Data.Either.Combinators

import Text.ParserCombinators.Parsec

csvFile = endBy line eol
line = sepBy cell (char ',')
cell = many (noneOf ",\n")

eol =   try (string "\n\r")
    <|> try (string "\r\n")
    <|> string "\n"
    <|> string "\r"
    <?> "end of line"

parseCSV :: String -> Either ParseError [[String]]
parseCSV input = parse csvFile "(unknown)" input

main :: IO ()
main = putStrLn (unlines (map unlines (fromRight' (parseCSV "1,2,3\n4,5,6\n\n"))))
