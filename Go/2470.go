package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func Gold2470() {
	// 빠른 입력을 위해 bufio 사용
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	// 첫 번째 값 입력 (n)
	var n int
	fmt.Fscan(reader, &n)

	// 배열 입력 받기
	slice := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &slice[i])
	}

	// 정렬
	sort.Ints(slice)

	// 투 포인터 알고리즘
	left, right := 0, n-1
	minDiff := 2000000000
	ans1, ans2 := 0, 0

	for left < right {
		sum := slice[left] + slice[right]
		absSum := sum
		if sum < 0 {
			absSum = -sum
		}

		if absSum < minDiff {
			minDiff = absSum
			ans1, ans2 = slice[left], slice[right]
		}

		// 투 포인터 이동
		if sum < 0 {
			left++
		} else {
			right--
		}
	}

	// 출력
	fmt.Fprintln(writer, ans1, ans2)
}

// func main() {
// 	Gold2470()
// }
