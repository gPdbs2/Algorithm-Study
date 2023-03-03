import sys

t = int(sys.stdin.readline())               # 테스트 케이스

for i in range(t):                          # 테스트 케이스 수만큼 반복
    R, S = input().split()
    for j in S:                             # 문자 반복
        print(j*int(R), end="")             # j * 문자열 R
    print()                                 # 개행

