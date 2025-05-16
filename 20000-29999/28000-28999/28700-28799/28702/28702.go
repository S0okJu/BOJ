package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func isFizz(n int) bool {
	return n%3 == 0 && n%5 != 0
}

func isBuzz(n int) bool {
	return n%3 != 0 && n%5 == 0
}

func isFizzBuzz(n int) bool {
	return n%3 == 0 && n%5 == 0
}

func solution() {
	scanner := bufio.NewScanner(os.Stdin)
	strings := make([]string, 3)

	for i := 0; i < 3; i++ {
		scanner.Scan()
		strings[i] = scanner.Text()
	}

	last := strings[2]
	lastNum := -1

	if num, err := strconv.Atoi(last); err == nil {
		lastNum = num
	} else {
		for i := 1; i >= 0; i-- {
			if num, err := strconv.Atoi(strings[i]); err == nil {
				lastNum = num + (2 - i)
				break
			}
		}
	}

	next := lastNum + 1

	if isFizzBuzz(next) {
		fmt.Println("FizzBuzz")
	} else if isFizz(next) {
		fmt.Println("Fizz")
	} else if isBuzz(next) {
		fmt.Println("Buzz")
	} else {
		fmt.Println(next)
	}
}

func main() {
	solution()
}
