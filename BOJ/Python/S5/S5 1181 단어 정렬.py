n = int(input())            # 단어 갯수
a = []                      # 리스트 생성

for i in range(n):
    a.append(input())       # 단어

a = list(set(a))            # 중복 제거
a.sort()                    # () 안 공백일 경우 알파벳 사전 순서대로 정렬
a.sort(key=len)             # 문자열 길이 순 정렬

for j in a:
    print(j)                # 한 줄에 1개씩 출력

# 걸린 시간 : 약 49분