
# the secret word player is trying to guess
secretWord = "Superman"
lettersGuessed = ""

# The amount a player can get wrong 
failureCount = 6 

#loop through max tunr count, at most 6 
while failureCount > 0:

    # get a guess from the player 
    guess = input("Enter a letter: ")

     #check guess 
    if guess in secretWord:
        print(f"Correct! There is one or more {guess} in the secret word.")
    
    #if wrong increase the count 
    else:
        failureCount -= 1
        print(f"Incorrect. There are no {guess} in the secret word. {failureCount} turn(s) left.")

    lettersGuessed = lettersGuessed + guess
    wrongLetterCount = 0

    for letter in secretWord:
        if letter in lettersGuessed:
            print(f"{letter}", end= "")
        else:
            print("_", end= "")
            wrongLetterCount += 1
    print("")

    #if there were no wrong letters, then the player wins 
    if wrongLetterCount == 0:
        print(f"Congrats! The secret word was: {secretWord}. You won!")
        break

else:
    print("Sorry you didn't win, try again. ")

    














#print out correct letters 


#if all correct, break through game 