import random
import string 
from hangman_visual import *
from words import words

def get_valid_word(words):
    word = random.choice(words) # randomly chooses word from list
    while '-' in word or ' ' in word: # chooses a different word if previous chosen word has '-' or ' '
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words).upper() # chooses word
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user guessed

    lives = 6

    print("\n Let's play Hangman!")

    # getting user input 
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print("__________________________________________________________________________ \n")
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters)) # ' '.join(['a', 'b', 'cd']) --> 'a b cd'

        # what current word is (ex: W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word] 
        print(hangman_visual[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper() 
        if user_letter in alphabet - used_letters: # user's guess is not already in used_letters
            used_letters.add(user_letter) # adds the user's guess into used_letters
            if user_letter in word_letters: # if user's guess is in the word then remove that letter from the word's letter list
                word_letters.remove(user_letter)
            
            else:
                lives = lives - 1 # takes away a life if wrong
                print('Sorry, this letter is not in the word. Please try again.') 
        
        elif user_letter in used_letters: # if user already guessed that letter, print this statement
            print('You have already used that letter. Please try again.')

        else: # if user inputs a non-alphabet character
            print('Not a valid letter. Please try again.')
        
        print("__________________________________________________________________________ \n")

    # when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(hangman_visual[lives])
        print('You died! The word was', word, '.')
    else:
        print('Congratulations! You guessed the word', word, '!!!')

hangman()