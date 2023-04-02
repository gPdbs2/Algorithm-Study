import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input()) for _ in range(n)]
ans = 0

def check(arr):
    n = len(arr)
    ans = 1

    for i in range(n):
        # 열 순회하며 연속된 숫자 세기
        cnt = 1
        for j in range(1, n):
            # 이전 것과 같으면 cnt에 1 추가
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            # 이전과 다르면 다시 1로 초기화
            else:
                cnt = 1
            # 비교 후 현재 cnt가 더 크면 ans 갱신
            if cnt > ans:
                ans = cnt

        # 행 순회하며 연속된 숫자 세기
        cnt = 1
        for j in range(1, n):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > ans:
                ans = cnt

    return ans

for i in range(n):
    for j in range(n):
        # 열 바꾸기
        if j+1 < n:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            # check : arr에서 인접한 것과 바꿨을 때 가장 긴 연속된 부분을 찾는 함수
            temp = check(arr)

            if temp > ans:
                ans = temp

            # 바꿨던 것들 다시 원상복구
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

        # 행 바꾸기
        if i+1 < n:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            temp = check(arr)
            if temp > ans:
                ans = temp

            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

print(ans)


# 걸린 시간 : 약 88분