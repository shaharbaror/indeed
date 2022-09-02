import random
import sys

#HANGMAN_ASCII_ART = (" _    _ \n| |  | |\n| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __ \n|  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ \n| |  | | (_| | | | | (_| | | | | | | (_| | | | | \n|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|\n                     __/ |\n                    |___/")
MAX_TRIES = 6

#print ("Welcome to the game Hangman","\n",HANGMAN_ASCII_ART ,"\n" , MAX_TRIES)

path1 = "./names.txt"
path2 = 'hangman'

num1 = (random.randint(0,6))
options = (open(path2,"r").read().split('split'))
wordBank = (open("names","r").read().split('\n'))
old_letters_guessed = ["-"]
right_letters = []

secretWord = wordBank[num1]




def check_win(secretWord, old_letters_guessed):
    counter = 0
    for x in secretWord:
        for y in old_letters_guessed:
            if x==y:
                counter +=1
    if len(secretWord) == counter:
        return True
    else:
        return False



def show_hidden_word(secret_word, old_letters_guessed) :
    showWords = ""

    #shows the numbers missing
    for x in secret_word:
        isWord = False
        for y in old_letters_guessed:
            if x == y:
                showWords = showWords + y
                isWord = True
                break;
        if not isWord:
            showWords = showWords + "_"


    print(showWords)
    print(old_letters_guessed)

def try_update_letter_guessed(letter_guessed, old_letters_guessed ):
    for x in old_letters_guessed:
        if x == letter_guessed:
            return False
        else:
            continue
    old_letters_guessed.append(letter_guessed)
    return True

def isRight(secretWord,userInput):
    for x in secretWord:
        if x == userInput:
            return True
    return False

#start action code




show_hidden_word(secretWord, old_letters_guessed)

print(options[0])
def main():
    for i in range(MAX_TRIES):

        userInput = input("Enter a letter: ")

        while not try_update_letter_guessed(userInput, old_letters_guessed):
            print("X")
            userInput = input("Enter a letter: ")

        while isRight(secretWord, userInput):
            while not try_update_letter_guessed(userInput, old_letters_guessed):
                print("X")
                userInput = input("Enter a letter: ")

        #print(MAX_TRIES-i -1)

            show_hidden_word(secretWord, old_letters_guessed)
            if check_win(secretWord, old_letters_guessed):
                print("You Win!")
                return
            userInput = input("Enter a letter: ")
        print(options[i+1])
        show_hidden_word(secretWord, old_letters_guessed)


if __name__ == "__main__":
    main()
    if not check_win(secretWord,old_letters_guessed):
        print("You Lose")
#try_update_letter_guessed("i",old_letters_guessed)
#show_hidden_word(secretWord, old_letters_guessed)




