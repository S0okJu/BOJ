package main

import (
	"bufio"
	"fmt"
	"os"
)

func Silver1543() {
	var document, word string
	scanner := bufio.NewScanner(os.Stdin)

	scanner.Scan()
	document = scanner.Text()

	scanner.Scan()
	word = scanner.Text()

	var cnt int = 0
	docLen := len(document)
	wordLen := len(word)

	for i := 0; i <= docLen-wordLen; {
		if document[i:i+wordLen] == word {
			cnt++
			i += wordLen
		} else {
			i++
		}
	}
	fmt.Println(cnt)
}
