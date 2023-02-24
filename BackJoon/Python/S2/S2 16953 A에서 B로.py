# 정답 1
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
cnt = 1     # 연산의 최솟값+1
while True:
    # a와 b가 같으면 break
    if b == a:
        break
    # b에서 a를 만들 수 없는 경우 : -1 출력
    # 1. b를 2로 나눌 수 없고, 10으로 나눈 나머지가 1이 아닌 경우
    # 2. b가 a보다 작은 경우
    elif (b%2 != 0 and b%10 != 1) or b < a:
        cnt = -1
        break
    # 10으로 나눈 나머지가 1이면 (끝자리가 1이면) b에서 1을 빼서 제거
    else:
        if b%10 == 1:
            b //= 10
            cnt += 1
        # b가 2로 나눠지는 경우 2로 나눈 후 cnt에 1 추가
        else:
            b //= 2
            cnt+= 1

print(cnt)


# 정답 2
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
cal = 1

while(b != a):
    cal += 1
    temp = b
    if b%10 == 1:
        b //= 10
    # 짝수인 경우 2로 나누도록 함
    elif b%2 == 0:
        b //= 2
    # 위 두 연산 수행 후 값의 변화가 없을 경우 -1 출력
    if temp == b:
        print(-1)
        break

else:
    print(cal)


# 걸린 시간 : 약 79분