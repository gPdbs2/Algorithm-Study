n, x = map(int, input().split())        # n : 정수 갯수, x : 기준 정수

a = list(map(int, input().split()))     # 수열 A 리스트

for i in range(n):
    if a[i] < x:
        print(a[i], end=' ')            # 입력받은 순서대로 공백으로 구분 출력(end로 끝문자 지정)

# 걸린 시간 : 약 35분