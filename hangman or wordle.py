import random
from words import words
import string

def valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def wordle():
    word = valid_word(words)
    word_letters = set(word) #letters of the randomly picked word
    alphabet = set(string.ascii_uppercase) #the alphabet in uppercase
    used_l = set() #the letters already inputed by the user
    lives = 6
    
    while len(word_letters) > 0 and (lives > 0):
        print('You have used the following letters: ', ' '.join(used_l))
        word_prompt = [letter if letter in used_l else '-' for letter in word]
        print('Current word: ', ' '.join(word_prompt))
        user_l = input('Guess a letter: ').upper()
        
        if user_l in alphabet - used_l:
            used_l.add(user_l)
            if user_l in word_letters:
                word_letters.remove(user_l)
            else:
                print("WRONG GUESS! This litter is not in the word.\n")
                lives = lives-1
                print("You have ", lives, " lives left\n")
        elif user_l in used_l:
            print("You've already used this character! Please try again.")
        else:
            print("Invalid input!")
    if word_letters ==0:
        print("\n Yaay you've guessed the word")
        print("The word is ", word, "\n")
    else:
        print("You died! Please try again, or not, whatever\n")
        print("The word was ", word, ", idiot")
wordle()
consent = True
while(consent):
    c = input("Do you want to play again? Y/n\n").upper()
    if (c == 'Y') or (c == 'YES'):
        wordle()
    elif (c == 'N') or (c == 'NO'):
        break
        consent = False
    else:
        print("Invalid input! I said either input Y for yes or n for no! What's so hard about that?")
        
    
