package main

import (
	"bufio"
	"container/list"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var (
	n, m    int
	grid    [][]int
	visited [][]bool
	dx      = []int{-1, -1, -1, 0, 0, 1, 1, 1}
	dy      = []int{-1, 0, 1, 1, -1, -1, 0, 1}
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	scanner.Scan()
	splitLine := strings.Fields(scanner.Text())
	n, _ = strconv.Atoi(splitLine[0])
	m, _ = strconv.Atoi(splitLine[1])

	grid = make([][]int, n)
	visited = make([][]bool, n)

	for i := 0; i < n; i++ {
		scanner.Scan()
		values := strings.Fields(scanner.Text())
		grid[i] = make([]int, m)
		visited[i] = make([]bool, m)

		for j := 0; j < m; j++ {
			grid[i][j], _ = strconv.Atoi(values[j])
		}
	}

	peakCount := 0
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if !visited[i][j] {
				peakCount += bfs(i, j)
			}
		}
	}

	fmt.Println(peakCount)
}

func bfs(x, y int) int {
	queue := list.New()
	queue.PushBack([2]int{x, y})
	visited[x][y] = true

	isPeak := true
	height := grid[x][y]

	for queue.Len() > 0 {
		element := queue.Front()
		queue.Remove(element)
		curr := element.Value.([2]int)
		currX, currY := curr[0], curr[1]

		for i := 0; i < 8; i++ {
			nx, ny := currX+dx[i], currY+dy[i]

			if nx >= 0 && ny >= 0 && nx < n && ny < m {
				if grid[nx][ny] > height {
					isPeak = false
				} else if grid[nx][ny] == height && !visited[nx][ny] {
					visited[nx][ny] = true
					queue.PushBack([2]int{nx, ny})
				}
			}
		}
	}

	if isPeak {
		return 1
	}
	return 0
}
