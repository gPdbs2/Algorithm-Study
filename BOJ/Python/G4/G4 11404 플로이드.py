import sys
input = sys.stdin.readline
INF =int(1e9)

# n: 도시 갯수, m: 버스 갯수
n = int(input())
m = int(input())
# 모든 최단 거리 저장
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    # 연결 간선 갯수가 하나가 아닐 수 있음 => 최솟값 넣기
    graph[a][b] = min(c, graph[a][b])

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')

    print()


# 걸린 시간 : 약 76분