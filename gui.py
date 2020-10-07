# By Stephen van der Westhuizen

from tkinter import * # the gui
from functions import * # functions
from PIL import ImageTk, Image # jpeg image support

# Setup
root = Tk()
root.title("Dister")
root.resizable(False, False)

metrics = ["Kilometer", "Meter", "Mile", "Foot"]
defVal = StringVar(root)
defVal.set(metrics[0]) # default value for drop down list

# Create all components
lblTitle = Label(root, text=" Dister - Get the distance ", bg="#ff0000")
lblLocation1 = Label(root, text="Location 1:", pady=10)
edtLocation1 = Entry(root)
lblLocation2 = Label(root, text="Location 2:", pady=10)
edtLocation2 = Entry(root)
cmbMetric = OptionMenu(root, defVal, *metrics, command=setMesure)
lblAnswer = Label(root, text="Answer", relief=SUNKEN, width=20)
btnCalculate = Button(root, text="Calculate", command=lambda:calcDistance(edtLocation1.get(), edtLocation2.get(), lblAnswer, root))

img = ImageTk.PhotoImage(Image.open("images/help.jpeg").resize((20, 20))) # define an image
imgHelp = Button(root, image=img, command=giveHelp) # image help button

# Place all components
lblTitle.grid(row=0, column=0, columnspan=4)
lblLocation1.grid(row=1, column=0)
edtLocation1.grid(row=1, column=1, columnspan=2)
lblLocation2.grid(row=2, column=0)
edtLocation2.grid(row=2, column=1, columnspan=2)
cmbMetric.grid(row=3, column=0)
btnCalculate.grid(row=3, column=1)
imgHelp.grid(row=3, column=2)
# NOTE TO FUTURE SELF:
# If you change the row here, you gotta change it inside functions.py as well!!
lblAnswer.grid(row=4, column=0, columnspan=3, pady=10)

# Configure all components
lblTitle.configure(font=("Sans-Serif", 20))
lblLocation1.configure(font=("monospace", 15))
lblLocation2.configure(font=("monospace", 15))
lblAnswer.configure(font=("monospace", 15))

# Extras
edtLocation1.insert(0, "Cape Town") # default text
edtLocation1.bind('<Control-a>', lambda e: callback(e, root))
edtLocation2.insert(0, "Tokyo") # default text
edtLocation2.bind('<Control-a>', lambda e: callback(e, root))
# btnCalculate.bind("<Enter>", lambda e:calcDistance(edtLocation1.get(), edtLocation2.get(), lblAnswer, root))

root.mainloop();