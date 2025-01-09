package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func Silver15654() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n, m int
	fmt.Fscan(reader, &n, &m)

	nums := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &nums[i])
	}

	sort.Ints(nums)

	selected := make([]int, m)
	visited := make([]bool, n)

	var backtrack func(int)
	backtrack = func(idx int) {
		if idx == m {
			for i := 0; i < m; i++ {
				fmt.Fprintf(writer, "%d", selected[i])
				if i < m-1 {
					fmt.Fprint(writer, " ")
				}
			}
			fmt.Fprintln(writer)
			return
		}

		for i := 0; i < n; i++ {
			if visited[i] {
				continue
			}

			selected[idx] = nums[i]
			visited[i] = true
			backtrack(idx + 1)
			visited[i] = false
		}
	}

	backtrack(0)
}

func main() {
	Silver15654()
}
