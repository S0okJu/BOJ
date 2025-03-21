package main

import (
	"bufio"
	"fmt"
	"os"
)

func solution(n int) int {
	if n == 1 {
		return 1
	} else if n == 2 {
		return 2
	} else if n == 3 {
		return 4
	} else {
		return solution(n-1) + solution(n-2) + solution(n-3)
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var T int
	fmt.Fscan(reader, &T)

	for i := 0; i < T; i++ {
		var num int
		fmt.Fscan(reader, &num)
		result := solution(num)
		fmt.Println(result)
	}

}
