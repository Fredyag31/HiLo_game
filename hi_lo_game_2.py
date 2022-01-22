import random

guessesTaken = 0 

print('Hello! I am going to show you a card, guess whether the next card is higher or lower, get four in a row to win!')

number = random.randint(1, 12)

#five variables for five cards, all random cards between 1 and 12

print('Well I am thinking of a card between 1 and 12, the first number is:')
print (number) #shows them first card

guess = input('Take a guess, is the next card higher or lower? Please enter either "h" or "l".')

while guessesTaken <= 4: #limit number of guesses to make game less than 4 to win?

    if guessesTaken == 4:
        print("You win")
        break
    else:
        nextnumber = random.randint(1,12)
        print(nextnumber)

        if guess == "h" and nextnumber <= number:
            print ("you lose")
            break
        elif guess == "l" and nextnumber >= number:
            print ("you lose")
            break
        else:
            guess = input("the card was" + str(nextnumber) + "is the next card higher or lower?")

        guessesTaken += 1 #increment guesses taken