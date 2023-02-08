import sys
input = sys.stdin.readline

n = int(input())
RGB = []

for i in range(n):
    RGB.append(list(map(int, input().split())))

for i in range(1, n):
    # RGB[i][n] : i번 째 집을 n값에 해당하는 색(0=R, 1=G, 2=B)으로 칠했을 때의 최솟값
    RGB[i][0] = min(RGB[i-1][1], RGB[i-1][2])+RGB[i][0]    # 빨간 집
    RGB[i][1] = min(RGB[i-1][0], RGB[i-1][2])+RGB[i][1]    # 초록 집
    RGB[i][2] = min(RGB[i-1][0], RGB[i-1][1])+RGB[i][2]    # 파란 집

# 3개의 값 중 가장 최솟값 출력
print(min(RGB[n-1][0], RGB[n-1][1], RGB[n-1][2]))


# 걸린 시간 : 약 43분