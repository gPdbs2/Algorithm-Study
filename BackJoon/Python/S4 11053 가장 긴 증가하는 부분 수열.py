import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
d = [0 for i in range(n)]                # dp에 자신을 포함해 만들 수 있는 부분 배열의 크기 지정

for i in range(n):
    for j in range(i):
        if a[i] > a[j] and d[i] < d[j]:  # 현재 있는 위치(i)의 원소가 이전에 있는 위치(j)의 원소보다 큰지 확인
            d[i] = d[j]                  # (단, d[i]가 d[j]보다 작을 경우에만 적용)
    d[i] += 1                            # 클 경우 d 값에 +1

print(max(d))                            # 마지막에 d에 있는 값 중 최댓값 출력

# 걸린 시간 : 약 63분