n = int(input())                       # 사람 수
p = list(map(int, input().split()))    # 배열 생성

p.sort()                               # 오름차순 정렬 (반복해서 더해지는 숫자를 작게 하기 위해)

time = 0                               # 대기 시간
total = 0                              # 총 걸리는 시간

for i in p:                            # 사람 수만큼 반복
    time += i                          # 대기 시간 누적
    total += time                      # 대기 시간을 총 시간에 넣어 다음 사람의 시간에 반영

print(total)

# 걸린 시간 : 약 63분
