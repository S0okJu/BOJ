package main

import "fmt"

func Bronze27866() {
	var input string
	var inpNum int

	fmt.Scanf("%s", &input)
	fmt.Scanf("%d", &inpNum)

	fmt.Println(string(input[inpNum-1]))
}
