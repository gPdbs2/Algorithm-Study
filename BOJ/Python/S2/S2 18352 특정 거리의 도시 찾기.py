from collections import deque           # 큐 자료구조 활용을 위해 deque 라이브러리 사용
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())  # 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
graph = [[] for _ in range(n + 1)]      # index 맞추기 위해서 n+1 개 row 생성

# 모든 도로 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0

# BFS 탐색 실행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면 -1 출력
if check == False:
    print(-1)

# 걸린 시간 : 91분

######################################################################################################################

# 정답 2
# check True, False 제거 => if k in distance: 추가 후 들여쓰기
from collections import deque           # 큐 자료구조 활용을 위해 deque 라이브러리 사용
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())  # 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
graph = [[] for _ in range(n + 1)]      # index 맞추기 위해서 n+1 개 row 생성

# 모든 도로 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0

# BFS 탐색 실행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순 출력
if k in distance:
    for i in range(1, n + 1):
        if distance[i] == k:
            print(i)

# 만약 최단 거리가 K인 도시가 없다면 -1 출력
else:
    print(-1)