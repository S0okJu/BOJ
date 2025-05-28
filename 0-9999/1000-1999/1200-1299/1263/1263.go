package main

import (
	"fmt"
	"sort"
)

type Work struct {
	endTime    int
	turnaround int
}

type Works struct {
	works []Work
}

func (w Works) schedule() int {

	// 끝나는 시점 기준으로 내림차순 정렬
	sort.Slice(w.works, func(i, j int) bool {
		return w.works[i].endTime > w.works[j].endTime
	})

	currTime := w.works[0].endTime
	for _, w := range w.works {
		if currTime > w.endTime {
			currTime = w.endTime
		}

		currTime -= w.turnaround
		if currTime < 0 {
			return -1
		}
	}
	return currTime
}

func main() {

	var N int
	fmt.Scanf("%d", &N)

	var works Works
	for i := 0; i < N; i++ {

		var ti, si int
		fmt.Scanf("%d %d", &ti, &si)

		works.works = append(works.works, Work{endTime: si, turnaround: ti})
	}
	fmt.Println(works.schedule())
}
