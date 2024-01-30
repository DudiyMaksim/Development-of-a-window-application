from tkinter import *

def func_b(color):
    entry.delete(0, END)
    entry.insert(0, color)
    root["background"] = color

def MakeButton(name, id):
    button = Button(root, text=name, bg=id, fg="white")
    button.config(command=lambda c=id: func_b(c))
    button.pack()

root = Tk()
root.title("Color Picker")
root.geometry("600x500")

label = Label(root, font="Arial",text="id of color : ")
label.pack()

entry = Entry(root, font=("Arial", 12), width=30)
entry.pack()
entry.insert(0, "#")

MakeButton('Celtic Blue', '#246bce')
MakeButton('Candy Apple Red', '#ff0800')
MakeButton('Byzantium','#702963')
MakeButton("Yellow1",'#ffff00')
MakeButton('Chartreuse4', '#458b00')
MakeButton('Gray1','#030303')

root.mainloop()
