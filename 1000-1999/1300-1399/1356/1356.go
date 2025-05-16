package main

import "fmt"

func ReputationCalculator(inp string) int64 {
	var result int64 = 1
	for i := 0; i < len(inp); i++ {
		result *= int64(inp[i] - '0')
	}
	return result
}

func Bronze1356() {
	// 문자열로 입력받는다.
	var input string
	fmt.Scanln(&input)

	// 일의 자리인 경우에는 무조건 0이다.
	if len(input) == 1 {
		fmt.Print("NO")
		return
	}

	// 앞부분, 뒷부분에 해당되는 값을 구한다.
	var front, back int64
	flag := "NO"
	for i := 0; i < len(input); i++ {
		front = ReputationCalculator(input[:i])
		back = ReputationCalculator(input[i:])
		if front == back {
			flag = "YES"
			break
		}
	}
	fmt.Print(flag)
}
