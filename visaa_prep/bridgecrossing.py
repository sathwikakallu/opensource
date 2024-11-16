x,y,z=map(int,input().split())
if z>=(x+y):
    print((z-y)//x)
else:
    print(0)
