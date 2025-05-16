package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func Solution(N int, A []int, B []int) int {
	// A는 오름차순으로 정렬
	sort.Ints(A)

	// B는 내림차순으로 정렬
	sort.Sort(sort.Reverse(sort.IntSlice(B)))

	result := 0
	for i := 0; i < N; i++ {
		result += (A[i] * B[i])
	}

	return result

}

func main() {
	reader := bufio.NewReader(os.Stdin)

	line, _ := reader.ReadString('\n')
	n, _ := strconv.Atoi(strings.TrimSpace(line))

	A := make([]int, n)
	B := make([]int, n)

	line, _ = reader.ReadString('\n')
	fields := strings.Fields(line)

	for key, val := range fields {
		A[key], _ = strconv.Atoi(val)
	}

	line, _ = reader.ReadString('\n')
	fields = strings.Fields(line)
	for key, val := range fields {
		B[key], _ = strconv.Atoi(val)
	}

	result := Solution(n, A, B)
	fmt.Println(result)
}
