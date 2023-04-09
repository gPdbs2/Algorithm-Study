import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
cnt = list(map(int, input().split()))

def op(op_num):
    global a, n, m
    # 1번 -> 상하반전
    if op_num == 1:
        temp = []
        for i in range(n):
            temp.append(a[n-1-i])
        a = temp
        del temp
        return
    # 2번 -> 좌우반전
    if op_num == 2:
        temp = []
        for i in range(n):
            temp.append(a[i][::-1])
        a = temp
        del temp
        return
    # 3번 -> 오른쪽으로 90도(시계방향)
    if op_num == 3:
        temp = [[] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                temp[i].append(a[n-1-j][i])
        a = temp
        del temp
        n = len(a)
        m = len(a[1])
        return
    # 4번 -> 왼쪽으로 90도(반시계방향)
    if op_num == 4:
        temp = [[] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                temp[i].append(a[j][m-1-i])
        a = temp
        del temp
        n = len(a)
        m = len(a[1])
        return
    # 5번 : 1->2, 2->3, 3->4, 4->1)
    if op_num == 5:
        temp = [[] for _ in range(n)]
        for i in range(n//2):
            for j in range(m//2):
                temp[i].append(a[n//2+i][j])             # 4->1
            for j in range(m//2):
                temp[i+n//2].append(a[n//2+i][m//2+j])   # 3->4
            for j in range(m//2):
                temp[i].append(a[i][j])                  # 1->2
            for j in range(m//2):
                temp[i+n//2].append(a[i][m//2+j])        # 2->3
        a = temp
        del temp
        return
    # 6번 : 1->4, 4->3, 3->2, 2->1
    if op_num == 6:
        temp = [[] for _ in range(n)]
        for i in range(n//2):
            for j in range(m//2):
                temp[i].append(a[i][j+m//2])             # 2->1
            for j in range(m//2):
                temp[i+n//2].append(a[i][j])             # 1->4
            for j in range(m//2):
                temp[i+n//2].append(a[i+n//2][j])        # 4->3
            for j in range(m//2):
                temp[i].append(a[i+n//2][m//2+j])        # 3->2
        a = temp
        del temp
        return

for i in range(r):
    op(cnt[i])
for i in range(len(a)):
    print(*a[i])


# 걸린 시간 : 약 107분