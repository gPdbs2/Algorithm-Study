import sys
input = sys.stdin.readline

def dfs(dep, i):
    if dep == 6:
        print(*res)
        return
    # for문 i : 만약 숫자 배열이 1 ~ 7까지 있다고 할 때 숫자를 골라주는 역할
    for i in range(i, k):   # 정답 배열에 넣으려는 인덱스 더했을 경우
        if dep+k-i < 6:     # 남은 요소들을 다 채워도 최종 길이를 만족하지 못한다면
            return          # 해당 재귀문 종료
        res.append(s[i])    # 최종 길이를 만족할 수 있을 경우에만 append
        dfs(dep+1, i+1)     # 재귀
        res.pop()           # 다음 요소 탐색을 위해 pop

while True:
    lotto = list(map(int, input().split()))
    k = lotto[0]
    s = lotto[1:]

    if k == 0:
        break

    res = []
    dfs(0, 0)
    print()

# 걸린 시간 : 98분