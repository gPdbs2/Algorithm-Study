# 정답 1
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())

    before = list(str(input().split()))
    after = list(str(input().split()))

    if sorted(before) == sorted(after):
        print("NOT CHEATER")
    else:
        print("CHEATER")

###################################################################

# 정답 2
import sys
input = sys.stdin.readline

# 테스트 케이스
T = int(input())

# 테스트 케이스만큼 실행
for i in range(T):

    # 범고래가 기억하는 카드 갯수 n
    n = int(input().rstrip())
    # 놀이 전, 후의 범고래가 기억하는 n개의 카드 리스트
    before = sorted(list(input().rstrip().split()))
    after = sorted(list(input().rstrip().split()))

    # 전과 후가 일치하면 NOT CHANGER, 일치하지 않으면 CHANGER 출력
    if before == after:
        print("NOT CHEATER")
    else:
        print("CHEATER")


# 걸린 시간 : 약 63분