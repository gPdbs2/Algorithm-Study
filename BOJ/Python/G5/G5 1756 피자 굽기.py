import sys
input = sys.stdin.readline

d, n = map(int, input().split())
oven = list(map(int, input().split()))
doughs = list(map(int, input().split()))

# 이분 탐색을 위해 입력값 변경
# 현재 지름이 이전 지름보다 크면 변경
# ex. [5 6 4 3 6 2 3] => [5 5 4 3 3 2 2]
for i in range(1, len(oven)):
    if oven[i] > oven[i - 1]:
        oven[i] = oven[i - 1]

# 도우가 쌓이는 위치
piled_loc = 0
lp, rp = 0, len(oven) - 1
for dough in doughs:
    # False로 남으면 도우를 더이상 못 쌓음
    is_piled = False

    while lp <= rp:
        mid = (lp+rp)//2
        diameter = oven[mid]
        if diameter >= dough:
            lp = mid+1
            piled_loc = mid
            is_piled = True
        else:
            rp = mid-1

    if not is_piled:
        piled_loc = -1
        break

    lp = 0
    # 도우가 쌓이면 rp값 갱신
    rp = piled_loc-1

if piled_loc == -1:
    print(0)
else:
    print(piled_loc+1)

# 걸린 시간 : 약 86분