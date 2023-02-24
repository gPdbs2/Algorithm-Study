import sys
input = sys.stdin.readline

# 이진 탐색 라이브러리 사용(Bisect)
from bisect import bisect_left, bisect_right

# n, n_li: 상근이가 갖고 있는 카드 갯수와 리스트
# m, m_li: 주어진 카드 갯수와 리스트
n = input().rstrip()
n_li = list(map(int, input().split()))
m = input().rstrip()
m_li = list(map(int, input().split()))

n_li.sort()

# 이진 탐색
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

for i in range(len(m_li)):
    print(count_by_range(n_li, m_li[i], m_li[i]), end=' ')


# 걸린 시간 : 약 87분