import sys
input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))
ans = [0]*n

# 각 자리에 들어갈 사람 확인
for i in range(n):
    # 좌측에 있는 자기보다 큰 사람 수
    cnt = 0

    # 모든 사람 확인
    for j in range(n):
        # 좌측에 있는 키 큰 사람 수와 일치하고, 그 자리에 아무도 없으면
        if cnt == ans[i] and line[j] == 0:
            ans[j] = i+1
            break
        # 자리에 아무도 없으면 좌측에 키 큰 사람 수 카운트
        elif ans[j] == 0:
            cnt += 1

print(*ans)


# 걸린 시간 : 약 65분