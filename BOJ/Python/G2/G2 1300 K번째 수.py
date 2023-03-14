import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
start, end = 1, k

while start <= end:
    mid = (start+end)//2
    idx = 0
    for i in range(1, n+1):
        # mid 이하의 i의 배수 or 최대 n
        idx += min(mid//i, n)
    if idx >= k:
        ans = mid
        end = mid-1
    else:
        start = mid+1

print(ans)

# 걸린 시간 : 약 57분