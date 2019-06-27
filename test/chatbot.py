def valid(answer):
    options = ["yes", "Yes", "yeah", "si", "YES", "ok", "okay", "OK", "sure"]
    for a in options:
        if answer == a:
            return True

def intro():
    answer1 = input('whats ur name? ')
    print (answer1, ' is a cool name. I am chattybot.')
def animil():
    ans8 = input("what's your favorite animal?")
    print(" oh....... that sux!!!!!!! I hate " + ans8)
def joke():
    telljoke = input("Do you want to hear a joke? ")
    if valid(telljoke):
        ans2 = input('why did the robot get angry so often ')
        print ('because people kept ppushing its buttons')
        ans3 = input('do you want to hear another joke? ')
        if valid(ans3):
            ans4 = input('why did the chatbot stop talking to u? ')
            print(". . .")
def fortune():
    fort = input("you want to know your fortune?")
    if valid(fort):
        print("you are not illiterate")
        ans5 = input("do you want to hear another fortune? ")
        print("your problems got bigger think of what you done....")

def rps():
    ansgame= input('do you want to play rock paper scissors? ')
    if valid(ansgame):
        ans6 = input('choose rock, paper or scissors ')
        if ans6 == "rock":
                print('i chose paper. i win')
        if ans6 == "scissors":
                print ('i chose rock. i win')
        if ans6 == "paper":
                print ('i chose scissors. i win')

def main():
    while True:
        intro()
        animil()
        joke()
        fortune()
        rps()
        ans7 = input('would you like to keep talking to me? ')
        if valid(ans7):
            pass
        else:
            quit()




#def joke()




# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()