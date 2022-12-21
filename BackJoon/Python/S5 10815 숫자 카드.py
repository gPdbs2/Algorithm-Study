# 정답 1 (이진 탐색 (재귀))
import sys
input = sys.stdin.readline

# 1. 입력 선언
n = int(input())
n_li = list(map(int, input().split()))
m = int(input())
m_li = list(map(int, input().split()))

n_li.sort()

# 2. 이진 탐색 (재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

for i in range(m):
    if binary_search(n_li, m_li[i], 0, n-1) is not None:
        print('1', end=' ')
    else:
        print('0', end=' ')

# 걸린 시간 : 약 65분


# 정답 2 (set() 사용)
import sys
input = sys.stdin.readline

n = int(input())                        # 상근이가 가지고 있는 카드 수
n_li = set(map(int, input().split()))   # 같은 수가 들어와 중복될 경우, 순차탐색은 시간초과가 날 수 있으므로 중복 제거
m = int(input())                        # 주어지는 정수 갯수
m_li = list(map(int, input().split()))

for i in range(m):
    if (m_li[i] in n_li):
        print('1', end=' ')
    else:
        print('0', end=' ')