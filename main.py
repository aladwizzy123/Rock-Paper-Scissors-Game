import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]


userchoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
 
print(images[userchoice])

computerchoice = random.randint(0,2)
print("Computer chose ")
print(images[computerchoice])
if userchoice >= 3 or userchoice < 0: 
  print("You typed an invalid number, you lose!") 
elif userchoice == 0 and computerchoice == 2:
  print("You win!")
elif computerchoice == 0 and userchoice == 2:
  print("You lose")
elif computerchoice > userchoice:
  print("You lose")
elif userchoice > computerchoice:
  print("You win!")
elif computerchoice == userchoice:
  print("It's a draw")


