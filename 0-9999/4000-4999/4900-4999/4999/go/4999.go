package main

import (
	"fmt"
)

func main() {
	var jae string
	fmt.Scanln(&jae)
	a_jae := jae[:len(jae)-1]

	var doctor string
	fmt.Scanln(&doctor)
	a_doctor := doctor[:len(doctor)-1]

	if len(a_jae) >= len(a_doctor) {
		fmt.Println("go")
	} else {
		fmt.Println("no")
	}

}
