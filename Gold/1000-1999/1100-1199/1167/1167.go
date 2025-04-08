package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Edge struct {
	to     int
	weight int
}

func dfs(node int, graph [][]Edge, visited []bool, distance int) (int, int) {

	visited[node] = true
	maxDist := distance
	fastestNode := node

	for _, e := range graph[node] {
		if !visited[e.to] {
			d, node := dfs(e.to, graph, visited, e.weight+distance)
			if d > maxDist {
				maxDist = d
				fastestNode = node
			}
		}
	}

	return maxDist, fastestNode
}

func solution(n int, graph [][]Edge) int {
	// 임의의 한 점에서 가장 거리가 먼 지점을 찾는다.
	visited := make([]bool, n+1)
	_, farthest := dfs(1, graph, visited, 0)

	visited2 := make([]bool, n+1)
	maxDistance, _ := dfs(farthest, graph, visited2, 0)
	return maxDistance

}

func main() {
	reader := bufio.NewReader(os.Stdin)

	// 첫 줄: 노드 수
	line, _ := reader.ReadString('\n')
	n, _ := strconv.Atoi(strings.TrimSpace(line))

	graph := make([][]Edge, n+1)

	for i := 0; i < n; i++ {
		row, _ := reader.ReadString('\n')
		parts := strings.Fields(row)

		from, _ := strconv.Atoi(parts[0])

		for j := 1; j < len(parts); j += 2 {
			if parts[j] == "-1" {
				break
			}
			to, _ := strconv.Atoi(parts[j])
			weight, _ := strconv.Atoi(parts[j+1])
			graph[from] = append(graph[from], Edge{to, weight})
		}
	}

	fmt.Println(solution(n, graph))
}
