a=int(input())
for i in range(a):
    x,y,z=map(int,input().split())
    k=x*y
    if k-z < k/2:
        print("YES")
    else:
        print("NO")