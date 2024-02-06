package main

import "fmt"

func main() {
	var name string
	var age int
	var weight int
	var role string

	for {
		fmt.Scanf("%s %d %d", &name, &age, &weight)
		if name == "#" && age == 0 && weight == 0 {
			break
		}
		if age > 17 || weight >= 80 {
			role = "Senior"
		} else {
			role = "Junior"
		}
		fmt.Printf("%s %s\n", name, role)
	}
}
