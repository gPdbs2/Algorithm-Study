import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]
# 2-친구 사이이면 1, 아니면 0
friend = [[0]*n for _ in range(n)]

for c in range(n):
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            # 2-친구에 해당하는 경우
            if graph[a][b] == 'Y' or (graph[a][c] == 'Y' and graph[c][b] == 'Y'):
                friend[a][b] = 1

# 결과값 담을 변수
res = 0

for i in friend:
    res = max(res, sum(i))
print(res)


# 걸린 시간 : 약 43분