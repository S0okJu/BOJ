package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type Counter struct {
	zero []int
	one  []int
}

func NewCounter() *Counter {
	return &Counter{
		zero: make([]int, 41),
		one:  make([]int, 41),
	}
}

func (c *Counter) count() {
	c.zero[0] = 1
	c.one[0] = 0

	c.zero[1] = 0
	c.one[1] = 1

	for i := 2; i <= 40; i++ {
		c.zero[i] = c.zero[i-1] + c.zero[i-2]
		c.one[i] = c.one[i-1] + c.one[i-2]
	}
}

func (c *Counter) print(n int) {
	fmt.Printf("%d %d\n", c.zero[n], c.one[n])
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	var T int
	scanner.Scan()
	T, _ = strconv.Atoi(scanner.Text())

	counter := NewCounter()
	counter.count()

	for i := 0; i < T; i++ {
		scanner.Scan()
		t, _ := strconv.Atoi(scanner.Text())

		counter.print(t)
	}

}
