a, b = input().split()                                      # a, b를 문자로 입력 받음(replace() 사용하기 위해)

min = int(a.replace('6', '5')) + int(b.replace('6', '5'))   # 최솟값 : 6을 5로 본 경우
max = int(a.replace('5', '6')) + int(b.replace('5', '6'))   # 최댓값 : 5를 6으로 본 경우

print(min, max, end=" ")                                    # 최솟값, 최댓값을 공백 두고 출력

# 걸린 시간 : 약 41분