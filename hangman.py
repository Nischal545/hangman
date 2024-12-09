import random


words = ["apple", "mango", "kiwi", "strawberry", "peach", "cherry", "lychee", "muskmelon", "watermelon", "coconut", "apricot", "grape", "lemon", "papaya", "banana"]


someWord = random.choice(words) 
print(someWord)
word_len = len(someWord)
chances = word_len + 2


def is_valid_guess(letter):
    if(not letter.isalpha()) or not letter.islower():
        print("You either entered a non-alphabetical character or you entered capital letter.")
        return False
    elif(len(letter)!=1):
        
        print("Please enter a single letter")
        return False
    return True


def hangman(chances, someWord):
    print("Guess the word: ")
    correctGuesses = set()
    current_state = ["_" for _ in someWord]
    
    print(" ".join(current_state))
    
    print(f"You have got {chances} chances left")
    
    # while chances!=0:
    while chances>0:
        print(f"Number of letters: {word_len}")
        guesses = str(input("Enter a letter: "))

        if not is_valid_guess(guesses):
            continue

        if guesses in someWord:
            print("Correct")
            for index, value in enumerate(someWord):
                if value == guesses:
                    current_state[index] = guesses
                correctGuesses.add(guesses)
        else:
            print("Wrong guess!")
        print(" ".join(current_state))
        print(f"Chances left: {chances}")

        if("_" not in current_state):
            print(f"Congratulations! You guessed the word: {someWord}")
            break   

    if("_" in current_state):
        print(f"Game Over! The correct word was: {someWord}")    

hangman(chances, someWord) 
print("Thank You for playing our game")
    


    


