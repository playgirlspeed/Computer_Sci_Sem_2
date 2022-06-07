hv = input("Horizontal or vertical?")
num = int(input("How long?"))
sym = input("what symbol?")
if(hv =='v'):
    for i in range(num):
        print(sym)
if(hv =='h'):
    for i in range(num):
        print( end = sym + " ")