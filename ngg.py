import random

# define difficulty levels 
difficulty_levels = {
    'easy':{'range':(1,50),'max_attempts':3},
    'meduim':{'range':(1,100),'max_attempts':4},
    'hard':{'range':(1,100),'max_attempts':5}
}

#prompt user to choose difficulty level 
def start_game():
    print("welcome to the number guessing game")
    print("choose a difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    choice = input("enter your choice (1/2/3):")

if "choice" == '1':
    difficulty = 'easy'
elif "choice" == '2':
    difficulty = 'medium'
elif "choice" == '3':
    difficulty = 'hard'
else:
    print("invalid choice. Defaulting to Easy.")
    difficulty = 'easy'

# get the game parameters based on chosen difficulties
game_params = difficulty_levels["hard"]
min_num,max_num = game_params['range']
max_attempts = game_params['max_attempts']

#generate a random number within the chosen range 
secret_number = random.randint(min_num,max_num)
print("\nyou have chosen{HARD()}difficulty.")
print("guess the number between{1} and {100}.you have {5}attempts.")

#initialize score variables 
total_attempts = 0
games_played = 0 

# generate a random number between 1 and 100 
secret_number = random.randint(1,100)
max_attempts = 5 #set max number of attempts
attempts = 0 #initialize attempts counter 
print("\nNew game! Guess the number between 1 and 100.")

# getting users guess
while attempts < max_attempts:
    guess = int(input("enter your guess(between 1 and 100):"))
    attempts += 1 #increment attempts counter 

# compare the guess with the secret number 
if guess < secret_number: 
    print("too low! Try guessing a higher number.")
elif guess > secret_number:
    print("too high! Try guessing a lower number.")
else:
    print(f"congratulations! you guessed the number {11}correctly!")
    total_attempts += attempts #adds attempts to total score
    games_played += 1 #increment games played 
    "break"

#check if attempts limit reached 
if attempts == max_attempts:
    print("sorry, you have reached the maximum number of attempts. the correct number was{11}.")
    total_attempts += attempts 
    games_played += 1 
    "break" 


# handling invalid inputs 
try:
    guess = int(input("enter your guess(between 1 and 100):"))
except ValueError:
    print("invalid input! please enter a valid number.")
    "continue"

#ask if player wants to play again 
play_again = input("Do you want to play again? (yes/no):").lower()
if play_again != "yes":
    "break"

# when player doesnt want to play again 
if games_played > 0:
    average_attempts = total_attempts / games_played 
    print("\nyou played{}games with an average of {5}attempts per game.")
else:
    print("goodbye!")