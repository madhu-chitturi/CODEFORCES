                                                                A. Floor Number
  
t=int(input())
for _ in range(t):
    n,x=map(int,input().strip().split())
    c=2
    floor=1
    while(c<n):
        c+=x
        floor+=1
    print(floor)
