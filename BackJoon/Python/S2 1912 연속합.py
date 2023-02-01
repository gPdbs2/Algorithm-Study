import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 1번부터 n번까지 리스트 새로 초기화
for i in range(1, n):
    # max 함수 활용
    # 해당 인덱스에 있는 값과 이전 인덱스에 있는 값+현재 인덱스에 있는 값 비교
    # 더 큰 수를 해당 인덱스에 저장
    arr[i] = max(arr[i], arr[i-1]+arr[i])

# 각 인덱스에 새로 저장된 값들을 비교하여 최댓값 출력
print(max(arr))

# 걸린 시간 : 약 71분