import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())                   # n: 수빈 위치, k: 동생 위치
max = 100000                                       # n, k의 최댓값 지정
distance = [0]*(max+1)

def bfs():
    q = deque()                                    # 큐를 빠르게 해주기 위해 deque 설정
    q.append(n)                                    # 수빈이 위치 n을 넣어줌
    while q:                                       # q가 정수일 때 while문을 통해 계속 반복
        x = q.popleft()                            # 제일 좌측 값을 pop, 그리고 그 값을 x에 저장
        if x == k:                                 # 만약 x의 값이 동생의 위치 k 이면 distance[x] 출력 후 종료
            print(distance[x])
            break
        for i in (x-1,x+1,x*2):                    # for문을 돌려 x-1,x+1,x*2의 값을 j에 순서대로 넣음
            if 0 <= i <= max and not distance[i]:  # 만약 i의 값이 0과 max 사이의 값 & distance[i]가 0의 값을 가지면
                distance[i] = distance[x]+1        # distance[x]에 +1
                q.append(i)                        # i를 큐에 추가
bfs()

# 걸린 시간 : 약 57분