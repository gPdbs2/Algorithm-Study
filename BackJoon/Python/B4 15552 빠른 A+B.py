import sys

t = int(sys.stdin.readline())       # input 대신 sys.stdin.readline 활용 가능
                                    # 문자열 저장하고자 할 경우 : sys.stdin.readline.rstrip()
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)

# 걸린 시간 : 약 37분
