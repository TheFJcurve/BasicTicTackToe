from tkinter import *
import numpy as np
from PIL import Image, ImageTk

# Keeping the official state of events
record_of_moves = np.array([[0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]])
# Keeping a track of which player is playing
player = 1

def is_over():
    '''checks if the tictacktoe game is over or not '''
    for number in range(3):
        if np.array_equal(record_of_moves[number], [1, 1, 1]) or \
                np.array_equal(record_of_moves[number], [2, 2, 2]):
            return True
        elif np.array_equal(record_of_moves[:, number], [1, 1, 1]) or \
                np.array_equal(record_of_moves[:, number], [2, 2, 2]):
            return True
        elif np.array_equal(record_of_moves.diagonal(), [1, 1, 1]) or \
                np.array_equal(record_of_moves.diagonal(), [2, 2, 2]):
            return True
        elif np.array_equal(np.flip(record_of_moves, 1).diagonal(), [1, 1, 1]) or \
                np.array_equal(np.flip(record_of_moves, 1).diagonal(), [2, 2, 2]):
            return True
    return False


def valid_move(position):
    '''checks if the tictacktoe move made by the player is valid or not '''
    if record_of_moves[position[0], position[1]] == 0:
        return True
    else:
        return False

def replace_with_player(button, position):
    '''replaces the button with the player that clicked it, keeps track of the function'''
    if valid_move(position):
        global player
        record_of_moves[position[0], position[1]] = player

        if is_over():
            if player == 1:
                winner = 'X'
            else:
                winner = 'O'

            window = Tk()
            window.geometry("600x600")
            window.title("Victory!")
            canvas02 = Canvas(window, height=600, width=600, bg='white')
            canvas02.pack()
            frame02 = Frame(canvas02, bg='pink', bd=10)
            frame02.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.9, anchor='n')
            win_label = Label(frame02, text=f'Player {winner} has won!', font=50)
            win_label.place(relx=0.40, rely=0.45)
            root.destroy()
            window.mainloop()
        else:

            if player == 1:
                player = 2
                button.config(image=ximg)

            else:
                player = 1
                button.config(image=oimg)
    else:
        error_label = Label(frame, text='Place Already Occupied, try somewhere else')
        error_label.place(relx=0.275, rely=0.85)

        error_label.after(1000, lambda: error_label.place_forget())


# Making the main window where the program runs on
root = Tk()
root.geometry("600x600")
root.minsize(600, 600)
root.maxsize(600, 600)
root.title("TicTakToe")
canvas = Canvas(root, height=600, width=600, bg='white')
canvas.pack()

# Importing the Images
ximage = Image.open("x.png")
ximage = ximage.resize((81, 81))
ximg = ImageTk.PhotoImage(ximage)
oimage = Image.open("o.png")
oimage = oimage.resize((81, 81))
oimg = ImageTk.PhotoImage(oimage)

# Making the frame where the buttons will be placed
frame = Frame(canvas, bg='pink', bd=10)
frame.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.9, anchor='n')

# Making buttons for the application. When clicked, they send their location to the functions.
button00 = Button(frame, bg="white", command=lambda: replace_with_player(button00, [0, 0]))
button00.place(relx=0.20, rely=0.20, relheight=0.15, relwidth=0.15)

button01 = Button(frame, bg="white", command=lambda: replace_with_player(button01, [0, 1]))
button01.place(relx=0.425, rely=0.20, relheight=0.15, relwidth=0.15)

button02 = Button(frame, bg="white", command=lambda: replace_with_player(button02, [0, 2]))
button02.place(relx=0.65, rely=0.20, relheight=0.15, relwidth=0.15)

button10 = Button(frame, bg="white", command=lambda: replace_with_player(button10, [1, 0]))
button10.place(relx=0.20, rely=0.40, relheight=0.15, relwidth=0.15)

button11 = Button(frame, bg="white", command=lambda: replace_with_player(button11, [1, 1]))
button11.place(relx=0.425, rely=0.40, relheight=0.15, relwidth=0.15)

button12 = Button(frame, bg="white", command=lambda: replace_with_player(button12, [1, 2]))
button12.place(relx=0.65, rely=0.40, relheight=0.15, relwidth=0.15)

button20 = Button(frame, bg="white", command=lambda: replace_with_player(button20, [2, 0]))
button20.place(relx=0.20, rely=0.60, relheight=0.15, relwidth=0.15)

button21 = Button(frame, bg="white", command=lambda: replace_with_player(button21, [2, 1]))
button21.place(relx=0.425, rely=0.60, relheight=0.15, relwidth=0.15)

button22 = Button(frame, bg="white", command=lambda: replace_with_player(button22, [2, 2]))
button22.place(relx=0.65, rely=0.60, relheight=0.15, relwidth=0.15)

# Running the applications on root
root.mainloop()
