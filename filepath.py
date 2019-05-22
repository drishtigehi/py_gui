#This is for python 3 and above
from tkinter import *
#from tkinter import filedialog #for python 3.5
root = Tk()
root.filename=filedialog.askopenfilename( filetypes = ("All files","*.*") )
print(root.fileName)

