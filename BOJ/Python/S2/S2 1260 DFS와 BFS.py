import sys
from collections import deque
input = sys.stdin.readline

# n: 노드 갯수, m: 간선 갯수, v: 시작 노드 번호
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 탐색
def dfs(start):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

# BFS 탐색
def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

# 오름차순 정렬
for i in graph:
    i.sort()

# DFS
visited = [False]*(N+1)
dfs(V)
print()

# BFS
visited = [False]*(N+1)
bfs(V)


# 걸린 시간 : 약 46분