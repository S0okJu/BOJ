package main

import "fmt"

func isMatch(a byte, b byte) bool {
	if a == '2' && b == '2' {
		return false
	}
	return true
}

func solution(A string, B string) int {
	a := len(A)
	b := len(B)
	result := a + b

	for offset := -b; offset <= a; offset++ {
		ok := true

		for i := 0; i < b; i++ {
			j := offset + i
			if 0 <= j && j < a {
				if !isMatch(A[j], B[i]) {
					ok = false
					break
				}
			}
		}

		if ok {
			left := min(0, offset)
			right := max(a, offset+b)
			result = min(result, right-left)
		}
	}

	return result
}

func main() {
	var A string
	fmt.Scanln(&A)

	var B string
	fmt.Scanln(&B)

	fmt.Println(solution(A, B))
}
