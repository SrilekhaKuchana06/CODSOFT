import random
print("***** Play Time...! Let's play Rock Paper Scissors *****")
user_score = com_score = 0
options = ['rock','paper','scissors']
while True:
    print("*** ROCK PAPER SCISSORS ***")
    user_choice = input("Choose Rock/Paper/Scissors: ")
    com_choice = random.choice(options)
    print("Computer's choice: ",com_choice)
    if user_choice == 'rock':
        if com_choice == 'paper':
            print("Rock lost to paper! Computer wins! Try again?")
            com_score += 1
        elif com_choice == 'scissors':
            print("Rock beats Scissors! You win! Play again?")
            user_score += 1
        else:
            print("It's a Tie! Try again?")
    elif user_choice == 'paper':
        if com_choice == 'rock': 
            print("Paper beats Rock! You win! Play again?")
            user_score += 1
        elif com_choice == 'scissors':  
            print("Paper lost to Scissors! Computer wins! Try again?")
            com_score += 1
        else:
            print("It's a Tie! Try again?") 
    else:  
        if com_choice == 'rock': 
            print("Scissors lost to rock! Computer wins! Try again?")
            com_score += 1
        if com_choice == 'paper':
            print("Scissors beats Paper! You win! Play again?")
            user_score += 1
        else:
            print("It's a Tie! Try again?") 
    inp = input("Another round? (yes/no): ")
    if inp == 'yes':
        continue
    else:
        print("Your Score: ",user_score)
        print("Computer Score: ",com_score)
        if user_score > com_score:
            print("Hurray! You won the match")
        elif user_score == com_score:
            print("It's a Tie match")
        else:
            print("Computer won the match")
        print("***** THANK YOU *****")
        break
