#counting the highest repeated no of vowels
def count_vowel(s):
    dict={'A':0,'E':0,'I':0,'O':0,'U':0}
    for i in s:
        if i=='a' or i =='A':
            dict['A']+=1
        elif i=='e' or i =='E':
            dict['E']+=1
        elif i=='i' or i =='I':
            dict['I']+=1
        elif i=='o' or i =='O':
            dict['O']+=1
        elif i=='u' or i =='U':
            dict['U']+=1  
    x=max(dict.values())
    #print(dict.items())
    result=[]
    for i,j in dict.items():
        if j ==x:
            result.append(i)
    return result
i_p=[ 
    ["Alex", "I enjoy hiking in the mountains."],
     ["Sam", "A lovely sunny day at the beach."],
     ["Jamie", "Reading a book is my favorite pastime."], 
     ["Taylor", "I love playing video games on weekends."], 
     ["Chris", "Exploring new cities is exciting and fun."]

]
o_p={}
for i in i_p:
    o_p[i[0]]=count_vowel(i[1])
print(o_p)
    
    