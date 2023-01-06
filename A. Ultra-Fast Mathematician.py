                                                                      A. Ultra-Fast Mathematician
  
a=input()
b=input()
c=[]
for i in range(len(a)):
    if(a[i]==b[i]):
        c.append(0)
    else:
        c.append(1)
for k in c:
    print(k,end="")
