#selection sort
l=list(map(int,input().split()))
n=len(l)
for j in range(0,n):
    pos=j
    min=l[j]
    for i in range(j,n):
        if l[i]<min:
            min=l[i]
            pos=i
        l[j],l[pos]=l[pos],l[j]
print(l)
    