import sys
input = sys.stdin.readline

def binary(array, target):
    start = 0
    end = len(array)-1
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return 0

t = int(input())
for _ in range(t):
    n = int(input())
    n_li = list(map(int, input().split()))   # 수첩 1
    m = int(input())
    m_li = list(map(int, input().split()))   # 수첩 2

    n_li = list(set(n_li))                   # 중복 요소 제거
    n_li.sort()

    for i in m_li:
        print(n_li, i)


# 걸린 시간 : 약 하루 + 1시간