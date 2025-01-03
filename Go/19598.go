package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type Meeting struct {
	start int
	end   int
}

func Gold19598() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	fmt.Scanln(&n)

	meetings := make([]Meeting, n)

	// 회의 정보 입력 받기
	for i := 0; i < n; i++ {
		line, _ := reader.ReadString('\n')
		line = strings.TrimSpace(line)
		times := strings.Split(line, " ")
		start, _ := strconv.Atoi(times[0])
		end, _ := strconv.Atoi(times[1])
		meetings[i] = Meeting{start, end}
	}

	// 시작점을 기준으로 정렬하기
	sort.Slice(meetings, func(i, j int) bool {
		return meetings[i].start < meetings[j].start
	})

	// 끝나는 시간과 관련된 배열
	endTimes := []int{meetings[0].end}
	maxRooms := 1

	for i := 1; i < n; i++ {
		// Heap의 POP 부분이라고 보면 된다.
		// 겹친다 = 회의실을 사용할 수 없다.
		for len(endTimes) > 0 && endTimes[0] <= meetings[i].start {
			endTimes = endTimes[1:]

		}

		// 힙의 삽입을 생각하면 된다.
		insertIdx := sort.SearchInts(endTimes, meetings[i].end)
		endTimes = append(endTimes, 0)
		copy(endTimes[insertIdx+1:], endTimes[insertIdx:])
		endTimes[insertIdx] = meetings[i].end

		// endTIme의 길이가 방의 크기라고 보면 된다.
		if len(endTimes) > maxRooms {
			maxRooms = len(endTimes)
		}
	}

	fmt.Println(maxRooms)
}
