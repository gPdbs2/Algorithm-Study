n = int(input())                    # n : 수의 갯수
n_list = []                         # 리스트 생성

for i in range(n):                  # n 갯수만큼 리스트에 요소 삽입
    n_list.append(int(input()))
n_list.sort()                       # 오름차순 정렬
for j in range(len(n_list)):        # 정렬한 수를 1개씩 출력
    print(n_list[j])

# 걸린 시간 : 약 37분
