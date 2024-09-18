#words pattern

'''type1'''

a=input("enter any words:")
b=len(a)
for i in range(b):
    j=0
    while j<i+1:
        print(a[j],end='')
        j+=1
    print("\n")

'''type2'''

a="hello world"
b=len(a)
for i in range(b):
    j=0
    while j<i+1:
        print(a[j],end='')
        j+=1
    print("\n")
