import random
i=0
score=0
while i<=3:
    random_number = random.randint(1,3)
    guess=int(input("Guess a number from 1 to 3 : "))
    if guess != random_number:
        print("You Guessed it  wrong")
        print("The number is {}".format(random_number))
        score=score+1
    else:
        print("Yes Your guess was correct")
        print("The number is {}".format(random_number))
    i=i+1
print("Your score is {}".format(score))
