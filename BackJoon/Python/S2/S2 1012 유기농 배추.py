# 재귀 제한 설정
import sys
sys.setrecursionlimit(10000)

# 2
def dfs(x, y):
    # 상하좌우 설정
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    # 상하좌우 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m) and (0 <= ny < n):
            if graph[ny][nx] == 1:
                graph[ny][nx] = -1          # 배추 인접 시 체크
                dfs(nx, ny)

# 1
t = int(input())

for i in range(t):
    m, n, k = map(int, input().split())     # m: 가로, n: 세로, k: 개수
    graph = [[0]*m for _ in range(n)]
    cnt = 0

    # 행렬 생성, 배추 위치에 1 표시
    for j in range(k):
        X, Y = map(int, input().split())
        graph[Y][X] = 1

    # 3. 배추 세기
    for x in range(m):
        for y in range(n):
            if graph[y][x] == 1:
                dfs(x, y)
                cnt += 1

    print(cnt)

