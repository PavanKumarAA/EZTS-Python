#BODMAS EXPRESSION IS VALID OR NOT
''' [3+7{52/11(3+5)}] valid
[4-6(235(9+6)] invalid'''
class stack:
    def __init__(self):
        self.items=[]
   
    def push(self,data):
        self.items.append(data)
   
    def pop(self):
        return self.items.pop()
        
    def size(self):
        return len(self.items)
        
    def top(self):
        return self.items[-1]
e="[3+7{52/11(3+5)}]"
s=stack()
OB="[{("
CB=")}]"
flag=0

for i in e:
    if i in OB:
        s.push(i)
    if i in CB:
        x=s.pop()
        if x=="(" and i==")":
            pass
        elif x=="{" and i=="}":
            pass
        elif x=="[" and i=="]":
            pass
        else:
            flag =1
            break
if flag == 0 and s.size()==0:
    print("valid")
else:
    print("invalid")
print(s.size())          
