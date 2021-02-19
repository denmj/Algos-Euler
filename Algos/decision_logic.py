t = "You have no idea how to approach this problem."
opA = "Send an email to the TAs"
opB = "Go to office hours"
opC = "Post the problem online, there's no way I'll be caught"


def choice(text, optionA, optionB, optionC):
    print(text + "\n")
    print("A: " + opA + "\n" + "B: " + opB + "\n" + "C: " + opC + "\n")

    user_i = input("Enter: ")

    if user_i == 'A':
        print('A')
        return 'A'
    elif user_i == 'B':
        print('B')
        return 'B'
    elif user_i == 'C':
        print('C')
        return 'C'
    else:
        print("Something invalid, so default is A")
        return 'A'


def adventure_1():

    choice_1 = choice(t, opA, opB, opC)

    if choice_1 == 'A':
        print("A ->")
        choice_2 = choice(t, opA, opB, opC)
        if choice_2 == 'A':
            print("A -> A")
            print("GooD")
        elif choice_2 == 'C':
            print("A -> C")
            choice_3 = choice(t, opA, opB, opC)
            if choice_3 == 'A':
                print("A -> C -> A")
                print("Bad")
            elif choice_3 == 'B':
                print("A -> C -> B")
                choice_4 = choice(t, opA, opB, opC)
                if choice_4 in ["A", "B"]:
                    print("A -> C -> B -> " + choice_4)
                    print("Good")
                elif choice_4 == 'C':
                    print("A -> C -> B -> C")
                    print("Bad")
            elif choice_3 == 'C':
                print("A -> C -> C")
                print("Good")
        elif choice_2 == 'B':
            print("A -> B")
            choice_2_1 = choice(t, opA, opB, opC)
            if choice_2_1 in ["A", "B"]:
                print("A -> B -> " + choice_2_1)
                print("Good")
            elif choice_2_1 == "C":
                print("A -> B -> C")
                print("Bad")
    elif choice_1 == 'C':
        print("C ->")
        choice_1_1 = choice(t, opA, opB, opC)
        if choice_1_1 == 'A':
            print("C -> A")
            print("Bad")
        elif choice_1_1 == 'C':
            print("C -> C")
            print("Good")
        elif choice_1_1 == 'B':
            print("C -> B")
            choice_1_1_1 = choice(t, opA, opB, opC)
            if choice_1_1_1 in ["A", "B"]:
                print("C -> B ->" + choice_1_1_1)
                print("Good")
            elif choice_1_1_1 == 'C':
                print("C -> B -> C")
                print("Bad")
    elif choice_1 == 'B':
        print("B ->")
        print("Bad")


def adventure_2():
    state_counter = 1
    if state_counter == 1:
        choice_1 = choice(t, opA, opB, opC)
        if choice_1 == 'A':
            state_counter += 1
        elif choice_1 == 'C':
            state_counter += 2
        else:
            print("Bad")
    if state_counter == 2:
        choice_2 = choice(t, opA, opB, opC)
        if choice_2 == 'A':
            print("Good")
        elif choice_2 == 'C':
            state_counter += 1
        elif choice_2 == 'B':
            state_counter += 2
    if state_counter == 3:
        choice_3 = choice(t, opA, opB, opC)
        if choice_3 == 'A':
            print("Bad")
        elif choice_3 == 'C':
            print("Good")
        elif choice_3 == 'B':
            state_counter += 1
    if state_counter == 4:
        choice_4 = choice(t, opA, opB, opC)
        if choice_4 in ['A', 'B']:
            print("Good")
        elif choice_4 == 'C':
            print("Bad")


adventure_2()