n = int(input())                        # 우유 가게 수
info = list(map(int, input().split()))  # 우유 가게 정보(리스트)

cnt = 0                                 # 마신 우유 수를 변수에 저장

for i in range(n):                      # 우유 가게를 차례로 방문
    if info[i] == cnt%3:                # 우유 가게 정보(info[i])와 이번에 마실 우유(마신 우유의 수/3의 나머지) 비교
        cnt +=1                         # 같다면 cnt 1 증가

print(cnt)

# 걸린 시간 : 약 70분