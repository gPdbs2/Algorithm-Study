import sys
input = sys.stdin.readline

n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(d[i])):
        # 0열끼리 더하기
        if j == 0:
            d[i][j] = d[i][j] + d[i-1][j]
        # 마지막 열끼리 더하기
        elif j == len(d[i])-1:
            d[i][j] = d[i][j]+d[i-1][j-1]
        # 두 방향 중 위 층의 값과의 합이 더 큰 경우를 적용
        else:
            d[i][j] = max(d[i-1][j-1], d[i-1][j])+d[i][j]

# n ~ 1행에서의 최댓값 출력
print(max(d[n-1]))


# 걸린 시간 : 약 43분