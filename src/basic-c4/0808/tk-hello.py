from tkinter import *
import tkinter.messagebox as mb

def say_hello():
    mb.showinfo("挨拶", "おはようございます")

root = Tk()
root.title("あいさつ")
desc_label = Label(text="以下のボタンを押してください")
desc_label.pack()

hello_button = Button(
text="挨拶",
width=10, height=3,
command=say_hello)
hello_button.pack()
root.mainloop()
