from tkinter import Tk, Toplevel, Label, Button, Entry, Text
import random
import RockScissorsPaper, GuessTheNumber
import threading


# "guess the number" window
def GTN_window():
   Gtop = Toplevel()
   Gtop.geometry("600x400")
   Gtop.title("Guess The Number")
   Gtop.iconbitmap('arcade.ico')
   Gtop.resizable(False, False)
   randoNum = random.randint(1, 1000)

   Glbl1 = Label(Gtop, text="Welcome to Guess The Number game!\n\nYou need to guess a number between 1 to 1000:", font=10)
   Glbl1.place(x=130, y=10)

   Glbl2 = Label(Gtop, text="Your guess:")
   Glbl2.place(x=20, y=100)

   GE1 = Entry(Gtop, width=10, bd=5)
   GE1.place(x=100, y=100)

   Gtxt = Text(Gtop, width=70, height=13)
   Gtxt.place(x=15, y=150)

   Gbtn1 = Button(Gtop, text="Submit", bd=3, command=lambda: GuessTheNumber.guess(eval(GE1.get()),randoNum,Gtxt))
   Gbtn1.place(x=180, y=99)

   Gbtn2 = Button(Gtop, text="Show record", bd=3, command=lambda: GuessTheNumber.show_record(Gtxt))
   Gbtn2.place(x=500, y=365)


# "rock-scissors-paper" window
def RSP_window():
   Rtop = Toplevel()
   Rtop.geometry("600x400")
   Rtop.title("Rock-Scissors-Paper")
   Rtop.iconbitmap('arcade.ico')
   Rtop.resizable(False, False)

   Rlbl1 = Label(Rtop, text="Welcome to Rock-Scissors-Paper game!\n\nTry to win the computer, the first who achieve 3 wins is the winner\n\n", font=10)
   Rlbl1.place(x=70, y=20)

   Glbl2 = Label(Rtop, text="[r]ock / [s]cissors / [p]aper  |  Insert  r / s / p  >")
   Glbl2.place(x=20, y=100)

   RE1 = Entry(Rtop, width=10, bd=5)
   RE1.place(x=270, y=100)

   Rtxt = Text(Rtop, width=70, height=12)
   Rtxt.place(x=15, y=150)

   Rbtn1 = Button(Rtop, text="Submit", bd=3, command=lambda:RockScissorsPaper.check_winner(RE1.get(),Rtxt))
   Rbtn1.place(x=350, y=99)

   Rbtn2 = Button(Rtop, text="Show the best success rate", bd=3, command=lambda:RockScissorsPaper.showBest(Rtxt,))
   Rbtn2.place(x=120, y=360)

   Rbtn3 = Button(Rtop, text="Exit and save your success rate", bd=3, command=lambda:RockScissorsPaper.exit(Rtop))
   Rbtn3.place(x=320, y=360)




if __name__ == '__main__':
   # creating a server for "rock-scissors-paper" game in order to save the user's best success Rate
   t = threading.Thread(target=RockScissorsPaper.activeServer)
   t.start()

   # main window
   window = Tk()
   window.title('Games World')
   window.geometry("700x300")
   window.iconbitmap('arcade.ico')
   window.resizable(False, False)

   lbl1 = Label (window, text="Welcome to the Games World!", font=50)
   lbl1.place(x=240, y=50)

   lbl2 = Label (window, text="What is your game?", font=50)
   lbl2.place(x=280, y=100)

   btn1 = Button (window,text = "Guess The Number" ,bd=5, font=50, command=GTN_window)
   btn1.place(x=70, y=200)

   btn2 = Button (window,text = "Rock-Scissors-Paper" ,bd=5, font=50, command=RSP_window)
   btn2.place(x=450, y=200)

   window.mainloop()