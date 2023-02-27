import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

# 정점 갯수 n, 간선 갯수 e
n, e = map(int, input().split())
graph= [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    # 무방향(양방향) 처리
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
    q = []
    distance = [INF] * (n + 1)
    distance[start] = 0

    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

p = dijkstra(1)

v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)

# 경로 비교
# 시작점 -> 정점1 최단경로 + 정점1 -> 정점2 최단경로 + 정점2 -> 도착점의 최단경로 길이
# 시작점 -> 정점2 최단경로 + 정점2 -> 정점1 최단경로 + 정점1 -> 도착점의 최단경로 길이
res = min(p[v1] + v1_dist[v2] + v2_dist[n], p[v2] + v2_dist[v1] + v1_dist[n])

if res < INF :
    print(res)
else:
    print(-1)


# 걸린 시간 : 약 51분