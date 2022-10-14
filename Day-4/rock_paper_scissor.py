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

#Write your code below this line 👇
game_options = [rock,paper,scissors]

#print(game_options[0])
user = int(input("what do you choose? Type 0 for Rock , 1 for Paper or 2 for Scissors\n"))
if(user >2):
    print("This is not possible!!!")
    
print(game_options[user])
computer = random.randint(0,2)
print("Computer choose:- ")
print(game_options[computer])

if(user == computer):
  print("You draw.")
elif(user == 0 and computer == 2):
  print("You win!!!")
elif(computer ==0 and user == 2):
  print("You loose!!!")
elif(user == 1 and computer == 0):
  print("You win!!")
elif(computer > user):
  print("You loose!!")
else:
  print("You entered wrong , you loose!!")