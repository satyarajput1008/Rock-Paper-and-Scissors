#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

options = ('rock','paper','scissors')
running = True

while running:

  player = None
  computer = random.choice(options)

  while player not in options:
    player = input("Enter A Choice(rock, paper,scissors): ")

  print(f"Player: {player}")
  print(f"Computer:{computer}")

  if player == computer:
    print("It's A Tie!")
  elif player == "rock"  and computer == "scissors":
    print("You Win!")
  elif player == "paper" and computer == "rock":
    print("You Win!")
  elif player == "scissors" and computer == "paper":
    print("You Win!")
  else:
    print("You Lose!")

  if not input("Play Again?(y/n):").lower()== "y":
    running = False

print ("Thanks For Playing!")


# In[ ]:




