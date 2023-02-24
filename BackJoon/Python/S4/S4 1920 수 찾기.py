import sys
input = sys.stdin.readline

n = input()
n_li = sorted(map(int, input().split()))    # 이분 탐색을 위해 N 정수 리스트 정렬
m = input()
m_li = map(int, input().split())

# 이분 탐색
def binary(l, n_li, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    # 중간 지점의 값과 리스트 요소 비교
    # 1. 같으면 1 반환
    if l == n_li[m]:
        return 1
    # 2. 중간 값보다 찾는 값이 작으면 중간보다 작은 부분에서 탐색
    elif l < n_li[m]:
        return binary(l, n_li, start, m-1)
    # 3. 중간 값보다 찾는 값이 크면 중간보다 윗 부분에서 탐색
    else:
        return binary(l, n_li, m+1, end)


for l in m_li:
    start = 0
    end = len(n_li)-1
    print(binary(l,n_li,start,end))

# 걸린 시간 : 약 72분