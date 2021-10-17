from tkinter import *
from  tkinter.filedialog import askopenfilename,asksaveasfilename
import os
from  tkinter.messagebox import showinfo
import tkinter.messagebox as msg



def new():
    global file
    root.title("Untitled - Notepad")
    file = None
    textarea.delete(1.0,END)



def flieopen():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        textarea.delete(1.0,END)
        with open(file) as f:
            textarea.insert(1.0, f.read())



def save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

        if file == "":
            file = None
        else:
            with open(file,"w") as f:
                f.write(textarea.get(1.0,END))
            root.title(os.path.basename(file)+"-Notepad")
            print("file saved")
    else:
        with open(file, "w") as f:
            f.write(textarea.get(1.0, END))
        root.title(os.path.basename(file) + "-Notepad")
def cut():
    textarea.event_generate(("<<Cut>>"))


def copy():
    textarea.event_generate(("<<Copy>>"))


def paste():
    textarea.event_generate(("<<Paste>>"))

def feedback():
    msg.askyesno("Feedback","how's your experience with us its good or not ?")



def help():
    msg.showinfo("Help","visit our website-www.Notepad.com")

def about():
    showinfo("Notepad","Notepad by Meharwan singh rathore")




root = Tk()
root.geometry("900x615")
root.title("Untitled-Notepad")
root.wm_iconbitmap("notepad_icon.ico")



textarea = Text(root,font="lucida 13")
textarea.pack(expand=True,fill=BOTH)

file = None

# File MENU-----------

Filemenu = Menu(root)

# Submenu---------

File = Menu(Filemenu,tearoff=0)
File.add_command(label="New",command=new)
File.add_separator()
File.add_command(label="Open...",command=flieopen)
File.add_separator()
File.add_command(label="Save",command=save)
File.add_separator()
File.add_command(label="Exit",command=quit)
Filemenu.add_cascade(label="File",menu=File)
root.config(menu=Filemenu)


# Submenu---------

Edit = Menu(Filemenu,tearoff=0)
Edit.add_command(label="Cut",command=cut)
Edit.add_separator()
Edit.add_command(label="Copy",command=copy)
Edit.add_separator()
Edit.add_command(label="Paste",command=paste)
Filemenu.add_cascade(label="Edit",menu=Edit)
root.config(menu=Filemenu)


# Submenu---------

Help = Menu(Filemenu,tearoff=0)
Help.add_command(label="View help",command=help)
Help.add_separator()
Help.add_command(label="Send feedback",command=feedback)
Help.add_separator()
Help.add_command(label="About notepad",command=about)
Filemenu.add_cascade(label="Help",menu=Help)
root.config(menu=Filemenu)

# ADDING SCROLLBAR...

scroll = Scrollbar(textarea)
scroll.pack(side=RIGHT,fill = Y)
scroll.config(command=textarea.yview)
textarea.config(yscrollcommand=scroll.set)




root.mainloop()