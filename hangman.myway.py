



import random
import string
from words import words
print("""
██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝

""")
from stages import hangman_stages


rules = open("rules.txt","r")
print(rules.read())
rules.close

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word.upper()

word = get_valid_word(words)

def hangman(word):
    final_word = word
    user_word_list = []
    word_list = list(word)
    word_letters = set(word)
    used_letters = set()
    alphabet = set(string.ascii_letters)
    guesses = 11
    stage = -1
    run_out_of_guesses = False
    
    #adding place-holders in the user's word list
    for word in word_list:
        user_word_list.append("-")
    print(user_word_list)
    
    
    while len(word_letters) > 0 and guesses > 0:
        user_letter = input("\n\nGuess a letter").upper()
        if user_letter in alphabet - used_letters: #checking if the letter inputted is available
            used_letters.add(user_letter)
            
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("\n\n\nCorrect letter")
                print("--You have {} guesses left--".format(guesses))
                
                if guesses == 11:
                    print("")
                else:
                    print(hangman_stages[stage])
            
                
                #update word list (for the user to see)
                count = word_list.count(user_letter)
                index = 0
                temp_index = 0
                if count > 1:
                    index = word_list.index(user_letter)
                    user_word_list[index] = word_list[index]
                    count -= 1
                    while count > 0:
                        index += 1
                        temp_index = word_list.index(user_letter, index)
                        user_word_list[temp_index] = word_list[temp_index]
                        count -= 1
                        print(user_word_list)

                        
                else:
                    index = word_list.index(user_letter)
                    user_word_list[index] = word_list[index]
                    if guesses == 11:
                        print("")
                        print(user_word_list)
                    else:
                        print(user_word_list)
                    

            else:
                print("\n\n\nIncorrect guess")
                print("--You have {} guesses left--".format(guesses-1))
                if guesses > 0:
                    stage += 1
                    print(hangman_stages[stage])
                    guesses -= 1
                print(user_word_list)

                
        
        
        elif user_letter in used_letters:
            print("Letter already guessed. Try again")  
        else:
            print("Invalid character. Try again")
     
    run_out_of_guesses = True if guesses == 0 else False
    if run_out_of_guesses == True:
        print("\n\n[GAME OVER] \n\nUnfortunately you have run out of guesses and have not correctly guessed the word")
        print("The word was {} !".format(final_word.lower()))
    elif run_out_of_guesses == False and len(word_letters) == 0:
        print("\n\n[WELL DONE] \n\nYou've succesfully guessed that the word was {}!".format(final_word.lower()))
        


    

hangman(word)
