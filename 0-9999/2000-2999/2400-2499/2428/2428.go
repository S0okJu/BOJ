package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func solution(N int, files []int) int {

	sort.Slice(files, func(i, j int) bool {
		return files[i] < files[j]
	})

	result := 0

	left := 0
	for right := 0; right < N; right++ {
		for left < right && float64(files[left]) < 0.9*float64(files[right]) {
			left += 1
		}
		// left == right 인 경우 제외
		result += (right - left)
	}
	return result
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	line1, _ := reader.ReadString('\n')
	N, _ := strconv.Atoi(strings.TrimSpace(line1))

	line2, _ := reader.ReadString('\n')
	tokens := strings.Fields(line2)

	files := make([]int, N)
	for i := 0; i < N; i++ {
		files[i], _ = strconv.Atoi(tokens[i])
	}

	fmt.Println(solution(N, files))
}
