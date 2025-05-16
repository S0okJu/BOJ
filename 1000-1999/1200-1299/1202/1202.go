package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"sort"
)

type Jewel struct {
	Weight int
	Price  int
}

type MaxHeap []int

func (h MaxHeap) Len() int            { return len(h) }
func (h MaxHeap) Less(i, j int) bool  { return h[i] > h[j] } // MaxHeap
func (h MaxHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *MaxHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *MaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var N, K int
	fmt.Fscan(reader, &N, &K)

	jewels := make([]Jewel, N)
	for i := 0; i < N; i++ {
		fmt.Fscan(reader, &jewels[i].Weight, &jewels[i].Price)
	}

	sort.Slice(jewels, func(i, j int) bool {
		return jewels[i].Weight < jewels[j].Weight
	})

	bags := make([]int, K)
	for j := 0; j < K; j++ {
		fmt.Fscan(reader, &bags[j])
	}
	sort.Ints(bags)

	hq := &MaxHeap{}
	heap.Init(hq)
	answer := 0
	idx := 0

	for _, bag := range bags {
		for idx < N && jewels[idx].Weight <= bag {
			heap.Push(hq, jewels[idx].Price)
			idx++
		}

		if hq.Len() > 0 {
			answer += heap.Pop(hq).(int)
		}
	}

	fmt.Println(answer)
}
