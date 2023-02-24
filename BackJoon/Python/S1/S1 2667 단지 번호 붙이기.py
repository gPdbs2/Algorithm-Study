n = int(input())
graph = [list(map(int, input())) for _ in range(n)]     # 입력 받을 그래프 담을 리스트
num = []

# 상하좌우 이동 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# dfs 정의
def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        global count            # cnt를 사용하기 위해 global 선언
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False


count = 0
result = 0

# 정의된 dfs를 가지고 graph를 탐색 => 그래프의 원소가 1일 때만 방문 처리
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            num.append(count)
            result += 1
            count = 0

num.sort()                      # 오름차순 정렬
print(result)                   # 총 단지 수 출력
for i in range(len(num)):       # 각 단지마다 집의 수 출력
    print(num[i])

# 걸린 시간 : 약 60분