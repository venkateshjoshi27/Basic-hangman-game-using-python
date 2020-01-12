import random as rd
words = ['awkward','banjo','bagpipes','bungler','croquet','dwarves','fishhook','gazebo'
         ,'haiku','jiffy','unzip','zombie','wildebeest','twelfth','memento']
word = rd.choice(words)
turn = 12
guesses = ''
while turn>0:
    counter = len(word)
    for char in word:
        if char in guesses:
            print(char)
            counter -=1
            if counter == 0:
                print("You win")
                exit()
        else:
            print("_")
    guess = input("Enter a character")
    guesses +=guess
    if guess not in word:
        print("Galat")
        turn = turn-1
    if turn == 0:
        print("You Loose")
