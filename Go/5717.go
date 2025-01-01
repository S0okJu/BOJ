package main

import "fmt"

func Bronze5717() {
	var male int
	var female int

	for {
		fmt.Scanf("%d %d", &male, &female)
		if male == 0 && female == 0 {
			break
		}
		fmt.Println(male + female)
	}
}
