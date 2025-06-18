package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	scanner.Scan()
	inp := scanner.Text()
	N, _ := strconv.Atoi(inp)

	words := make([]string, N)
	for i := 0; i < N; i++ {
		scanner.Scan()
		line := strings.TrimSpace(scanner.Text())
		words[i] = line
	}

	// Sorting
	sort.Slice(words, func(i, j int) bool {
		if len(words[i]) == len(words[j]) {
			return words[i] < words[j] // 사전순
		}
		return len(words[i]) < len(words[j]) // 길이 오름차순
	})

	// Remove duplication
	var result []string
	for i, word := range words {
		if i == 0 || word != words[i-1] {
			result = append(result, word)
		}
	}

	for _, word := range result {
		fmt.Println(word)
	}
}
