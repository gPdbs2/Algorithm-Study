# 정답 1 (1로 만들기 코드 응용)
import sys
input = sys.stdin.readline

n = int(input())
a = int(1e9)
d = [a]*5001                                # n의 최댓값이 5000 -> 5000까지 최댓값으로 초기화
d[3] = d[5] = 1                             # 3과 5 인덱스에 봉지를 의미하는 1 부여

for i in range(3, n+1):
    d[i] = min(d[i], d[i-3]+1, d[i-5]+1)    # 3부터 n+1까지 순차적으로 저장

if d[n] == a:
    print(-1)
else:
    print(d[n])


# 정답 2 (메모이제이션 활용)
import sys
input = sys.stdin.readline

n = int(input())
# n kg일 때 각각 가장 적은 양의 봉지를 담을 용도
# 최솟값을 구해야 하기 때문에 n의 범위보다 1이 큰 5001을 값으로 지정
# 배열 크기를 n+5로 잡은 이유 : n의 값이 5보다 작을 경우 index out of range 오류 잡기 위해서
d = [5001]*(n+5)
# 인덱스 3, 5에는 각각 봉지 1개를 사용하고 최초의 값으로 대입하기 위해 1 사용
d[3] = d[5] = 1

# 5 이하인 경우는 이미 결과가 저장되어 있으므로 6부터 시작
for i in range(6, n+1):
    d[i] = min(d[i-3]+1, d[i-5]+1)

# n kg 만들 수 없으면 배열 값이 5000보다 크기 때문에 치환해서 -1 반환
print(d[n] if d[n] < 5001 else -1)


# 걸린 시간 : 약 80분