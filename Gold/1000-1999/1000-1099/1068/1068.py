import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
parent_info = list(map(int,input().split()))
Removed = int(input())

# 부모당 자식들 정보  
tree = [[] for _ in range(N)]
alive = [ True for _ in range(N)]
root = 0

for i in range(N):
    if parent_info[i] != -1:
        tree[parent_info[i]].append(i)
    else:
        root = i

def BFS(p):
    queue = deque([p])
    visited = [ False for _ in range(N)]
    # 초기화 
    visited[p] = True
    alive[p] = False

    while queue:
        p = queue.popleft()

        for c in tree[p]:
            queue.append(c)
            visited[c] = True
            alive[c] = False

def solution(removed_node):
    cnt = 0 
    alive[removed_node] = False

    if removed_node == root:
        return 0
    # leaf 노드 삭제할 경우 
    elif len(tree[removed_node]) == 0:
        parent_index = 0
        for i, parent in enumerate(tree):
            for child in parent:
                if child == removed_node:
                    parent_index = i 
        tree[parent_index].remove(removed_node)
    else:
        for child in tree[removed_node]:
            BFS(child)
    
    for i in range(N):
        if alive[i] and len(tree[i]) == 0:
            cnt += 1
    return cnt 

print(solution(Removed))