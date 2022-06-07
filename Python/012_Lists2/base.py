import random
thislist = [1,2,3,4,5,6,7,8,9,10]

x=int(input("how many random numbers"))
print("your numbers")
for i in range(0,x):
    print(thislist[random.randrange(10)], end=" ")
    
    
thatlist = []
for z in range (0,x):
    f = random.randrange(1,10)
    thislist.append(f)
print("\n"+ "your random number are" + "\n" + str(thislist))

