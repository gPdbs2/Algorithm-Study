import sys
input = sys.stdin.readline

n = int(input())
p = [0] +list(map(int, input().split()))
# 인덱스 0부터 하면 헷갈리므로 dp[0]은 0으로 채운 후 1부터 시작
dp = [0 for _ in range(n+1)]

# dp[1] = p[1] = 3
# dp[2] = dp[1]+p[1], p[2] 중 큰 값 = 8
# dp[3] = dp[1]+p[2], dp[2]+p[1], p[3] 중 큰 값 = 15
# dp[4] = dp[1]+p[3], dp[2]+p[2], dp[3]+p[1], p[4] 중 큰 값 = 18
for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j]+p[j])

print(dp[i])


# 걸린 시간 : 약 43분