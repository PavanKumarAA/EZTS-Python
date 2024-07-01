#find the smallest positive integer present in the list of array
arr=[4,-5,0,2,-3,-56,3,45]
min=arr[0]
for i in range(1,len(arr)):
    if arr[i]<min and arr[i]>=1:
        min=arr[i]
print(min)