package main

import "fmt"

func main() {
	sum := 0
	for i := 0; i < 5; i++ {
		var a int
		fmt.Scanf("%d", &a)
		sum += a
	}

	fmt.Println(sum)
}
