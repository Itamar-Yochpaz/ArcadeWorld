from tkinter import END


# global variables
tries = 0
oldRecord = 0



class GuessTheNumber(object):
    def __init__ (self):
        pass

    def __call__ (self, guessNum , randoNum): # checking the guess
        global tries

        if guessNum > randoNum:
            return "{0} is to big, try smaller number\n".format(guessNum)

        elif guessNum < randoNum:
            return "{0} is to small, try bigger number\n".format(guessNum)

        else: # The user guessed right
            newRecord = tries
            saver (newRecord)
            tries = 0
            return "\nYou win in {0} tries \nexit and return to play again" .format(newRecord)



def guess(guessNum ,randoNum , Gtxt): # getting here after pressing "SUBMIT" button
    global tries
    tries +=1
    game = GuessTheNumber()
    Gtxt.insert(END, game(guessNum ,randoNum))



def show_record(Gtxt): # displaying the user record
    global oldRecord
    text = "\n\nyour record is: {0}\n\n".format(oldRecord)
    Gtxt.insert(END, text)



def saver(newRecord): # if there is a new record, saving it
    global oldRecord

    if oldRecord == 0 or newRecord < oldRecord:
        oldRecord = newRecord