import sys
input = sys.stdin.readline

# 테스트 케이스
t = int(input())

# 테스트 케이스 수만큼 반복
for i in range(t):
    # 단어를 구성하는 문자를 담을 문자열 a, b 생성
    a,b = map(str, input().split())

    # 문자열 a,b를 리스트 x,y로 변환 후 정렬
    x = sorted(list(a))
    y = sorted(list(b))

    # 정렬된 리스트 x,y의 일치 여부 확인
    if x == y:
        print(a + ' & ' + b + ' are anagrams.')
    else:
        print(a + ' & ' + b + ' are NOT anagrams.')

# 걸린 시간 : 42분