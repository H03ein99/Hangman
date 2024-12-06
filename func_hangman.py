from random import choice
from time import sleep


def check(answer, guess, char):
    result = ""
    for i in range(len(answer)):
        if answer[i] == char:
            result += char
        else:
            result += guess[i]
    return result


animals = ("Giraffe,Lion,Monkey,Shark,Fish"
           ",Tiger,Bee,Gorilla,Kangaroo,"
           "Snake,Horse,Dog,Cat,Frog,Goat").upper().split(",")

name = input("what is your name? ").capitalize()
print("Hello there {}\nlets play HANGMAN game about animal's names!!!\n".format(name))
answer = choice(animals)
guess = "_" * len(answer)
chances = 5
sleep(1)
print(8 * "-", "Game Started", 8 * "-")
print(guess)
while True:
    char = input("guess a character: ").upper()
    new_guess = check(answer, guess, char)
    if new_guess == guess:
        chances -= 1
        print("Wrong!!! {} chances left".format(chances))
    guess = new_guess
    print(guess)
    if guess == answer:
        print("Congrats {} You Won :))) ".format(name))
        break
    elif chances == 0:
        print("Game Over {}\n"
              "the right answer was {}\n"
              "maybe next time ^_^".format(name, answer))
        break
    sleep(.5)
print(10 * "-", "The End", 10 * "-")