import sys
from typing import List
from collections import deque
input = sys.stdin.readline

def solution(N: int, graph: List[List[int]], deletion: int, root: int) -> int:
    if deletion == root:
        return 0

    def delete_target(node):
        q = deque([node])
        while q:
            curr_node = q.popleft()
            for child in graph[curr_node]:
                q.append(child)
            graph[curr_node] = []
            for i in range(N):
                if curr_node in graph[i]:
                    graph[i].remove(curr_node)

    delete_target(deletion)

    def get_leaf_count(start_node):
        count = 0
        q = deque([start_node])
        while q:
            node = q.popleft()
            if len(graph[node]) == 0:
                count += 1
            else:
                for child in graph[node]:
                    q.append(child)
        return count

    return get_leaf_count(root)


if __name__ == '__main__':
    N = int(input())
    parents = list(map(int, input().split()))
    graph = [[] for _ in range(N)]
    root = -1

    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
        else:
            graph[parent].append(i)

    deletion_target = int(input())
    print(solution(N, graph, deletion_target, root))