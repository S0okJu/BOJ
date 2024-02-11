package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var number int
	var sentences []string

	// Scanner
	scanner := bufio.NewScanner(os.Stdin)

	fmt.Scanf("%d", &number)

	// sentences init
	sentences = make([]string, number)
	for i := 0; i < number; i++ {
		scanner.Scan()
		sentences[i] = scanner.Text()
	}

	for j := 0; j < number; j++ {
		fmt.Printf("%d. %s\n", j+1, sentences[j])
	}
}
