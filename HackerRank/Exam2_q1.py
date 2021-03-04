import random


def player_pic():
    input_user = input("Nuber betwee 0 and 10: ")
    return input_user


def ai_pic():

    return random.randint(0, 10)



def func_1():
    game = True
    while game:

        play_p = player_pic()

        if play_p == 'q':
            break

        if 0 <= int(play_p) <= 10:
            print(play_p)

            ai_move = ai_pic()

            if ai_move > int(play_p):
                print("AI won, you guessed {} , and AI's number is {}".format(play_p, ai_move))
            if ai_move == int(play_p):
                print("Tie, you guessed {} , and AI's number is {}".format(play_p, ai_move))
            if ai_move < int(play_p):
                print("You won, you guessed {} , and AI's number is {}".format(play_p, ai_move))
        else:
            print("incorrect number")


def func_0():
    print("Who needs loop?")
    print("Who needs loop?")
    print("Who needs loop?")
    print("Who needs loop?")
    print("Who needs loop?")


def func_10():
    print("Who needs loop?")
    func_0()
    func_0()
    func_0()
    func_0()
    func_0()


def func_20():
    func_10()
    func_10()
    func_10()
    func_10()

func_20()