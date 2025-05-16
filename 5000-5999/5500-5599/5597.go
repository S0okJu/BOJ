package main

import "fmt"

func Bronze5597() {
	var students [30]bool

	for i := 0; i < 28; i++ {
		var studentId int
		fmt.Scanln(&studentId)
		students[studentId-1] = true
	}
	for i := 0; i < 30; i++ {
		if students[i] != true {
			fmt.Println(i + 1)
		}
	}
}
