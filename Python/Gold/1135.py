import sys 
input = sys.stdin.readline
n = int(input())
people = list(map(int, input().split()))

# 1. init
tree = [[] for _ in range(n+1)]
time = [0 for _ in range(n+1)]

# 2. Build tree 
for i in range(1,n):
    tree[people[i]].append(i)

# 3. DFS
def dfs(node):
    # 3.1. Go to leaf node and store the time 
    childs = []
    for j in tree[node]:
        dfs(j)
        childs.append(time[j])
    
    # 3.2. If it is not leaf node
    if childs:
        # Get max time 
        # 최적의 합을 구하기 위해 정렬 시도(오래 걸리는 친구부터)
        childs.sort(reverse=True)
        # 여기서 k는 소식을 듣는 순서
        time[node] = max(childs[k] + k + 1 for k in range(len(childs)))

dfs(0)
print(time[0])
    