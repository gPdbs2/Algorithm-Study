t = int(input())

for i in range(t):
    a = list(input())       # 리스트 A 생성
    score = 0               # 점수
    sum = 0                 # 총 점수

    for j in a:
        if j == 'O':        # 문제를 맞춘 갯수가 연속일 경우 1씩 커짐
            score += 1
            sum = sum + score
        else:
            score = 0
    print(sum)              # 총 점수 출력

# 걸린 시간 : 약 50분