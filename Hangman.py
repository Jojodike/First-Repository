import random
from words import words 
random.choice(words)
import string

def fetch_word(words):
    word = random.choice(words) # chooses random word from the list 
    while ' ' in word or '-' in word:
        word = random.choice(words) 
    
    return word.upper()

def hangman():
    word = fetch_word(words)
    alphabet = set(string.ascii_uppercase)
    word_letters = set(word) # letters in the random word
    used_letters = set() # letters that the user has guessed
    
    lives = 8 # number of lives the user has
    
    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #letters used to guess 
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        
        #current hangman word
        word_list= [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        user_letter = input('Enter a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                lives = lives - 1 # lose life if wrong
                print('Letter not in word.')
                
        elif user_letter in used_letters:
            print('Letter already used. Choose again.')
        
        else:
            print('Invalid letter. Try again.')   
    
    # gets here when len(word_letters) == 0 OR when lives  == 0 
    if lives == 0:
        print('Sorry, gotta hang you. The word was', word)
    else:
        print('You guessd right, the word is', word, '!')
    
hangman()