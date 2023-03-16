import sys
input = sys.stdin.readline

# n: 듣도 못한 사람, m: 보도 못한 사람
n, m = map(int, input().split())
# n_li: 듣도 못한 사람 리스트, m_li: 보도 못한 사람 리스트
n_li = [input().rstrip("\n") for _ in range(n)]
m_li = [input().rstrip("\n") for _ in range(m)]

# 각 리스트의 중복되는 이름 뽑아내기
intersection = list(set(n_li) & set(m_li))
print(len(intersection))

# 교집합 리스트 정렬 후 출력
for i in sorted(intersection):
    print(i)

# 걸린 시간 : 약 62분