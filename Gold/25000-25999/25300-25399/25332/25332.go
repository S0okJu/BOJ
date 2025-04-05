package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func Solution(N int, A []int, B []int) int {

	diff_map := make(map[int]int)
	// 아무것도 더하지 않는 것도 부분합으로 간주한다.
	diff_map[0] = 1

	result := 0
	diff := 0

	// A,B 차이의 누적합이 같은 것은 것을 탐색
	// 누적합이 같다는 것은 합이 같다는 의미와 같음
	for idx := 0; idx < N; idx++ {
		diff += A[idx] - B[idx]
		result += diff_map[diff]
		diff_map[diff] += 1
	}
	return result
}

func readIntsLine(reader *bufio.Reader, N int) []int {
	nums := make([]int, N)
	for {
		line, _ := reader.ReadString('\n')
		fields := strings.Fields(line)
		if len(fields) >= N {
			for i := 0; i < N; i++ {
				nums[i], _ = strconv.Atoi(fields[i])
			}
			return nums
		}
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	// N 읽기
	line, _ := reader.ReadString('\n')
	N, _ := strconv.Atoi(strings.TrimSpace(line))

	A := readIntsLine(reader, N)
	B := readIntsLine(reader, N)

	result := Solution(N, A, B)
	fmt.Println(result)
}
