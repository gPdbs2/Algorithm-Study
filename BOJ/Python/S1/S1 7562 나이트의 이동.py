from collections import deque
import sys
input = sys.stdin.readline

t = int(input().rstrip())

# BFS 탐색
def bfs():
    # dx, dy : 나이트의 이동 좌표(문제 그림)
    dx = [-1, 1, 2, 2, 1, -1, -2, -2]
    dy = [2, 2, 1, -1, -2, -2, -1, 1]
    q = deque()
    q.append((bx, by))

    while q:
        x, y = q.popleft()
        # 목적지 좌표가 나오면 그 값에서 -1한 값 리턴 (1부터 시작했으므로)
        if x == ex and y == ey:
            return matrix[x][y] -1
        # 상하좌우 & 대각선 탐색
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]

            # 이동할 때마다 이전 좌표 값에 +1해줌
            if 0 <= nx < l and 0 <= ny < l and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] +1
                q.append((nx, ny))

# 테스트 케이스 수만큼 반복
for _ in range(t):
    l = int(input().rstrip())                      # 체스판 한 변의 길이
    bx, by = map(int, input().rstrip().split())    # 현재 있는 칸
    ex, ey = map(int, input().rstrip().split())    # 이동하려고 하는 칸
    matrix = [[0]* l for _ in range(l)]            # 체스판의 크기
    matrix[bx][by] = 1

    print(bfs())

# 걸린 시간 : 약 69분