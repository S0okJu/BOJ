package main

import (
	"fmt"
	"math"
)

func Silver2670() {
	var N int
	fmt.Scanln(&N)

	arr := make([]float64, N)
	for i := 0; i < N; i++ {
		fmt.Scanln(&arr[i])
	}

	result := arr[0]
	for k := 1; k < N; k++ {
		arr[k] = math.Max(arr[k], arr[k]*arr[k-1])
		result = math.Max(arr[k], result)
	}

	fmt.Printf("%.3f", result)

}
