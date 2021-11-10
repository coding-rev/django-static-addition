import os
import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
# Local imports
from main import StaticProjectLogic

root = Tk()
root.geometry('500x300')

class OpenFile:
    def open_file(self):
        file = askopenfile(mode='r', filetypes = [('Html Files', '*.html')])
        if file is not None:
            # Send path to the logic
            send = StaticProjectLogic().logics(file.name)

            # Displaying the results for the user to copy
            with open("results.html",'r')as resultsFile:
                results_content = resultsFile.read()
                #tkinter.messagebox.showinfo('RESULTS - Static Path Added. PLEASE COPY',\content)
                root2 = Tk()
                root2.geometry("900x700")
                # Title
                label = Label(root2, text="Django Static Added - Copy | Credits to: Codingrev")
                label.config(font=("Cambria", 14))
                # Field for displaying text
                TextWidget = Text(root2, height=500, width=800)

                label.pack()
                TextWidget.pack()
    
                TextWidget.insert(tkinter.END, results_content)

btn = Button(root, text="Browse file directory", command=lambda:OpenFile().open_file())
btn.pack(side=TOP, pady=10)
mainloop()
