import sys
input = sys.stdin.readline

# com: 컴퓨터 갯수, pair = 네트워크 쌍 갯수
com = int(input())
pair = int(input())
graph = [[] for _ in range(com+1)]
visited = [0 for _ in range(com+1)]

for _ in range(pair):
    a, b = map(int, input().split())
    # 연결된 컴퓨터의 정보에서 언제 1이 등장할 지 모름
    graph[a].append(b)
    graph[b].append(a)

cnt = 0

# 재귀적 구현
def dfs(v):
    global cnt
    visited[v] = True
    cnt += 1
    for i in graph[v]:
        if visited[i]:
            continue
        dfs(i)

dfs(1)
print(cnt-1)

# 걸린 시간 : 약 44분