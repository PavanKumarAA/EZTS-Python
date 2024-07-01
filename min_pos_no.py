#first missing positive no
arr=[4,-5,0,2,-3,-56,3,45]
min=arr[0]
for i in range(1,len(arr)):
    if arr[i]<arr[0]:
        min=arr[i]
print(min)
