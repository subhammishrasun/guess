'''import random

target=random.randint(1,500)
 
while True:
    userChoice=input("Guess the target or quit:")
    if(userChoice=="quit"):
        break

    userChoice=int(userChoice) 
    if(userChoice==target):
        print("Sucess:Correct Guess!! ")
        break

    elif(userChoice<target):
        print("your numer is too small.Take a bigger guess..")
    else:
        print("your number was too big.Take a smaller guess..")

print("----GAME OVER----")  '''

import random
import string

pass_len=12
charValues=string.ascii_letters+string.digits+string.punctuation

password=""
for i in range(pass_len):
    password+=random.choice(charValues)

print("your random password:",password)