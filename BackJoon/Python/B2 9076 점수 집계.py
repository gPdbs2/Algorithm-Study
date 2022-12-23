import sys
input = sys.stdin.readline

t = int(input())                          # 테스트 케이스

for i in range(t):
    n = list(map(int, input().split()))   # 5명 심판의 점수
    n.sort()                              # 리스트 정렬

    if n[3]-n[1] >= 4:                    # 중간 3명 중 최고점, 최저점 차이가 4 이상일 경우 KIN 출력
        print("KIN")
    else:                                 # 총점 출력
        print(sum(n)-max(n)-min(n))

# 걸린 시간 : 24분