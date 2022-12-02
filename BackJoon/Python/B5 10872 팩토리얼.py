def factorial(n):                # 재귀 호출
    if n <= 1:                   # n이 1 이하일 때 1 반환
        return 1
    return n * factorial(n - 1)  # n! = n * (n-1)!

n = int(input())
print((factorial(n)))

# 걸린 시간 : 약 29분