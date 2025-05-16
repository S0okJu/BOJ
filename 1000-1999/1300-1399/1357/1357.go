package main

import (
	"fmt"
	"strconv"
)

func reverseSwapRunes(s string) int {
	chars := []rune(s)
	for i, j := 0, len(chars)-1; i < j; i, j = i+1, j-1 {
		chars[i], chars[j] = chars[j], chars[i]
	}
	convStr := string(chars)

	convInt, _ := strconv.Atoi(convStr)
	return convInt
}

func Bronze1357() {
	var a, b string
	fmt.Scanln(&a, &b)

	revA := reverseSwapRunes(a)
	revB := reverseSwapRunes(b)
	res := reverseSwapRunes(strconv.Itoa(revA + revB))

	fmt.Println(res)
}
