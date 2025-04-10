package main

import (
	"bufio"
	"container/list"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Graph struct {
	root  int
	edges map[int]map[int]int
}

func NewGraph() *Graph {
	return &Graph{edges: make(map[int]map[int]int)}
}

func (g *Graph) AddRoot(root int) {
	g.root = root
}
func (g *Graph) AddEdge(parent, child int) {
	if g.edges[parent] == nil {
		g.edges[parent] = make(map[int]int)
	}
	g.edges[parent][child] = 1
}

func (g *Graph) delete(target int) {
	visited := make(map[int]bool)

	// 양방향 연결 리스트로 덱 구현
	q := list.New()
	q.PushBack(g.root)
	visited[g.root] = true

	// target 노드 기준 전부 제거
	delete(g.edges, target)

	// target 노드를 자식 리스트로 가지는 경우 모두 제거
	for q.Len() > 0 {
		// popleft
		element := q.Front()
		current := element.Value.(int)
		q.Remove(element)

		for neighbor := range g.edges[current] {
			// 빈 리스트로 반환
			if neighbor == target {
				// 제거하기
				delete(g.edges[current], neighbor)
				continue
			} else {
				if !visited[neighbor] {
					visited[neighbor] = true
					q.PushBack(neighbor)
				}
			}
		}

	}

}

func (g *Graph) search() int {
	visited := make(map[int]bool)

	// 양방향 연결 리스트로 덱 구현
	q := list.New()
	q.PushBack(g.root)

	leafCnt := 0
	for q.Len() > 0 {
		// popleft
		element := q.Front()
		current := element.Value.(int)
		q.Remove(element)

		if visited[current] {
			continue
		}
		visited[current] = true
		if child, exist := g.edges[current]; !exist || len(child) == 0 {
			leafCnt += 1
		} else {
			for neighbor := range child {
				if !visited[neighbor] {
					q.PushBack(neighbor)
				}
			}
		}
	}
	return leafCnt
}

func (g *Graph) Solution(target int) int {

	// 루트 노드를 제거한다면
	if target == g.root {
		return 0
	}
	// 나머지를 삭제한다.
	g.delete(target)

	// search leaf
	leafCnt := g.search()

	return leafCnt
}

func main() {
	// Input
	reader := bufio.NewReader(os.Stdin)

	line1, _ := reader.ReadString('\n')
	line1 = strings.TrimSpace(line1)
	N, _ := strconv.Atoi(line1)

	line2, _ := reader.ReadString('\n')
	line2 = strings.TrimSpace(line2)
	parentStings := strings.Fields(line2)

	graph := NewGraph()
	for i := 0; i < N; i++ {
		pStr := parentStings[i]
		parent, _ := strconv.Atoi(pStr)
		if parent == -1 {
			graph.AddRoot(i)
			continue
		}

		graph.AddEdge(parent, i)
	}

	line3, _ := reader.ReadString('\n')
	line3 = strings.TrimSpace(line3)
	target, _ := strconv.Atoi(line3)

	result := graph.Solution(target)
	fmt.Println(result)

}
