package main

import "fmt"

func Silver13699() {
	var n int
	fmt.Scanf("%d", &n)

	t := make([]int, n+1)
	t[0] = 1

	for i := 1; i < n+1; i++ {
		for j := 0; j < i; j++ {
			t[i] += (t[j] * t[i-j-1])
		}
	}

	fmt.Println(t[n])
}
