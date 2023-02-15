# 정답 1. 플로이드-워셜
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):          # 경유지 노드
    for j in range(n):      # 출발 노드
        for k in range(n):  # 도착 노드
            # i에서 j로 가는 경로가 있으면 1 출력
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1

for n in graph:
    print(*n)


# 걸린 시간 : 약 89분