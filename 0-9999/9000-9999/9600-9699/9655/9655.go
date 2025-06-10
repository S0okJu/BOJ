package main

import "fmt"

func solution(N int) string {
	turn := 1

	for {
		if N > 3 {
			N -= 3
		} else {
			N -= 1
		}

		if N == 0 {
			break
		}

		turn += 1
	}

	if turn%2 == 1 {
		return "SK"
	} else {
		return "CY"
	}
}

func main() {
	var N int
	fmt.Scanf("%d", &N)

	fmt.Println(solution(N))

}
