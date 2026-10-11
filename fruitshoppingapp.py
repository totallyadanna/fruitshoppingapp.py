from tkinter import *
# tkinter is a graphical library of python

window = Tk()
# creating the app window

window.geometry("800x600")
# the width and height of the window

window.title("The Fruit Shopping App")
# title of the window

# give colour to the window
window.config(background = "blue")

def calculatePrice():
    price = 3
    fruits = fruit.get()
    amount = int(quantity.get())
    totalPrice = price * amount
    finalPrice.config(text= "total price you need to pay is " + str(totalPrice))

heading = Label(window,text="fruit shopping app", font = ("Ariel", 40), background = "blue", fg = "white")

# display heading

heading.place(x=200,y=0)

selectfruit = Label(window,text="select fruit:", font = ("Ariel", 30), background = "blue", fg = "white")
selectfruit.place(x=100, y=140)
# displays a label and the coordinates

fruit = Spinbox(window, values = ("apple", "orange", "banana", "kiwi", "blueberry", "blackberry", "dragonfruit", "sugarcane", "pineapple", "melon", "grape"))
fruit.place(x = 250, y = 150)
# creates a spinbox of options

quantity = Label(window,text="quantity:", font = ("Ariel", 30), background = "blue", fg = "white")
quantity.place(x=100, y=287)

quantity = Spinbox(window, from_ =0, to = 10)
quantity.place(x = 220, y = 300)
# range of numbers

priceButton = Button(window, text = "calculate the price", command = calculatePrice)
priceButton.place(x = 250, y = 350)

finalPrice = Label(window, text = "final price =", background = "blue", fg = "white")
finalPrice.place(x = 250, y = 400)

# output stays on the screen forever until the user manually closes the window

window.mainloop()
