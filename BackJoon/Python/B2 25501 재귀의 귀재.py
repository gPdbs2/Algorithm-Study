import sys                              # input()보다 입력값 받아오는 속도가 더 빠름

t = int(sys.stdin.readline())           # 테스트 케이스

def recursion(s, l, r):
    global cnt                          # 호출 횟수 (함수 내 전역 변수로 사용하기 위해 global로 명시)
    cnt +=1                             # 함수 출력 시마다 cnt 증가
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for i in range(t):                      # 테스트 케이스 수만큼 반복
    cnt = 0
    print(isPalindrome(sys.stdin.readline().rstrip()), cnt)

# 걸린 시간 : 약 43분