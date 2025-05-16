package main

import (
	"math"
)

func Bronze2033(N int) int {
	if N < 10 {
		return N
	}

	magnitude := 10
	for magnitude <= N {
		// 반올림하여 N을 업데이트
		N = int(math.Round(float64(N)/float64(magnitude))) * magnitude
		magnitude *= 10
	}

	return N
}

//func main() {
//	var N int
//	fmt.Scan(&N)
//	result := roundNumber(N)
//	fmt.Println(result)
//}
