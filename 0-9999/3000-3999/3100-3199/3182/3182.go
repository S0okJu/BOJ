package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type Solution struct {
	N     int
	graph []int

	visited []bool
}

func NewSolution(N int, graph []int) *Solution {
	return &Solution{
		N:     N,
		graph: graph,
	}
}

func (s *Solution) init() {
	s.visited = make([]bool, s.N+1)
}

func (s *Solution) dfs(start int) int {

	s.init()

	stack := make([]int, s.N+1)
	stack = append(stack, start)

	cnt := 0
	for len(stack) > 0 {
		// stack pop
		curr := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		if !s.visited[curr] {
			s.visited[curr] = true
			cnt += 1
			stack = append(stack, s.graph[curr])
		}
	}
	return cnt
}

func (s *Solution) Solve() int {

	result := s.N + 1
	max_ := 0
	for i := 1; i <= s.N; i++ {
		cnt := s.dfs(i)

		if (max_ == cnt && result > i) || max_ < cnt {
			max_ = cnt
			result = i
		}
	}
	return result
}

func main() {

	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	N, _ := strconv.Atoi(scanner.Text())

	answer := make([]int, N+1)
	answer[0] = 0
	for i := 1; i <= N; i++ {
		scanner.Scan()
		num, _ := strconv.Atoi(scanner.Text())
		answer[i] = num
	}

	solution := NewSolution(N, answer)
	fmt.Println(solution.Solve())
}
