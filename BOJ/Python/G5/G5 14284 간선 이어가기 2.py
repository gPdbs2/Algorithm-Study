import heapq                    # 힙 자료구조 활용
import sys
input = sys.stdin.readline
INF = int(1e9)                  # 무한을 의미하는 값으로 10억 지정

# n: 정점의 갯수, m: 간선 수
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
# distance 저장 => 이 때 배열의 값은 시작점에서 다른 모든 노드로 가는 최솟값으로 갱신될 예정
distance = [INF]*(n+1)

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))     # a에서 b까지 가는 데 드는 가중치는 c
    graph[b].append((a, c))     # 무방향 (양방향) 처리

s, t = map(int, input().split())

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 거리를 0으로 설정 후 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 이미 처리된 노드는 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드들 확인
        for i in graph[now]:
            cost = dist+i[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧으면 갱신
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(s)
print(distance[t])


# 걸린 시간 : 약 50분