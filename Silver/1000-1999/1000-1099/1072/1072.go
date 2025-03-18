package main

import "fmt"

func Silver1072() {
	var x, y int
	fmt.Scan(&x, &y)

	result := 0
	// z := (y / x) * 100
	z := (y * 100) / x // 이렇게 해야 소수점이 버려지지 않음

	if z >= 99 || x == y {
		fmt.Println(-1)
		return
	}

	left, right := 0, 1000000000
	for left <= right {
		mid := (left + right) / 2
		curr_z := ((y + mid) * 100) / (x + mid)

		if z < curr_z {
			right = mid - 1
			result = mid
		} else {
			left = mid + 1
		}
	}

	fmt.Println(result)
}
