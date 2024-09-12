a=['arasi','dheena','ammu','blacky','karuva']
b=[5000,7000,3000,4000,2500]

sender = input("enter the sender name:")
reciver=input("enter the reciever name:")
amount=int(input("enter amound:"))

for i in a:
    if i==sender:
         print("sender is available")
         x=(a.index(i))
         print("sender balance amount:",b[x]-amount)
        
    elif i==reciver:
         print("receiver is available")
         y=(a.index(i))
         print("receiver full amount:",b[y]+amount)
         break


