package main

import (
	"bufio"
	"fmt"
	"os"
)

func Gold2171() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n int
	fmt.Fscan(reader, &n)

	xToY := make(map[int]map[int]bool)

	xCoords := make([]int, 0)

	for i := 0; i < n; i++ {
		var x, y int
		fmt.Fscan(reader, &x, &y)

		// x 좌표에 대한 맴이 없으면 생성
		if _, exists := xToY[x]; !exists {
			xToY[x] = make(map[int]bool)
			xCoords = append(xCoords, x)
		}
		xToY[x][y] = true // (x, y) 존재 표시
	}

	count := 0

	for i := 0; i < len(xCoords); i++ {
		x1 := xCoords[i]
		for j := i + 1; j < len(xCoords); j++ {
			x2 := xCoords[j]

			yPoints := make(map[int]bool)

			for y := range xToY[x1] {
				if xToY[x2][y] {
					yPoints[y] = true
				}
			}

			if len(yPoints) >= 2 {
				// 조합 공식 활용 (n * (n-1))/2
				count += (len(yPoints) * (len(yPoints) - 1)) / 2
			}
		}
	}

	fmt.Fprintln(writer, count)
}
