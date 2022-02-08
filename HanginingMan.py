import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word that doesnt repeat
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the usser has guessed
    
    lives = 6

    while len(word_letters)> 0 and lives > 0:
        #letters used
        print('You have', lives, ' lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is 
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1 # Takes away a life if wrong
        
        elif user_letter in used_letters:
            print('You have already used that caracter. Please try again.')
        
        else:
            print('Invalid character! Please try again.')

hangman()
