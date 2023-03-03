import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# n: 지름길 갯수, d: 고속도로 길이
n, d = map(int, input().split())
graph = [[] for _ in range(d+1)]
distance = [INF]*(d+1)

# 다익스트라
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 최소 거리를 1로 초기화
for i in range(d):
    graph[i].append((i+1, 1))

# 지름길이 있는 경우에 업데이트
for _ in range(n):
    s, e, l = map(int, input().split())
    # 도착 지점보다 고속도로 길이가 길면 무시
    if e > d:
        continue
    graph[s].append((e, l))

dijkstra(0)
print(distance[d])


# 걸린 시간 : 약 83분