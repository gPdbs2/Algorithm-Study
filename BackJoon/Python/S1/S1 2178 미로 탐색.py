import sys
from collections import deque
input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
alist = [list(map(int, input().strip())) for _ in range(n)]

# 각 위치별로 방문 여부 확인
visited = [[False for _ in range(m)] for _ in range(n)]

# 상하좌우 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque([(x, y, 1)])
    visited[x][y] = True
    while q:
        x, y, distance = q.popleft()
        if x == n-1 and y == m-1:
            # 최종 경로 도착
            print(distance)
            break
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # nx, ny가 미로를 벗어났는지, (nx,ny) 좌표를 이미 방문했는지, 해당 좌표가 벽인지 확인
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and alist[nx][ny] == 1:
                    # 방문 처리
                    visited[nx][ny] = True
                    # 지금까지 이동한 값인 distance+1 넣기 - 시작점도 거리에 포함 => 초기값은 1
                    # 좌표가 (n-1, m-1)이 됐을 때 그 위치로 오기까지의 거리인 distance 출력
                    q.append((nx, ny, distance + 1))
bfs(0, 0)