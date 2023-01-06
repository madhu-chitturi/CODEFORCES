                                                                    A. Stones on the Table
  
n=int(input())
s=list(input())
c=0
p1=0
p2=1
while(p1<n and p2<n):
    if(s[p1]==s[p2]):
        p1+=1
        p2+=1
        c+=1
    else:
        p1+=1
        p2+=1
print(c)
