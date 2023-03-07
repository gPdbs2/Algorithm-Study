import sys
input = sys.stdin.readline
sys.setrecursionlimit(5000)

# n: 정점 갯수, m: 간선 갯수
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    u, v = map(int, input().split())
    # 무방향 처리
    graph[u]. append(v)
    graph[v].append(u)

# dfs 탐색
def dfs(start, depth):
    # 시작 노드 방문 처리
    visited[start] = True

    # 해당 시작점을 기준으로 dfs를 통해 그래프 탐색
    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth+1)

# 컴포넌트 갯수 저장할 변수
cnt = 0

# 1~n+1번 노드까지 각각 돌면서
for i in range(1, n+1):
    if not visited[i]:          # 만약 i번째 노드를 방문하지 않았다면
        if not graph[i]:        # 해당 정점이 연결된 그래프가 없다면
            cnt += 1            # 개수를 +1
            visited[i] = True   # 방문 처리
        else:           # 연결된 그래프가 있으면
            dfs(i, 0)   # dfs 탐색 돌기
            cnt += 1    # 개수를 +1

print(cnt)


# 걸린 시간 : 약 49분