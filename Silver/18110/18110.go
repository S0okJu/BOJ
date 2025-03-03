package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
)

func solutions() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	N, _ := strconv.Atoi(scanner.Text())

	if N == 0 {
		fmt.Println(0)
		return
	}
	scores := make([]int, N)
	for i := 0; i < N; i++ {
		scanner.Scan()
		scores[i], _ = strconv.Atoi(scanner.Text())
	}
	sort.Ints(scores)

	threshold := int(math.Round(float64(N) * 0.15))
	sum := 0
	for i := threshold; i < N-threshold; i++ {
		sum += scores[i]
	}

	average := float64(sum) / float64(N-(threshold*2))

	averageRounded := int(math.Round(average))

	fmt.Println(averageRounded)
}

func main() {
	solutions()

}
