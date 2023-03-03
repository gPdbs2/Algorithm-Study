import sys
input = sys.stdin.readline

# word : 입력 받을 단어의 스펠링 리스트, res : 결과 담을 리스트
word = list(map(str, input().rstrip("\n")))
res = []

# 3개의 단어로 자를 수 있는 모든 경우의 단어를 구함
for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        first = word[:i]    # 첫 번째 단어
        second = word[i:j]  # 두 번째 단어
        third = word[j:]    # 세 번째 단어

        # 각 단어의 스펠링 순서 뒤집기
        first.reverse()
        second.reverse()
        third.reverse()

        # 뒤집은 단어를 원래 순서대로 합친 후 res 리스트에 추가
        res.append("".join(first+second+third))

# res 리스트에서 가장 작은 단어 출력
# 사전 순으로 가장 앞에 있는 단어
print(min(res))

# 걸린 시간 : 약 67분