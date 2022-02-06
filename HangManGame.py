
def list2string(x):
    st = ""
    for i in range(len(x)):
        st+=x[i]+" "
    return st


def HangMan_Game(y): 

    print("Try to guess the word by suggesting letters with a limit of 6 fails!\n")
    x = []
    for i in range(len(y)):
        x.append(y[i])

    fails = 0
    answer = ["_"] * (len(x))
    end = ["0"] * (len(x))


    print("Type a letter: ")
    letter = str(input())

    while fails < 5:

        if letter in x:
            for i in range(len(x)):
                if letter == x[i]:
                    answer[i] = letter
                    x[i] = "0"
                    
                    if x == end:
                        fails = 10
            print(list2string(answer))

        else:
            fails += 1
            print("You got it wrong for the %dº time. Try Again!" %(fails))

        if x !=end:
            print("Type a letter: ")
            letter = str(input())

    if fails == 5:
        print("You died.. Ups!")
    else:
        print("You got the right word!: " + list2string(answer) )
