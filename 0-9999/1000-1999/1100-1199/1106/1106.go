package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type CityInfo struct {
	cost      int
	customers int
}

func minSlice(arr []int) int {
	minVal := math.MaxInt32
	for _, val := range arr {
		if val < minVal {
			minVal = val
		}
	}
	return minVal
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func solutions() {
	scanner := bufio.NewScanner(os.Stdin)

	scanner.Scan()
	var C, N int
	fmt.Sscanf(scanner.Text(), "%d %d", &C, &N)

	infos := make([]CityInfo, N)
	for i := 0; i < N; i++ {
		scanner.Scan()
		words := strings.Fields(scanner.Text())

		cost, _ := strconv.Atoi(words[0])
		customers, _ := strconv.Atoi(words[1])

		infos[i] = CityInfo{cost: cost, customers: customers}
	}

	dp := make([]int, C+100)
	for i := range dp {
		dp[i] = int(1e7)
	}
	dp[0] = 0

	for _, info := range infos {
		for i := info.customers; i < C+100; i++ {
			dp[i] = min(dp[i-info.customers]+info.cost, dp[i])
		}
	}

	fmt.Println(minSlice(dp[C:]))
}

func main() {
	solutions()
}
