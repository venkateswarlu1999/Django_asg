# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import hangman_images

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """it's check the taken latter in secret_word or not. if it is in the word return true otherwise return false"""
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True
        
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass




def get_guessed_word(secret_word, letters_guessed):
        """in this it check the all words in secret word to compare the letter gussed word is it in the secret word 
        it add to the gussed word and remove the one space other wise it gives equal spaces of secret word and finally it returns the guessed word  """
        guessed_word = ""
        for letter in secret_word:
          if letter in letters_guessed:
              guessed_word += letter
          else:
              guessed_word += "_"
          guessed_word += " "  
        return guessed_word.strip()

    
    # secret_word: string, the word the user is guessing
    # letters_guessed: list (of letters), which letters have been guessed so far
    # returns: string, comprised of letters, underscores (_), and spaces that represents
    #   which letters in secret_word have been guessed so far.
    
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass



def get_available_letters(letters_guessed):
        """first it wiil be created all alphabets in lower case. it will be check we guessed letteer in all letters is it in 
            it will be removed all letters and give the remain letters in available lettrs"""
        all_letters = string.ascii_lowercase
        available_letters = ""
        for letter in all_letters:
          if letter not in letters_guessed:
              available_letters += letter
        return available_letters
    # '''
    # letters_guessed: list (of letters), which letters have been guessed so far
    # returns: string (of letters), comprised of letters that represents which letters have not
    #   yet been guessed.
    # '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass
    
    

def hangman(secret_word):
    guesses_remaining = 6
    letters_guessed = []

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    """it will be give the spaces to the lenght of the secret word"""
    print("_"*len(secret_word))

    while True:
        """"it knows the how many guess we have"""
        print(f"You have {guesses_remaining} guesses left.")
        """it show the all alphabets in lower case as available letters"""
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        """it take the guess as user input and converts to the lowercase"""
        guess = input("Please guess a letter: ").lower()
        """it check the either you give the guss in alphabet or not. if is it not alpha it show the given msg"""
        if not guess.isalpha() or len(guess) != 1:
            print("Oops! That is not a valid letter. Please try again.")
            continue
        """it check your guess is already in gueesed or not. if is it already gueesed show the given msg"""
        if guess in letters_guessed:
            print("Oops! You've already guessed that letter. Please try again.")
            continue
        """if your guess is satisfy the above two cionditions it can add the letter gussed"""
        letters_guessed.append(guess)
        """if your guess in secret word show the given msg otherwise show the else block msg and lose the one guess from all gusees"""
        if guess in secret_word:
            print("Good guess!")
        else:
            print("Oops! That letter is not in my word.")
            guesses_remaining -= 1
        """it show the word in spacess"""
        print(f"Word: {get_guessed_word(secret_word, letters_guessed)}")
        print("-------------")

        if is_word_guessed(secret_word, letters_guessed):
            """if you guess all letters in the secret word within the guesses then it will be show the given msg and also secret word"""
            print("Congratulations, you won!")
            """here it calculate your marks as per below condition and stop the execution"""
            score = guesses_remaining * len(set(secret_word))
            print(f"Your total score for this game is: {score}")
            break

        if guesses_remaining == 0:
            """if your not guessing the secret word within the guesses it will show the given msg and stop the execution"""
            print(f"Sorry, you ran out of guesses. The word was {secret_word}.")
            break

  # '''
  #   secret_word: string, the secret word to guess.
    
  #   Starts up an interactive game of Hangman.
    
  #   * At the start of the game, let the user know how many 
  #     letters the secret_word contains and how many guesses s/he starts with.
      
  #   * The user should start with 6 guesses

  #   * Before each round, you should display to the user how many guesses
  #     s/he has left and the letters that the user has not yet guessed.
    
  #   * Ask the user to supply one guess per round. Remember to make
  #     sure that the user puts in a letter!
    
  #   * The user should receive feedback immediately after each guess 
  #     about whether their guess appears in the computer's word.

  #   * After each guess, you should display to the user the 
  #     partially guessed word so far.
    
  #   Follows the other limitations detailed in the problem write-up.
  #   '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


"""in this function it convert to the secreate word in to the spaces. it will be the same as per length"""
def match_with_gaps(my_word, other_word):
    if len(my_word) != len(other_word):
        return False
    
    for i in range(len(my_word)):
        if my_word[i] != '_' and my_word[i] != other_word[i]:
            return False
    
    return True

    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass


"""it will be show the possible matches. it will check filled word with other words in the words list 
   if match found it give the possible word from the words list"""
def show_possible_matches(my_word):
    matches_found = False
    for word in wordlist:
        if match_with_gaps(my_word, word):
            print(word, end=" ")
            matches_found = True
    
    if not matches_found:
        print("No matches found")

    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass

"""this function work same as before hangman function. in this some hints and conditions will be added"""
def hangman_with_hints(secret_word):
    """here its how many guess u have"""
    guesses_remaining = 6
    """here how many warnings u have"""
    warnings_remaining = 3
    """her it is empty list for guessed letters"""
    letters_guessed = []
    """her it is list contains vowels"""
    vowels = ['a', 'e', 'i', 'o', 'u']
    """here it show the greetings to the user"""
    print("Welcome to the game Hangman!")
    """here it show the msg what is the lenth of the secret word is given"""
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    """here it give the spaces to equal of secrect word letters"""
    print("_"*len(secret_word))
    """here whilee true it execute program in loop it's become flase"""
    while True:
        """it show the how many guessess you have"""
        print(f"You have {guesses_remaining} guesses left.")
        """it show the how many warnings you have"""
        print(f"You have {warnings_remaining} warnings left.")
        """it show the all letters are available in the smaller case"""
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        """it convert your input as lowercase letter"""
        guess = input("Please guess a letter: ").lower()
        """it check your input is not in alphabets and not in number"""
        if not guess.isalpha() or len(guess) != 1:
            """here below condition execute ur input as '*' then it check the all possibilites of matching words 
               in the words list with help of get_gussed_word function.if it there it show the output otherwise it show the not found msg"""
            if guess == '*':
                show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            else:
                """here you enter not alphabets and * then it will check your warnings it will be a zero then it remove one guss in your total guesses
                otherwise it will be remove one warning remining ur warnings"""
                if warnings_remaining > 0:
                    warnings_remaining -= 1
                    print("Oops! That is not a valid letter. You have", warnings_remaining, "warnings left:", get_guessed_word(secret_word, letters_guessed))
                else:
                    print("Oops! That is not a valid letter. You have no warnings left, so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                    guesses_remaining -= 1
            continue
        """here it check ur guess in alredy guessed letters or not. if it is in alredy_guessed then u can lose one guess
           otherwise it added to the letter_guessed list"""
        if guess in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! You've already guessed that letter. You have", warnings_remaining, "warnings left:", get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! You've already guessed that letter. You have no warnings left, so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                guesses_remaining -= 1
            continue

        letters_guessed.append(guess)
        """here it check the guess letter in the secret word or not.if letter in secret word it show the good guess msg
        other wise it check is it in vowels or not if is in vowels u will lose two guesses at a time otherwise u can lose one guess"""
        if guess in secret_word:
            print("Good guess!")
        else:
            if guess in vowels:
                print("Oops! That vowel is not in my word. You lose two guesses.")
                guesses_remaining -= 2
            else:
                print("Oops! That letter is not in my word.")
                guesses_remaining -= 1
        """here it show the word with filled your guessed words it will be in the secret word"""
        print(f"Word: {get_guessed_word(secret_word, letters_guessed)}")
        """here it show the list of images based on it index number. it index willbe ur remaining_guesses """
        print(hangman_images.stages[guesses_remaining])
        """here it show the below msg if you can guss the secret word"""
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you won!")
            """here it will ganarete your score based on below condition"""
            score = guesses_remaining * len(set(secret_word))
            print(f"Your total score for this game is: {score}")
            break
        """here it show the secret word if you can guess all letters in secret word in ur guesses or u will lose the all guesses"""
        if guesses_remaining == 0:
            print(f"Sorry, you ran out of guesses. The word was {secret_word}.")
            break
        



    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

# l=['venkat','malli','vishnu','krishna','aruna']
if __name__ == "__main__":
#     pass

# #     # To test part 2, comment out the pass line above and
# #     # uncomment the following two lines.
    
    # secret_word = choose_word(l)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    """here it is excute the above fuction. it is function call of above all functions"""
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
