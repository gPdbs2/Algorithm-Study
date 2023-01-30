# BottomUp 방식 (for문 활용)
import sys
input = sys.stdin.readline

x = int(input())

d = [0]*(x+1)                       # 1-based

for i in range(2, x+1):             # 2부터 x까지 반복
    d[i] = d[i-1]+1                 # 1을 빼는 연산 -> 1회 진행
    if i%2 == 0:                    # 2로 나눠 떨어질 때, 2로 나누는 연산
        d[i] = min(d[i], d[i//2]+1)
    if i%3 == 0:                    # 3으로 나눠 떨어질 때, 3으로 나누는 연산
        d[i] = min(d[i], d[i//3]+1)

print(d[x])

# 걸린 시간 : 약 41분


# TopDown 방식 (재귀 활용)
import sys
input = sys.stdin.readline

x = int(input())
# 딕셔너리로 초기화
# 1일 때 1이 되는 데 필요한 연산 횟수는 0
d = {1:0}

# 숫자 i를 입력 받아 재귀적으로 딕셔너리 채워가는 것
def rec(i):
    # 재귀 종료 조건 : 입력받은 i가 딕셔너리의 key에 존재할 경우 d[i] 리턴
    if i in d.keys():
        return d[i]
    # 2로 나눠도 떨어지고, 3으로 나눠도 떨어지는 경우 둘 중 최솟값을 넣음
    if (i%2 == 0) and (i%3 == 0):
        # rec(i//3)+1 : i를 3으로 나눈 몫이 1이 되는데 필요한 최소 연산 횟수 + i를 3으로 나누는 연산 횟수 1회
        d[i] = min(rec(i//2)+1, rec(i//3)+1)
    elif i%2 == 0:
        # rec(i-1)+1 : i-1이 1이 되는데 걸리는 최소 연산 횟수
        d[i] = min(rec(i//2)+1, rec(i-1)+1)
    elif i%3 == 0:
        d[i] = min(rec(i//3)+1, rec(i-1)+1)
    # i가 3으로도 나눠 떨어지지 않고, 2로도 나눠 떨어지지 않는 경우
    else:
        # i-1이 1이 되는데 걸리는 최소 연산 횟수 + 1회(i에서 1을 빼는 연산 1회)
        d[i] = rec(i-1)+1
    # 재귀 호출을 모두 마무리, rec(x)의 결과를 최종 반환 
    return d[i]

print(rec(x))


