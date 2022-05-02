import random
from tkinter import END,messagebox
from socket import *
import threading



# global variables
userWins = 0
computerWins = 0
totalWinsCamp = 0
totalWinsUsr = 0
SuccessRate = 0
biggestRate = 0
data = ""



class RockScissorsPaper(object):
    def __init__(self):
        self.computer_option = random.choice(['r', 's', 'p'])

    def __call__(self, user_option): # checking who won the round
        global computerWins
        global userWins

        if self.computer_option == user_option:
            return "It's a draw\n"

        elif self.computer_option == 's' and user_option == 'p':
            computerWins += 1
            y = "computer won this round\n"
            return is_end(y)

        elif self.computer_option == 'r' and user_option == 's':
            computerWins += 1
            y = "computer won this round\n"
            return is_end(y)

        elif self.computer_option == 'p' and user_option == 'r':
            computerWins += 1
            y = "computer won this round\n"
            return is_end(y)

        else:
           userWins +=1
           y = "user won this round\n"
           return is_end(y)



def activeServer(): # activating the server
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(("", 1234))
    server.listen(100)

    while True:
        client, addr = server.accept()
        t = threading.Thread(target=BiggestRate, args=(client,))
        t.start()



def check_winner(user_option,Rtxt): # getting here after pressing "SUBMIT" button
    if user_option != 'r' and user_option != 's' and user_option != 'p':
        Rtxt.insert(END, "\nYou have selected a wrong value \nPlease select again ( [r] / [s] / [p] )\n")
    else:
        rsp = RockScissorsPaper()
        Rtxt.insert(END, rsp(user_option))



def BiggestRate(client): # saving the biggest rate
    global data
    global biggestRate

    try:
        data = eval(client.recv(2048).decode())
    except Exception as e:
        messagebox.showinfo("Error", "You must play at least on game before saving your rate")

    if data > biggestRate and data != 101:
        biggestRate = data

    if data == 101:
        biggestRate = str(biggestRate)
        client.sendall(biggestRate.encode())
        biggestRate = eval(biggestRate)

    client.close()



def is_end(y): # checking if the game end, if it does so who won the game
    global totalWinsCamp
    global totalWinsUsr
    global userWins
    global computerWins

    if userWins == 3:
        totalWinsUsr += 1
        userWins = 0
        computerWins = 0
        y = "\nuser won the game\n""Status: computer-{0} | user-{1}\n\n\n".format(totalWinsCamp, totalWinsUsr)
        return y

    elif computerWins == 3:
        totalWinsCamp += 1
        userWins = 0
        computerWins = 0
        y = "\ncomputer won the game\nStatus: computer-{0} | user-{1}\n\n\n".format(totalWinsCamp, totalWinsUsr)
        return y

    return y



def showBest(Rtxt): # getting here after pressing "how the best success rate" button, displaying the user best rate
    client1 = socket(AF_INET, SOCK_STREAM)
    client1.connect(("127.0.0.1", 1234))

    client1.sendall("101".encode())
    Rtxt.insert(END, "Your best success rate is: {0}%\n\n\n".format(client1.recv(2048).decode()))



def exit(Rtop):  # getting here after pressing "Exit and save your success rate" button, saving user rate & exit
    client2 = socket(AF_INET, SOCK_STREAM)
    client2.connect(("127.0.0.1", 1234))

    global totalWinsCamp
    global totalWinsUsr
    global SuccessRate

    try:
        SuccessRate = (totalWinsUsr / (totalWinsUsr + totalWinsCamp)) * 100
        SuccessRate = str(SuccessRate)
        client2.sendall(SuccessRate.encode())
    except:
        pass

    totalWinsCamp = 0
    totalWinsUsr = 0

    Rtop.destroy()