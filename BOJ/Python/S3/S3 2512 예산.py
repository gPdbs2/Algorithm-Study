import sys
input = sys.stdin.readline

n = int(input())
budget = list(map(int, input().split()))
m = int(input())

def binary(start, end):
    while start <= end:
        total = 0
        mid = (start+end)//2
        for i in budget:
            if i > mid:
                total += mid
            else:
                total += i
        if total <= m:
            start = mid+1
        else:
            end = mid-1

    return end

a = binary(0, max(budget))
print(a)

# 걸린 시간 : 약 77분