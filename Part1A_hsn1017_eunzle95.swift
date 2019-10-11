// 1	I
// 4	IV
// 5	V
// 9	IX
// 10	X
// 40	XL
// 50	L
// 90	XC
// 100	C
// 400	CD
// 500	D
// 900	CM
// 1000	M

var result = 0

let dict: [(roman: String, number: Int )] = [
	("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100),
	("XC", 90), ("L", 50), ("XL", 40), ("X", 10), ("IX", 9),
	("V", 5), ("IV", 4), ("I", 1)
]

let input = readLine()
if let input = input {
	var string = input
	while string.count > 0 {
		for (roman, number) in dict {
			if string.starts(with: roman) {
				result += number
				string.removeFirst(roman.count)
				break
			}
		}
	}
}

print(result)
