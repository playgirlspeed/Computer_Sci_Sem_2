import random
word_list = []
with open('allow_words.txt') as f:
    for line in f:
        l = line.strip()
        word_list.append(1)

num = random.randrange(0,12972)
answer = word_list[num]
print(answer)

a = 0 
for i in range(0,6):
    guess = input("Guess a word! ")
    if guess == answer: 
        print("You Won!!!")
        a = 1
        break
    else:
        print("Guess Again!")

if a == 0:
    
    
    
    
    
    
    print("You lose!")
    
    
f.close()
