n = int(input())                                   # 입력받은 색종이 수
p = [[0] * 100 for _ in range(100)]                # 도화지 범위 배열 선언, 초기화

for _ in range(n):                                 # 입력된 색종이 수만큼 돈다
    x, y = map(int, input().split())               # 좌측 하단에서 x,y좌표 받기
    for i in range(x, x+10):                       # x(세로) 반복 : 시작점 ~ 시작점+색종이 세로 길이
        for j in range(y, y+10):                   # y(가로) 반복 : 시작점 ~ 시작점+색종이 가로 길이
            p[i][j] = 1                            # 해당 범위 값 0 -> 1로 교체

cnt = 0                                            # 결과값(넓이) 변수 설정
for k in p:                                        # 도화지 전체 면적 반복
    cnt += k.count(1)                              # 범위 값이 1인 경우만 세어 준다

print(cnt)                                         # 결과값(넓이) 출력

# 걸린 시간 : 약 66분
