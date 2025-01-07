package main

import (
	"bufio"
	"fmt"
	"os"
)

func Silver15652() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n, m int
	fmt.Fscan(reader, &n, &m)

	selected := make([]int, m)

	var backtrack func(int, int)
	backtrack = func(idx, start int) {
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

		// 순회
		for i := start; i <= n; i++ {
			selected[idx] = i
			backtrack(idx+1, i)
		}
	}

	backtrack(0, 1)
}

func main() {
	Silver15652()
}
