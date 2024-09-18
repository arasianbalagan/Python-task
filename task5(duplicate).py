
#revome duplicate values

a=[10,20,30,40,5,30,20,50,20,45]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)
