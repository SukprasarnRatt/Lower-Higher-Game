import random
from replit import clear
import art
import game_data
def check_answer(a, b, answer):
  """ Check Answer than return True or False"""
  if a['follower_count'] > b['follower_count'] and answer == "A":
    return True
  elif b['follower_count'] > a['follower_count'] and answer == "B":
    return True
  else:
    return False
  
# inside game
def format_data(account):
  print(f"Compare A: {account['name']}, {account['description']}, from {account['country']}, {account['follower_count']}")

def game():
  print(art.logo)
  score = 0
  compare_a = random.choice(game_data.data)
  format_data(compare_a)
  
  print(art.vs)
  
  against_b = random.choice(game_data.data)
  if compare_a == against_b:
    against_b = random.choice(game_data.data)
  format_data(against_b)
  answer = input("Who has more followers? Type 'A' or 'B: ")
  result = check_answer(compare_a, against_b, answer)
  if result == True:
    clear()
    while result == True:
      score += 1
      print(art.logo)
      print(f"You're right! Current score: {score}")
      if against_b['follower_count'] > compare_a['follower_count']:
        compare_a = against_b
        against_b = random.choice(game_data.data)
        if compare_a == against_b:
          against_b = random.choice(game_data.data)
      else:
        against_b = random.choice(game_data.data)
        if compare_a == against_b:
          against_b = random.choice(game_data.data)
      format_data(compare_a)
      
      print(art.vs)
  
      format_data(against_b)
      answer = input("Who has more followers? Type 'A' or 'B: ")
      result = check_answer(compare_a, against_b, answer)
      clear()
  if result == False:
    clear()
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {score}")

keep_going = True
while keep_going == True:
  ask = input("Do you  want to play the Higher-Lower game?, Type 'yes' or 'no': ")
  if ask == 'yes':
    clear()
    game()
  else:
    keep_going = False
    