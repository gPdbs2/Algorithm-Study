x = int(input())    # 영수증에 적힌 총 금액
n = int(input())    # 구매한 물건의 종류의 수

t = 0               # 총 금액

for i in range(n):
    a, b = map(int, input().split())    # map(): 입력값 한꺼번에 정수로 변환
    t += a*b                            # 총 금액 = 각 물건의 가격 a * 개수 b

if t == x:
    print("Yes")
else:
    print("No")