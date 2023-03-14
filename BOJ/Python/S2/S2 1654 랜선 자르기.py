import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]
start, end = 1, max(lan)    # 이분탐색 처음과 끝 위치

# 적절한 랜선 길이 찾기
while start <= end:
    mid = (start+end)//2    # 중간점
    lines = 0               # 랜선 수
    for i in lan:
        lines += i//mid     # 분할된 랜선 수
    if lines >= n:          # 랜선의 갯수가 분기점
        start = mid+1
    else:
        end = mid-1

print(end)


# 걸린 시간 : 약 38분