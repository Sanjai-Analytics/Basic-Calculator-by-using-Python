from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("300x400")

scvalue = StringVar()

screen = Entry(root, textvariable=scvalue, font="Arial 24")
screen.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, padx=10, pady=10)

def click(value):
    if value == "=":
        try:
            scvalue.set(eval(scvalue.get()))
        except:
            scvalue.set("Error")

    elif value == "C":
        scvalue.set("")

    elif value == "Guvi":
        scvalue.set("I Learned Python at Guvi")

    else:
        scvalue.set(scvalue.get() + value)

buttons = [
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","-"],
    ["0",".","=","+"],
]

row = 1
for r in buttons:
    col = 0
    for c in r:
        Button(root,text=c,font="Arial 18",
               command=lambda x=c: click(x),
               width=5,height=2).grid(row=row,column=col,padx=5,pady=5)
        col += 1
    row += 1

Button(root,text="C",font="Arial 18",command=lambda: click("C"),
       width=22,height=2).grid(row=5,column=0,columnspan=4,pady=5)

# Button(root,text="Guvi", font="Arial 18",command=lambda: click("Guvi"),
#        width=16,height=2).grid(row=6,column=0,columnspan=4,pady=5)

# logo = PhotoImage(file="Projects/guvi.png")
# Label(root, image=logo).grid(row=7, column=0, columnspan=4)

logoGuvi=PhotoImage(file="Projects/guvi.png")

Button(root,
       image=logoGuvi,
       command=lambda: click("Guvi")
).grid(row=6, column=0, columnspan=4, pady=5)
root.mainloop()
