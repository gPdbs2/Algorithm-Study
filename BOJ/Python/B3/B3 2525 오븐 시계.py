# 정답 1
h, m = map(int, input().split())
t = int(input())

h += t // 60       # 시 = 걸리는 시간//60
m += t % 60        # 분 = 걸리는 시간%60

if m >= 60:        # 분이 60 이상일 경우 h=h+1, m=m-60
    h += 1
    m -= 60
if h >= 24:        # 시가 24 이상일 경우 h=h-24
    h -= 24

print(h, m)


# 정답 2
h, m = map(int, input().split())
m += int(input())

print((h+m//60) % 24, m % 60)       # h = (시 + 분//60분) % 24시간, m = 분 % 60분
