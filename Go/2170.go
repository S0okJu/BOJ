package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type Line struct {
	start int
	end   int
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	var n int
	fmt.Scanln(&n)

	lines := make([]Line, n)
	for i := 0; i < n; i++ {
		// 공백과 개행문자 제거
		line, _ := reader.ReadString('\n')
		line = strings.TrimSpace(line)
		nums := strings.Split(line, " ")
		start, _ := strconv.Atoi(nums[0])
		end, _ := strconv.Atoi(nums[1])
		lines[i] = Line{start, end}
	}

	// 시작점을 기준으로 정렬
	// Quick Sort 기반으로 정렬
	sort.Slice(lines, func(i, j int) bool {
		return lines[i].start < lines[j].start
	})

	total := 0
	currStart := lines[0].start
	currEnd := lines[0].end

	for i := 1; i < n; i++ {
		// 선들이 겹치면
		if lines[i].start <= currEnd {
			// 합친다
			if lines[i].end > currEnd {
				currEnd = lines[i].end
			}
		} else { // 선들이 겹치지 않으면
			// 힙친 선들의 길이를 구한다
			total += (currEnd - currStart)

			// 합친 선들로 값을 업데이트
			currStart = lines[i].start
			currEnd = lines[i].end
		}
	}

	// 마지막 선에 대한 길이를 구한다.
	total += (currEnd - currStart)
	fmt.Println(total)
}
