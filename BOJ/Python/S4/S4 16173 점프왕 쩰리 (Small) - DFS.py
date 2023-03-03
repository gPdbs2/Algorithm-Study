import sys
input = sys.stdin.readline

# 입력 선언
n = int(input())                                             # 게임 구역의 크기
graph = [list(map(int, input().split())) for _ in range(n)]  # 게임 판의 구역
visited = [[0]*n for _ in range(n)]                          # 방문 여부 저장할 리스트

# 이동 설정 (하, 우)
dx = [0,1]
dy = [1,0]

# dfs 정의
def dfs(x, y, visited):
    # 영역을 벗어나면 return
    if x < 0 or x>= n or y < 0 or y >= n:
        return False

    # 방문 처리
    if visited[y][x] == 1:
        return False

    # 방문한 지점의 수가 -1 이라면 HaruHaru 출력 후 종료
    if graph[y][x] == -1:
        print("HaruHaru")
        exit()

    # 방문 표시
    visited[y][x] = 1

    # 아래, 우측 탐색
    for i in range(2):
        # 요소 수만큼 점프해서 방문
        nx = x+dx[i]*graph[y][x]
        ny = y+dy[i]*graph[y][x]
        dfs(nx, ny, visited)
    return True

if dfs(0, 0, visited) == 1:
    print("Hing")


# 걸린 시간 : 68분