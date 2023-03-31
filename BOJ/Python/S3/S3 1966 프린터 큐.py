import sys
import heapq
input = sys.stdin.readline

n = int(input())                            # n: 3

def solution(pri, loc):                     # loc,pri: 0, 5 / loc,pri: 2, [1,2,3,4]                     / loc,pri: 0, [1,1,9,1,1,1]
    heap = []                               # heap: [-5]    / heap: [-4, -3, -2, -1] -> [-3, -1, -2]    / heap: [-9.-1,-1,-1,-1,-1]
    ans = 1                                 # ans: 1        / ans: 1                 -> ans: 2          / ans: 5
    for i in pri:                           # i: 0          / i: 3                                      / i: 2
        heapq.heappush(heap, (-i))
    while heap:
        for i in range(len(pri)):
            if pri [i] == -heap[0]:         # pri: [-5]    / i = 3일 때 pri[3]: 4, -heap[0]: -(-4) = 4
                if i == loc:
                    return ans
                heapq.heappop(heap)
                ans += 1

for i in range(n):
    i, j = map(int, input().split())        # i,j: 1,0 / i,j: 4,2       / i,j: 6,0
    h = list(map(int, input().split()))     # h: [5]   / h: [1,2,3,4]   / h: [1,1,9,1,1,1]
    print(solution(h, j))