n = input()             # 점수 N 입력 받기
digit = len(n)//2       # N의 자릿수 형태는 항상 짝수

l = 0                   # 좌측 합
r = 0                   # 우측 합

for i in n[:digit]:     # 문자열 좌측 기준 슬라이싱
    l += int(i)
for i in n[digit:]:     # 문자열 우측 기준 슬라이싱
    r += int(i)

if l == r:              # 좌측 합과 우측 합 비교
    print("LUCKY")      # 같으면 LUCKY 출력
else:
    print("READY")      # 다르면 READY 출력

# 걸린 시간 : 약 56분

