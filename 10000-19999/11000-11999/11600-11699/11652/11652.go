package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	// 첫 줄: N 입력
	scanner.Scan()
	N, _ := strconv.Atoi(scanner.Text())

	numDict := make(map[int]int)
	for i := 0; i < N; i++ {
		scanner.Scan()
		n, _ := strconv.Atoi(scanner.Text())
		numDict[n]++
	}

	// 최빈값 구하기
	first := true
	var maxValue int
	for _, v := range numDict {
		if first || v > maxValue {
			maxValue = v
			first = false
		}
	}

	// 최빈값 key들 모으기
	keys := make([]int, 0)
	for k, v := range numDict {
		if v == maxValue {
			keys = append(keys, k)
		}
	}
	sort.Ints(keys)
	fmt.Println(keys[0])
}
