from tkinter import *
# tkinter is a graphical library of python

window = Tk()
# creating the app window

window.geometry("800x600")
# the width and height of the window

window.title("Fruit Shopping App")
# title of the window

# give colour to the window
window.config(background = "blue")

heading = Label(window,text="fruit shopping app", font = ("Ariel", 40), background = "blue", fg = "white")

# display heading

heading.place(x=200,y=0)

selectfruit = Label(window,text="select fruit:", font = ("Ariel", 30), background = "blue", fg = "white")
selectfruit.place(x=100, y=140)

fruit = Spinbox(window, values = ("apple", "orange", "banana", "kiwi", "blueberry", "blackberry", "dragonfruit", "sugarcane", "pineapple", "melon", "grape"))
fruit.place(x = 250, y = 150)

quantity = Label(window,text="quantity:", font = ("Ariel", 30), background = "blue", fg = "white")
quantity.place(x=100, y=287)

quantity = Spinbox(window, from_ =0, to = 10)
quantity.place(x = 220, y = 300)

# output stays on the screen forever until the user manually closes the window

window.mainloop()