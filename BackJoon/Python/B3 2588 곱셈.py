a=int(input())
b=int(input())

# 파이썬 나누기는 슬래시 2개 (//)
out1=a*((b%100)%10)     # a*(b의 1의 자리 수)
out2=a*((b%100)//10)    # a*(b의 10의 자리 수)
out3=a*(b//100)         # a*(b의 100의 자리 수)

res=a*b
print(out1,out2,out3,res,sep="\n")