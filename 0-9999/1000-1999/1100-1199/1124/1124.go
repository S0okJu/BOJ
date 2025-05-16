package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func primeFactors(n int) []int {
	factors := []int{}

	for n%2 == 0 {
		factors = append(factors, 2)
		n = n / 2
	}

	for i := 3; i*i <= n; i += 2 {
		for n%i == 0 {
			factors = append(factors, i)
			n = n / i
		}
	}

	if n > 2 {
		factors = append(factors, n)
	}

	return factors
}

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	if n == 2 {
		return true
	}
	if n%2 == 0 {
		return false
	}

	for i := 3; i*i <= n; i += 2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func Silver1124() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	input := scanner.Text()

	nums := strings.Split(input, " ")
	a, _ := strconv.Atoi(nums[0])
	b, _ := strconv.Atoi(nums[1])

	count := 0
	for i := a; i <= b; i++ {
		f := primeFactors(i)
		isUnderPrime := isPrime(len(f))
		if isUnderPrime {
			count += 1
		}
	}
	fmt.Println(count)
}
