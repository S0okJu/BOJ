package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func solutions() {
	scanner := bufio.NewScanner(os.Stdin)

	// 테스트 케이스 개수 입력
	scanner.Scan()
	T, _ := strconv.Atoi(scanner.Text())

	for i := 0; i < T; i++ {
		// 동전 종류 개수 입력
		scanner.Scan()
		N, _ := strconv.Atoi(scanner.Text())

		// 동전 종류 입력
		scanner.Scan()
		words := strings.Fields(scanner.Text())
		coinTypes := make([]int, N)
		for idx, w := range words {
			coinT, _ := strconv.Atoi(w)
			coinTypes[idx] = coinT
		}

		// 목표 금액 입력
		scanner.Scan()
		finalAmount, _ := strconv.Atoi(scanner.Text())

		// 동전 조합 경우의 수 계산
		cases := make([]int, finalAmount+1)
		cases[0] = 1

		for _, coinType := range coinTypes {
			for k := coinType; k <= finalAmount; k++ {
				cases[k] += cases[k-coinType]
			}
		}

		// 결과 출력
		fmt.Println(cases[finalAmount])
	}
}

func main() {
	solutions()
}
