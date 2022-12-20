n, k = map(int, input().split())             # n : 응시자 수 , k : 상받는 사람 수
score = list(map(int, input().split()))      # 리스트 생성

score.sort(reverse=True)                     # 리스트 요소를 내림차순 정렬

print(score[k-1])                            # 커트라인 인원 k에서 -1한 값을 출력

# 걸린 시간 : 39분