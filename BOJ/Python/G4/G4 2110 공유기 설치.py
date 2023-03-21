import sys
input = sys.stdin.readline

n, c = map(int, input().split())
# 집의 좌표 리스트 x 생성 후 정렬
x = [int(input().rstrip("\n")) for _ in range(n)]
x.sort()

# start: 최소 거리, end: 최대 거리
start, end = 1, x[-1]-x[0]

def binary(start, end):
    ans = 0
    while start <= end:
        mid = (start+end)//2
        current = x[0]
        # cnt : 공유기 설치 횟수
        cnt = 1

        for i in range(1, len(x)):
            if x[i] >= current+mid:
                current = x[i]
                cnt += 1
        # 주어진 공유기 갯수가 c개 이상이면 거리 넓힘
        if cnt >= c:
            start = mid+1
            ans = mid
        # c개 미만이면 거리 좁힘
        else:
            end = mid-1
    return ans

print(binary(start, end))


# 걸린 시간 : 약 83분