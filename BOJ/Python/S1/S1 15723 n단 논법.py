import sys
input = sys.stdin.readline
INF = int(1e9)

# N: 전제의 갯수
N = int(input())
# 알파벳 소문자 문자열
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# n: 문자열 길이
n = len(alphabet)
# 초기값이 INF인 배열 생성
graph = [[INF]*n for _ in range(n)]


for _ in range(N):
    # 전제 입력받기 => "a is b"
    a, b = map(alphabet.index, input().rstrip().split(" is "))
    graph[a][b] = 1

# 플로이드-워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            # i가 k를 거쳐 j로 갈 수 있는 경우 서로 연결
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

# M: 결론 갯수
M = int(input())

for _ in range(M):
    # 출력 => "a is b"
    a, b = map(alphabet.index, input().rstrip().split(" is "))
    # a와 b가 연결되어 있지 않으면 해당 값은 INF이므로 이때 F 출력
    if graph[a][b] == INF:
        print("F")
    else:
        print("T")


# 걸린 시간 : 약 61분