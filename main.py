from tkinter import *
# importam libraria tkinter pentru a folosi interfata grafica
import random


# importam libraria random pt a folosi functia random
def new_game():
    global player

    player = random.choice(players)

    # randul jucatorului
    label.config(text=player + " turn")

    # creearea grid-ului de butoane si colorate in negru
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="black")


window = Tk()
window.title("XOX_Game")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
# resize la fereastra
window.geometry("%dx%d" % (width, height))
# alegere caractere jucatori si functia random pentru a incepe
players = ["X", "O"]
player = random.choice(players)

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=player + " turn", font=('consolas', 40))
label.pack(padx=0, pady=30, side="top")

# realizarea butonului de reset
reset_button = Button(text="RESET", font=('consolas', 20), command=new_game)
reset_button.pack(pady=30, side="bottom")

frame = Frame(window)
frame.pack()


def next_turn(row, column):
    global player

    # testare initiala pentru a vedea daca jocul nu este castigat
    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            # schibarea jucatorului in caz ca jocul nu e castigat

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + " turn"))

            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))

            elif check_winner() == "Try again!":
                label.config(text="Try again!!")

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))

            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))

            elif check_winner() == "Try again!":
                label.config(text="Try again!!")


def check_winner():
    # parcurgem fiecare rand sa vedem daca textul din buton daca e identic
    for i in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    # parcurgem fiecare coloana sa vedem daca textul din buton daca e identic

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    # parcurgem fiecare diagonala sa vedem daca textul din buton daca e identic

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    # daca una din if urile de mai sus sunt indepicite butoanele respective se coloreaza in verde
    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="#cccc00")
        return "Try again!"

    else:
        return False


def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2, bg="black", fg="white",
                                      borderwidth=5, command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)
window.mainloop()
