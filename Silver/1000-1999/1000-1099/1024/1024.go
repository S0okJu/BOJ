package main

import "fmt"

func Solution(N int, L int) []int {
	for length := L; length <= 100; length++ {
		temp := N - (length*(length-1))/2

		if temp < 0 {
			continue
		}

		if temp%length == 0 {
			a := temp / length
			result := make([]int, length)
			for i := 0; i < length; i++ {
				result[i] = i + a
			}
			return result
		}
	}
	return nil
}
func main() {
	var N, L int
	fmt.Scan(&N, &L)

	result := Solution(N, L)
	if result == nil {
		fmt.Println(-1)

	} else {
		for _, v := range result {
			fmt.Printf("%d ", v)
		}
	}
}
