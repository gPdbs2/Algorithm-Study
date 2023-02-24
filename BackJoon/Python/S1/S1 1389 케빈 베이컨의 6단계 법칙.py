from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start):
    num = [0]*(n+1)
    visited = [start]
    q = deque()
    q.append(start)

    while q:
        # list.pop() 사용 시 시간 복잡도 : O(N)
        a = q.popleft()
        for i in graph[a]:
            # BFS 함수 실행 시 start 노드에서 다른 노드로 갈 수 있을 때
            if i not in visited:
                # num 리스트의 각 인덱스 값+1 해주고 다음 BFS로 넘김
                num[i] = num[a]+1
                visited.append(i)
                q.append(i)
    # num 리스트에 있는 수들의 총합 return
    return sum(num)

if __name__ == '__main__':
    n, m = map(int, input().rstrip().split())
    # 양방향 노드 그래프
    # 범위 n+1 : 노드 번호가 1부터 시작하므로
    graph = [[] for _ in range(n+1)]
    # 각 인덱스마다 몇 번 노드와 연결되어 있는지 저장
    for i in range(m):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    # res 리스트 만들어 노드 1~n까지 결과 값 sum을 res 리스트에 넣어줌
    res = []
    # 1번 노드부터 BFS 호출
    for i in range(1, n+1):
        res.append(bfs(graph, i))

    # 가장 작은 숫자가 있는 인덱스 출력
    print(res.index(min(res))+1)


# 걸린 시간 : 약 83분