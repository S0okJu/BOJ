package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func Silver2512() {
	scanner := bufio.NewScanner(os.Stdin)

	// 첫 번째 줄 읽기
	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())

	// 두 번째 줄 읽기
	scanner.Scan()
	line := scanner.Text()
	numbers := strings.Split(line, " ")
	nums := make([]int, n)
	for i := 0; i < n; i++ {
		nums[i], _ = strconv.Atoi(numbers[i])
	}

	// 세 번째 줄 읽기
	scanner.Scan()
	m, _ := strconv.Atoi(scanner.Text())

	sort.Ints(nums)
	low, high := 0, max(nums[len(nums)-1])
	result := 0

	for low <= high {
		// 상한선 설정
		mid := (low + high) / 2

		// 상한선 적용
		total := 0
		for i := 0; i < n; i++ {
			total += min(mid, nums[i])
		}

		if total <= m {
			low = mid + 1
			result = mid
		} else {
			high = mid - 1
		}
	}
	fmt.Print(result)
}
