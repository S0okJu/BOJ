package main

import (
	"fmt"
	"strings"
)

func main() {
	var inp string
	var result string

	fmt.Scan(&inp)
	result = convertCase(inp)
	fmt.Println(result)
}

func convertCase(words string) string {
	var result strings.Builder

	for _, word := range words {
		if 'a' <= word && word <= 'z' {
			result.WriteRune(word - 'a' + 'A')
		} else if 'A' <= word && word <= 'Z' {
			result.WriteRune(word - 'A' + 'a')
		} else {
			result.WriteRune(word)
		}
	}
	return result.String()
}
