from random import choice

class Hangman:
    __turn = []
    __loosers = []
    __winners = []
    game_round = 0
    __animals = ("Giraffe,Lion,Monkey,Shark,Fish"
                 ",Tiger,Bee,Gorilla,Kangaroo,"
                 "Snake,Horse,Dog,Cat,Frog,Goat").upper().split(",")

    def __init__(self, name):
        self.name = name.capitalize()
        self.__chances = 3
        self.__answer = choice(Hangman.__animals)
        self.guess = "_" * len(self.__answer)
        print("player {} added to the game".format(self.name))
        # print("answer is  {}".format(self.__answer))

    @classmethod
    def add_user(cls):
        question = "enter player's name: "
        cls.__turn.append(Hangman(input(question)))
    def get_char(self):  # to get a char from user
        print(self.guess, end=": ")
        self.char = input("{} enter a char: ".format(self.name)).upper()

    def reduce_chance(self):  # reduce chance by one if chance reaches 1 player looses and removes from players list
        self.__chances -= 1
        print("Wrong! {} has {} chance left".format(self.name, self.__chances))
        if self.__chances == 0:
            print("player {} lost the game!!".format(self.name))
            Hangman.__loosers.append(Hangman.__turn.pop(Hangman.__turn.index(self)))

    def check_guess(self):
        result = ""
        for i in range(len(self.__answer)):
            if self.__answer[i] == self.char:
                result += self.char
            else:
                result += self.guess[i]
        return result

    def if_user_wins(self):
        if self.guess == self.__answer:
            Hangman.__winners.append(Hangman.__turn.pop(Hangman.__turn.index(self)))

    @classmethod
    def one_round(cls):
        Hangman.game_round += 1
        print("-" * 5, "round {} started".format(cls.game_round), "-" * 5)
        for player in cls.__turn:
            player.get_char()
            player.new_guess = player.check_guess()
            print(player.new_guess)
            if player.new_guess == player.guess:
                player.reduce_chance()
            else:
                player.guess = player.new_guess
            player.if_user_wins()

    @classmethod
    def launcher(cls):
        status = False
        while not status:
            order = cls.handler()
            if order == 1:
                cls.add_user()
            elif order == 2:
                status = True
        while status:
            cls.one_round()
            if len(cls.__turn) == 0:
                status = False
        cls.show_results()


    @classmethod
    def show_results(cls):
        print("_" * 20, "\nresults:\n")
        if len(cls.__winners) != 0:
            print("~" * len(cls.__winners) * 20)
            print("winners are: ", end=" ")
            for player in cls.__winners:
                print(player.name, end=" ")
            print("\n",end="")
            print("~" * len(cls.__winners) * 20)
        else:
            print("Nobody could win the game")
        if len(cls.__loosers) != 0:
            print("Answer for loosers: ")
            for player in cls.__loosers:
                print(player.name, " : ", player.__answer)
        print("=" * 5, "The End", "=" * 5)

    @classmethod
    def handler(cls):
        order = input("add/start: ").lower()
        if order == "add":
            return 1
        elif order == "start":
            return 2
        else:
            print("enter add to add a user or start to start the game")


Hangman.launcher()


