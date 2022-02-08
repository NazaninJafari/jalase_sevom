
import random

words = ['book','python','bag','umbrella','dog','clock','engineer','toothpaste','shirmoz']
i = 0
joon  = 5

#word = random.choice(words)

while joon > 0 :
    word = random.choice(words)
    print ('-' * len(word))
    a = input ("what is your idea? ")
    user_character = a.lower()
    
    if user_character in word :
        print ("yes")
        i += 1
        joon -=1
      

    else :
        joon = joon - 1
        print ("No!")    

if i == len(words) :
    print ("you won :)")
else :
    print("game over")    