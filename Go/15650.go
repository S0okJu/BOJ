package main

import (
	"bufio"
	"fmt"
	"os"
)

func Silver15650() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n, m int
	fmt.Fscan(reader, &n, &m)

	// 선택한 숫자들을 저장할 배열
	selected := make([]int, m)
	// 숫자의 사용 여부를 체크할 배열
	used := make([]bool, n+1)

	var backtrack func(int, int)
	backtrack = func(idx, start int) {
		// m개를 모두 선택했으면 출력
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

		for i := start; i <= n; i++ {
			if !used[i] {
				selected[idx] = i
				used[i] = true
				backtrack(idx+1, i+1)
				used[i] = false
			}
		}
	}

	backtrack(0, 1)
}
