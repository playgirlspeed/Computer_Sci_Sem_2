x = int(input("Whats is your first number?"))
op = input("What is your operator?")
y = int(input("What is your second number?"))
equals = "="
if(op=='+'):
    answer = x+y
    print(answer)
    
if(op=='-'):
    answer = x-y
    print(answer)
    
if(op=='*'):
    answer = x*y
    print(answer)
    
if(op=='/'):
    answer = x/y
    print(answer)