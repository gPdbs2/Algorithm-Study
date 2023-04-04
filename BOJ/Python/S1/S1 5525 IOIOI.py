import sys
input = sys.stdin.readline

n = int(input())    # 문자열 갯수
m = int(input())    # 문자열 s의 길이
s = input()         # 문자열

# i: 인덱스, pattern: 문자열 갯수, cnt: IOI 갯수
i, pattern, cnt = 0, 0, 0

while i < m-1:
    # 현재 문자열이 'IOI' 일 경우
    if s[i-1] == 'I' and s[i] == 'O' and s[i+1] == 'I':
        i += 2
        # 문자열 갯수에 1 추가
        pattern += 1
        # 패턴 갯수가 n과 일치하면 s 안에 Pn이 포함된 것
        if pattern == n :
            # 패턴 갯수-1
            pattern -= 1
            cnt += 1
    else:
        i += 1
        pattern = 0

print(cnt)


# 걸린 시간 : 약 42분