package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {

	reader := bufio.NewReader(os.Stdin)

	firstLine, _ := reader.ReadString('\n')
	parts := strings.Fields(firstLine)
	n, _ := strconv.Atoi(parts[0])
	k, _ := strconv.Atoi(parts[1])

	secondLine, _ := reader.ReadString('\n')
	numStrings := strings.Fields(secondLine)
	inputData := make([]int, n)
	for i, numStr := range numStrings {
		inputData[i], _ = strconv.Atoi(numStr)
	}

	// 0으로 초기화
	sumDict := make(map[int]int)
	sumDict[0] = 1

	sum := 0
	answer := 0

	for _, data := range inputData {
		// fmt.Println(data)
		sum += data

		if val, exists := sumDict[sum-k]; exists {
			answer += val
		}

		sumDict[sum]++
	}

	fmt.Println(answer)
}
