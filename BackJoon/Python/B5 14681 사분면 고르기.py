x=int(input())
y=int(input())

if x>0 and y>0:     # x,y가 양수일 때 1사분면
    print("1")
elif x<0 and y>0:   # x가 음수, y가 양수일 때 2사분면
    print("2")
elif x<0 and y<0:   # x,y가 음수일 때 3사분면
    print("3")
else:
    print("4")      # x가 양수, y가 음수일 때 4사분면
