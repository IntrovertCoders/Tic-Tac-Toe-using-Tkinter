from tkinter import *
from tkinter import messagebox

root = Tk(className=" Tik Tac Toe")
root.geometry('425x490')


turn = 1
move = 0
Xscore = 0
Oscore = 0


def btn_reset():
    global turn, move
    turn = 1
    move = 0
    button1['text'] = ' '
    button2['text'] = ' '
    button3['text'] = ' '
    button4['text'] = ' '
    button5['text'] = ' '
    button6['text'] = ' '
    button7['text'] = ' '
    button8['text'] = ' '
    button9['text'] = ' '


def update_button(btn):
    global turn, move, Xscore, Oscore
    move += 1
    if btn['text'] == ' ' and turn == 1:
        btn['fg'] = "Black"
        btn['text'] = 'X'
        turn = 0
    elif btn['text'] == ' ' and turn == 0:
        btn['fg'] = "Red"
        btn['text'] = 'O'
        turn = 1
    else:
        move -= 1
        messagebox.showwarning("Warning", "Button Already Clicked")
    if move <= 9:
        if check_win() == 1:
            Xscore += 1
            messagebox.showinfo("Congratulations", "Player X won")
            text1.delete('1.0', END)
            text1.insert(INSERT, Xscore)
            if messagebox.askyesno("New Game", "Do you want to start a new Game?"):
                btn_reset()
            else:
                root.destroy()
        elif check_win() == 0:
            Oscore += 1
            messagebox.showinfo("Congratulations", "Player O won")
            text2.delete('1.0', END)
            text2.insert(INSERT, Oscore)
            if messagebox.askyesno("New Game", "Do you want to start a new Game?"):
                btn_reset()
            else:
                root.destroy()
    if move == 9 and check_win() == -1:
        messagebox.showinfo("Ouchh", "It's a TIE")
        if messagebox.askyesno("New Game", "Do you want to start a new Game?"):
            btn_reset()
        else:
            root.destroy()


def check_win():
    # player X condition check
    if ((button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X') or
            (button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X') or
            (button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X')):
        return 1
    elif ((button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X') or
          (button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X') or
          (button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X')):
        return 1
    elif ((button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X') or
          (button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X')):
        return 1
    # player O condition check
    if ((button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O') or
            (button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O') or
            (button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O')):
        return 0
    elif ((button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O') or
          (button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O') or
          (button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O')):
        return 0
    elif ((button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O') or
          (button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O')):
        return 0
    return -1


# buttons
button1 = Button(root, text=' ', font=('consolas', 45), width=4, command=lambda: update_button(button1))
button1.grid(row=0, column=0)
button2 = Button(root, text=' ', font=('consolas', 45), width=4, command=lambda: update_button(button2))
button2.grid(row=0, column=1)
button3 = Button(root, text=' ', font=('consolas', 45), width=4, command=lambda: update_button(button3))
button3.grid(row=0, column=2)
button4 = Button(root, text=' ', font=('consolas', 45), width=4, command=lambda: update_button(button4))
button4.grid(row=1, column=0)
button5 = Button(root, text=' ', font=('consolas', 45), width=4, command=lambda: update_button(button5))
button5.grid(row=1, column=1)
button6 = Button(root, text=' ', font=('consolas', 45), width=4, command=lambda: update_button(button6))
button6.grid(row=1, column=2)
button7 = Button(root, text=' ', font=('consolas', 45), width=4, command=lambda: update_button(button7))
button7.grid(row=2, column=0)
button8 = Button(root, text=' ', font=('consolas', 45), width=4, command=lambda: update_button(button8))
button8.grid(row=2, column=1)
button9 = Button(root, text=' ', font=('consolas', 45), width=4, command=lambda: update_button(button9))
button9.grid(row=2, column=2)

# text
label = Label(root, text="      Player X Score : ", font=('Orbitron', 15), fg='Black')
label.place(relx=0.0, rely=0.8)

text1 = Text(root, height=1, font=('Orbitron', 15), width=3, fg='Black')
text1.place(relx=0.7, rely=0.8)

label = Label(root, text="      Player O Score : ", font=('Orbitron', 15), fg='Red')
label.place(relx=0.0, rely=0.9)

text2 = Text(root, height=1, font=('Orbitron', 15), width=3, fg='Red')
text2.place(relx=0.7, rely=0.9)

text1.insert(INSERT, "0")
text2.insert(INSERT, "0")

root.mainloop()
