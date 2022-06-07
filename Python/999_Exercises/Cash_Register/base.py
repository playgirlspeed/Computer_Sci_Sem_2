items = int(input("How many items? "))

total = 0
for i in range (0, items):
    itemName = input("What is the item?" )
    price = float(input("How much is it?" ))
    print("Thanls for purchasing" + itemName)
    total = total + price
    
print("Your totals is:" + str(total))