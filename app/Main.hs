module Main where
import Data.Either.Combinators

import Text.ParserCombinators.Parsec

sourceFile = many f
f = (string "fn") <|> (string " ")
--sourceFile = endBy line eol
--line = many (noneOf "\n")
--line = sepBy cell (char '#')
--cell = many (noneOf "#\n")

eol =   try (string "\n\r")
    <|> try (string "\r\n")
    <|> string "\n"
    <|> string "\r"
    <?> "end of line"

parseSource :: String -> Either ParseError [String]
parseSource input = (parse sourceFile "" input)

unwrap s = (show (fromRight' (parseSource s)))

main :: IO ()
main = putStrLn (unwrap "fn something(a, b, c):\n    return a + b * c\n")
