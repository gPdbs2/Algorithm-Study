import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

n = input().rstrip()
n_li = list(map(int, input().split()))
m = input().rstrip()
m_li = list(map(int, input().split()))

n_li.sort()

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

for i in range(len(m_li)):
    print(count_by_range(n_li, m_li[i], m_li[i]), end=' ')