import tkinter as tk
from tkinter import ttk
import math as math

window = tk.Tk()
window.title("PyProbabilities")
value = 0
probs = []
attempts = []

frame = tk.Frame(master = window, width= 500, height= 500)
frame.grid(row = 5, column= 3, padx=5, pady=5)

label = tk.Label(master= frame, text= "Probability")
label.grid(column= 0, row = 0)

entry = tk.Entry(master=frame, text=value)
entry.grid(column= 1, row = 0)


def button_action():
    
    global entry
    value1 = float(entry.get())
    calculate(value1)
    populate_gui()

def calculate2(value):
    if value == 0:
        return
    ivalue = 1 - value
    attempts.append(math.log(.25, ivalue))
    probs.append(1 - (ivalue**attempts[0] ))
    attempts.append(math.log(.5, ivalue))
    probs.append(1 - (ivalue**attempts[1] ))
    attempts.append(math.log(.75, ivalue))
    probs.append(1 - (ivalue**attempts[2] ))
    attempts.append(math.log(.99, ivalue))
    probs.append(1 - (ivalue**attempts[3] ))

def calculate(value):
    if value == 0:
        return
    ival = 1 - value
    prob = 0
    counter = 0;
    threshold = .25

    global probs
    global attempts

    probs= []
    attempts = []

    while threshold < 1:
        print (str(threshold) + " " + str (counter))
        while True:
            prob = 1 - ival**counter
            if prob < threshold:
                counter = counter + 1
            else :
                probs.append(prob)
                attempts.append(counter)
                break
            
        threshold = threshold + .25
        if threshold == 1:
            threshold = .99
        

def populate_gui():
    global probs
    global attempts
    global label_text1
    global label_text2
    global label_text3
    global label_text4

    label_text1.set( "25% chance at {0} attemps ({1} probability)".format(attempts[0],round(probs[0],5)))
    label_text2.set( "50% chance at {0} attemps ({1} probability)".format(attempts[1],round(probs[1],5)))
    label_text3.set( "75% chance at {0} attemps ({1} probability)".format(attempts[2],round(probs[2],5)))
    label_text4.set( "99% chance at {0} attemps ({1} probability)".format(attempts[3],round(probs[3],5)))



btn = tk.Button(master=frame, text="Calculate", command=button_action)
btn.grid(column= 2, row = 0)


label_text1 = tk.StringVar()
label_text1.set("25% chance:")
label1 = tk.Label(textvariable=label_text1)
label1.grid(column= 2, row = 1, columnspan= 3)
#label1.pack()
label_text2 = tk.StringVar()
label_text2.set("50% chance:")
label2 = tk.Label(textvariable=label_text2)
label2.grid(column= 2, row = 2, columnspan= 3, sticky=tk.W + tk.E)
#label2.pack()
label_text3 = tk.StringVar()
label_text3.set("75% chance:")
label3 = tk.Label(textvariable=label_text3)
label3.grid(column= 2, row = 3, columnspan= 3, sticky=tk.W + tk.E)
#label3.pack()
label_text4 = tk.StringVar()
label_text4.set( "99% chance:")
label4 = tk.Label(textvariable=label_text4)
label4.grid(column= 2, row = 4, columnspan= 3, sticky=tk.W + tk.E)

window.mainloop()



