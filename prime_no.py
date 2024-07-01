#prime no
m= int(input("enter the no:"))
flag = 0
if m<0:
    flag=1
elif m==0:
    flag=0
else:
    for i  in range(2,m):
        if m%i==0:
            flag = 1
            break
if flag ==0:
    print("valid ")
else:
    print("invalid")