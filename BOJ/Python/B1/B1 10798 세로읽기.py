arr = [[] for i in range(15)]       # 최대 글자 수(15)만큼 반복해서 리스트 생성

for _ in range(5):                  # 입력 받을 단어 수(5)만큼 반복
    word = input()
    for i in range(len(word)):      # 단어의 글자 수만큼 반복
        arr[i].append(word[i])      # 리스트에 첫 번째 글자 = 0 번째 리스트, 두 번째 글자 = 1 번째 리스트에 추가
res = ''

for i in range(len(arr)):           # arr 길이 만큼 반복
    res += ''.join(arr[i])          # res 는 각 리스트를 join 한 글자 수를 붙여준 것

print(res)

# 걸린 시간 : 약 82분