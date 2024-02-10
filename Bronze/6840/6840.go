package main

import (
	"fmt"
	"sort"
)

func main() {
	var inputArray [3]int
	var inp int

	for i := 0; i < 3; i++ {
		fmt.Scanln(&inp)
		inputArray[i] = inp
	}
	sort.Ints(inputArray[:])
	fmt.Printf("%d", inputArray[1])
}
