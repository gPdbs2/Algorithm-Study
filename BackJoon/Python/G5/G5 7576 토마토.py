from collections import deque

m, n = map(int, input().split())
# 토마토 받아서 넣을 2차원 리스트
box = [list(map(int, input().split())) for _ in range(n)]
# 좌표를 넣을 큐
queue = deque([])

# 상하좌우 설정
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 정답 담을 변수
res = 0

# queue에 처음에 받은 토마토의 위치 좌표 append
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i,j])

def bfs():
    while queue:
        # 처음 토마토 좌표 x, y에 꺼내기
        x, y = queue.popleft()
        # 상하좌우 설정
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 해당 좌표가 좌표 크기를 넘어가지 않고, 그 좌표에 토마토가 익지 않은 상태(0)여야 함
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                # 익히고 1 더해주면서 횟수 세기
                # 여기서 나온 최댓값이 정답
                box[nx][ny] = box[x][y] +1
                queue.append([nx, ny])

bfs()
for i in box:
    for j in i:
        # 다 탐색했는데 토마토 익히지 못했으면 -1 출력
        if j == 0:
            print(-1)
            exit(0)
    # 다 익혔으면 최댓값이 정답
    res = max(res, max(i))
# 처음을 1로 시작했으니 1 빼줌
print(res-1)