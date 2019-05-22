#This is for python 3 and above
from tkinter import *
#from tkinter import filedialog #for python 3.5
root = Tk()
root.filename=filedialog.askopenfilename( filetypes = ("All files","*.*") )
print(root.fileName)

#for python 2.7
#from Tkinter import *from Tkinter import *
#import Tkinter, Tkconstants, tkFileDialog

#root = Tk()
#root.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
#print (root.filename)
