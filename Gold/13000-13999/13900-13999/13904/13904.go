package main

import (
	"container/heap"
	"fmt"
)

type Task struct {
	weight   int
	deadline int
}

type MaxHeap []Task

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i].weight > h[j].weight }
func (h MaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *MaxHeap) Push(x interface{}) {
	*h = append(*h, x.(Task))
}
func (h *MaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func main() {
	var n int
	fmt.Scan(&n)

	hq := &MaxHeap{}
	heap.Init(hq)
	maxDay := 0

	for i := 0; i < n; i++ {
		var d, w int
		fmt.Scan(&d, &w)
		heap.Push(hq, Task{weight: w, deadline: d})
		if maxDay < d {
			maxDay = d
		}
	}

	assigned := make([]bool, maxDay+1)
	score := 0

	for hq.Len() > 0 {
		task := heap.Pop(hq).(Task)

		for i := task.deadline; i > 0; i-- {
			if !assigned[i] {
				assigned[i] = true
				score += task.weight
				break
			}
		}
	}
	fmt.Println(score)
}
