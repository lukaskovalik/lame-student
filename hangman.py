#THE HANGMAN!
import random

def wordToGuess():
    slovicka = ['hrad', 'doska', 'svetlo', 'prievan', 'nintendo', 'abrakadabra']
    slovo = random.choice(slovicka)
    return slovo

def userInput():
    while True:
        pismeno = input("Zadaj pismeno: ").lower()
        if pismeno.isalpha() == True:
            return pismeno
        elif pismeno.isalpha() == False:
            print("Hadanka obsahuje iba pismena, zadaj pismeno!")
            continue
        return pismeno

guess = wordToGuess()
lives = 6 # hrac ma 6 pokusov
guessedLetters = []

while lives > 0:
    guessedWord = ""
    for letter in guess:
        if letter in guessedLetters:
            guessedWord += letter
        else:
            guessedWord += "_"
    print("Hadaj slovo: ", guessedWord)

    if guess == guessedWord:
        print("Uhadol si slovo. Gratulujem!")
        break

    userInputLetter = userInput()
    if userInputLetter in guessedLetters:
        print("Toto pismeno si uz hadaj, hadaj znova.")
        continue

    guessedLetters.append(userInputLetter)

    if userInputLetter not in guess:
        lives -= 1
        print(f"Neuhadol si pismeno. Zostavajucich pokusov: {lives} ")


    if lives == 0:
        print("Prehral si, slovo si neuhadol")
        break






