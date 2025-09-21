import random
number=random.randint(1,100)
attempts=0
guess=None 
print("I have thought a number!! Try to guess it!!")
while guess!=number:
 guess=int(input("Enter your Guess here:"))
 attempts+=1
 if guess<number:        
  print("Too low!! Try again")
 elif guess>number:
  print("Too high!! Try again")
 else:
   print(f"Congratulations!! You guessed it right in {attempts} attempts")     
