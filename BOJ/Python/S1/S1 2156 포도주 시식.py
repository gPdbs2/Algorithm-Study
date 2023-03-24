import sys
input = sys.stdin.readline

n = int(input())
w = [int(input()) for _ in range(n)]

dp = [0]*n
dp[0] = w[0]

# 현재 & 이전, 전전 X  =>  w[i] + w[i-1] + dp[i-3]
# 현재 $ 전전, 이전 X  =>  w[i] + dp[i-2]
# 현재 안 마심  =>  dp[i-1]
if n > 1:
    dp[1] = w[0]+w[1]
if n > 2:
    dp[2] = max(w[2]+w[1], w[2]+w[0], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i-3]+w[i-1]+w[i], dp[i-2]+w[i], dp[i-1])

print(dp[n-1])


# 걸린 시간 : 약 74분