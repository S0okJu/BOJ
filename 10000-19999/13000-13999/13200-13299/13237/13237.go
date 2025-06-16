package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())

	parents := make([]int, n+1)
	children := make([][]int, n+1)
	var root int

	for i := 1; i <= n; i++ {
		scanner.Scan()
		parents[i], _ = strconv.Atoi(scanner.Text())
		if parents[i] == -1 {
			root = i
		} else {
			children[parents[i]] = append(children[parents[i]], i)
		}
	}

	heights := make([]int, n+1)

	var dfs func(node int, height int)
	dfs = func(node int, height int) {
		heights[node] = height
		for _, child := range children[node] {
			dfs(child, height+1)
		}
	}

	dfs(root, 0)

	for i := 1; i <= n; i++ {
		fmt.Println(heights[i])
	}
}
