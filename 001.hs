main = do
	print(probOne 999)

probOne :: Int -> Int
probOne n
	| (n <= 1 ) = 0
	| otherwise = foldl (+) 0 (threeAndFive [1..n])

threeAndFive :: [Int] -> [Int]
threeAndFive [] = []
threeAndFive (x:xs)
	| (mod x 3 == 0) || (mod x 5 == 0) = [x] ++ threeAndFive xs
	| otherwise = threeAndFive xs
