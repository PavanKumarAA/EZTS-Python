''' given an integer array your task is to find the k continues digits which gives you the maximum sum where k is given by user
sample input
[2,4,3,5,6,3,4,6,7,1,2,5]
ouput:[4,6,7]
'''
l=[2,4,3,5,6,3,4,6,7,1,2,5]
sum=max=0
k=int(input("enter the no of continues digit:"))
for i in range(0,len(l)-k+1):
    sum=0
    for j in range(0,k):
        sum+=l[i+j]
    if max<sum:
        max=sum
        pos=i
print("result")
print(max)
print("the sequence of ",k,"continues no are")
for j in range(0,k):
    print(l[pos+j])