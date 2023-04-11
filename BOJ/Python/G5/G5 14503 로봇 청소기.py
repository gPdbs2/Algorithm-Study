import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())  # 로봇 청소기 좌표 (r,c) & 보는 방향 (d)
dx = [-1, 0, 1, 0]                   # 북(-1, 0) / 동(0, 1) / 남(1, 0) / 서(0, -1)
dy = [0, 1, 0, -1]

# 로봇 청소기가 청소해야 할 지도
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0     # 청소한 칸의 갯수

def clean(x, y, d):
    global ans
    # 빈 칸이면 청소
    if a[x][y] == 0:
        a[x][y] = 2     # 방문 처리
        ans += 1        # 청소한 칸에 +1

    # 4방향 탐색
    for i in range(4):
        nd = (d+3)%4
        nx = x+dx[nd]
        ny = y+dy[nd]

        # 이동한 위치가 빈 곳이면 탐색
        if a[nx][ny] == 0:
            clean(nx, ny, nd)
            return
        # 현재 방향 변경
        d = nd

    # 4방향 모두 탐색한 경우
    # (현재 방향+2)를 4로 나눈 나머지가 후진
    nd = (d+2)%4
    nx = x+dx[nd]
    ny = y+dy[nd]

    # 이동 위치가 벽이면 리턴
    if a[nx][ny] == 1:
        return
    # 이동 위치가 벽이 아니면 탐색
    clean(nx, ny, d)

clean(x, y, d)
print(ans)


# 걸린 시간 : 약 97분