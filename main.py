############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

from art import logo
# from replit import clear
import random
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(these_cards):
  x=random.choice(cards)
  these_cards.append(x)

def calculate_score(these_cards):
  this_sum = 0
  is_ace = 0
  for x in these_cards:
    this_sum += x
    if x == 11:
      is_ace += 1
  for x in range(is_ace):
    if this_sum > 21:
      this_sum -= 10
  return this_sum

def endgame():
    if computer_score > 21 and user_score > 21:
      print("\nYou both busted!  It's a push!")
      return
    elif computer_score > 21:
      print('\nComputer busts!  You win!')
      return
    elif user_score > 21:
      print("\nBusted!  You lose!")
      return
    elif user_score == 21 and computer_score == 21:
      print("\nBoth 21!  It's a push!")
      return
    elif user_score == 21 and len(user_cards) == 2:
      print("\nBlackJack!!  You win!")
      return
    elif user_score == 21:
      print("\nYou got 21!!  You win!")
      return
    elif computer_score == 21:
      print("\nComputer gets 21.  You lose.")
      return 
    elif user_score == computer_score:
      print("\nTie game.  That is a push")
      return
    elif user_score < computer_score:
      print("\nComputer wins.  Sorry, loser.")
      return
    elif user_score > computer_score:
      print("\nYour score is higher!  You win!!!")
      return
    

game_on = True
while game_on:
  yeah = input("\nDo you want to play a game of Blackjack?: ").lower()
  if yeah == 'n':
    game_on = False
    break

  user_cards = []
  computer_cards = []
  user_score = 0
  computer_score = 0
  
  deal_card(user_cards)
  deal_card(user_cards)
  deal_card(computer_cards)
  deal_card(computer_cards)

  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)

  print(f"Your cards: {user_cards}, current score: {user_score}")
  print(f"Computer card showing: {computer_cards[0]}")

  # Let the player take more cards
  if user_score < 21:
    one_more = True
  else:
    one_more = False
  while one_more == True:
    if user_score > 20:
      one_more = False
      break
    should_pass = input("\nDo you want another card?: ").lower()
    if should_pass == "n":
      one_more = False
      break
    else:
      deal_card(user_cards)
      user_score = calculate_score(user_cards)
      print(f"Your cards: {user_cards}, current score: {user_score}")
      print(f"Computer card showing: {computer_cards[0]}")
  # End of Let the player take more cards

  # Decide if computer gets more cards
  while computer_score < 17 and user_score < 21:
    deal_card(computer_cards)
    computer_score = calculate_score(computer_cards)
    print(f"\nYour cards: {user_cards}, current score: {user_score}")
    print(f"Computer cards: {computer_cards}, current score: {computer_score}")

  # Decide the winner!!
  print(f"\nYour final cards: {user_cards}, current score: {user_score}")
  print(f"Computer final cards: {computer_cards}, current score: {computer_score}")
  endgame()



print('Game Over!')
    
