from collections import deque
import sys
input = sys.stdin.readline

#
m, n, k = map(int, input().split())
# M × N 크기의 2차원 배열 생성
graph = [[0] * n for i in range(m)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 모눈종이 색칠하기
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    # 입력받는 좌표대로 배열의 영역을 1로 칠해주기
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

# 모눈종이 전체 BFS 탐색
# 0,0 부터 M,N 좌표까지 탐색하며 0인 부분에 대해 BFS 탐색 진행
def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 1
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 모눈종이의 범위를 벗어나면 무시
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            # 방문하지 않은 좌표는 방문 처리 후 큐에 삽입
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny))
                cnt += 1
    return cnt

res = []

#
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            res.append(bfs(graph, i, j))

print(len(res))
res.sort()
for i in res:
    print(i, end=' ')


# 걸린 시간 : 약 77분