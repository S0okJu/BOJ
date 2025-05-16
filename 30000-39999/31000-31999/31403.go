package main

import (
	"fmt"
	"strconv"
)

func Bronze31403() {
	var num []int = make([]int, 3)

	for i := 0; i < 3; i++ {
		fmt.Scanln(&num[i])
	}
	// 1. If num is int
	fmt.Println(num[0] + num[1] - num[2])

	// 2. If num is string
	var cat string
	cat = strconv.Itoa(num[0]) + strconv.Itoa(num[1])
	numCat, _ := strconv.Atoi(cat)
	fmt.Println(numCat - num[2])
}
