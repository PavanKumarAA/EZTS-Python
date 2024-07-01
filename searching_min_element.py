#searching for min element using bubble sort
l=list(map(int,input("enter the elements to be sorted").split()))
target=l[0]
for i in range(0,len(l)):
    if l[i]<target:
        target=l[i]
print(target)