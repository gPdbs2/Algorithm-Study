import sys
input = sys.stdin.readline

A, P = map(int, input().split())     # A: 수열 D의 인덱스 1에 있는 값, P: 각 자리 수를 곱한 횟수
check = [0]*236197                   # 배열 최댓값 설정 (최대 출력 값 : 9^5 + 9^5 + 9^5 + 9^5 = 236196)
cnt = 1

def next(A, P):
    A =str(A)
    ans = 0
    for i in A:
        ans += pow(int(i), P)
    return ans

def dfs(A, P, cnt, check):
    if check[A] != 0:
        return check[A]-1
    check[A] = cnt
    b = next(A, P)
    cnt += 1
    return dfs(b, P, cnt, check)

print(dfs(A, P, cnt, check))