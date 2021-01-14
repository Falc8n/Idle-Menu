from tkinter import *


def close_root():
    root.destroy()


root = Tk()

home_label = Label(root, text="home").grid(row=0, column=1)

exit_button = Button(root, text="Exit", command=close_root).grid(row=0, column=10)



root.title("Idle Menu v0.1")
root.geometry("500x500")

root.mainloop()