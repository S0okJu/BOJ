package main

import (
	"fmt"
	"sort"
)

func Bronze2997() {
	var numbers [3]int
	var frontDif int
	var backDif int

	fmt.Scanf("%d %d %d", &numbers[0], &numbers[1], &numbers[2])

	//sort
	sort.Ints(numbers[:])
	frontDif = numbers[1] - numbers[0]
	backDif = numbers[2] - numbers[1]

	if frontDif == backDif*2 {
		if numbers[1]+frontDif < 100 || numbers[1]+frontDif >= -100 {
			fmt.Printf("%d %d %d %d", numbers[0], numbers[1], numbers[1]+frontDif, numbers[2])
		}
		fmt.Printf("%d %d %d %d", numbers[0], numbers[1], numbers[1]+frontDif, numbers[2])
	} else if frontDif == backDif {
		fmt.Printf("%d %d %d %d", numbers[0], numbers[1], numbers[2], numbers[2]+backDif)
	} else if frontDif*2 == backDif {
		if numbers[0]+backDif < 100 || numbers[0]+backDif >= -100 {
			fmt.Printf("%d %d %d %d", numbers[0], numbers[0]+backDif, numbers[1], numbers[2])
		}
	}
}
