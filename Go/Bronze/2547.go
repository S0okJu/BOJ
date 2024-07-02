package main

import (
	"fmt"
	"math/big"
)

func Bronze2547() {
	var T int
	fmt.Scanln(&T)

	for i := 0; i < T; i++ {
		fmt.Scanln()

		var N int
		fmt.Scanln(&N)

		sum := big.NewInt(0)
		for j := 0; j < N; j++ {
			var temp int64
			fmt.Scanln(&temp)
			sum = sum.Add(sum, big.NewInt(temp))
		}

		if sum.Div(sum, big.NewInt(int64(N))) == big.NewInt(0) {
			fmt.Println("YES")
		} else {
			fmt.Println("NO")
		}
	}
}

func main() {
	Bronze2547()
}
