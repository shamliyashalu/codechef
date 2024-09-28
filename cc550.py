t=int(input())
while t>=1:
    a,b,c,d=map(int, input().split())
    if(a==b==c==d==0):
        print("in")
    else:
        print("out")
    t -= 1
	