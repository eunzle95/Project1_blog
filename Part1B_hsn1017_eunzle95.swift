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
	("M", 1000), ("D", 500), ("C", 100),
	 ("L", 50), ("X", 10), ("V", 5), ("I", 1)
]
let exception: [(roman: String, number: Int )] = [
	("CM", 900), ("CD", 400), ("XC", 90), ("XL", 40), ("IX", 9), ("IV", 4)
]

let input = readLine()
if let input = input {
    var word: Character = " "
    var duplicates = 1
    var str = input
    var bool = true
    for c in input {
        
        let string = c
        // check for rule 3
        if ((word == string) && string == "V") ||
        ((word == string) && string == "L") ||
        ((word == string) && string == "D") {
            print("You are a Royal 🐸")
            bool = false
            break
        }
        else {  // check for rule 2
            if word == string {
                duplicates += 1
            }
            else {
                duplicates = 1
            }
            word = string
            if (duplicates > 4) {
                print("You are a Royal 🐶")
                bool = false
                break
            }
        }
        while str.count > 0 {
            if bool == false {
                break
            }
            for (roman, _) in exception {
                if str.starts(with: roman) {
                    print("You are a Royal 🐴")
                    bool = false
                    break
                }
            }
            for (roman, number) in dict {
                if str.starts(with: roman) {
                    result += number
                    str.removeFirst(roman.count)
                    break
                }
            }
        }
    }
    if bool {
        print(result)
    }
}