from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfile,asksaveasfile


def new():
    textArea.delete(1.0,END)

def openfile():
    nameoffile=askopenfile()
    pathOffile=nameoffile.name

    f=open(pathOffile,"r")
    data=f.read()
    f.close

    textarea.insert(1.0,data)

def save():
    content=textarea.get(1.0,END)
    namefile=asksaveasfile(initialfile="untitled.txt", defaultextension=".txt",
                         filetypes=[("all files", "*.*"), ("Text Documents", "*.txt")])
    f=open(nameFile.name,"w")
    f.write(content)
    f.close()

def closeapplication():
    root.destroy()

def allselect():
    textarea.event_generate("<<SelectAll>>")

def cut():
    textarea.event_generate('<<Cut>>')

def copy():
    textarea.event_generate('<<Cut>>')

def paste():
    textarea.event_generate('<<Paste>>')

def aboutus():
    showinfo("about company description")

def teams():
    showinfo("about developers description")

root=Tk()
root.title("notepad")
root.geometry("500x300")

textarea=Text()
textarea.pack(expand=True, fill=BOTH)
textarea.config(bg="light green")


mainmenu=Menu(root)
root.config(menu=mainmenu)

filemenu=Menu(mainmenu, tearoff=0)
editmenu=Menu(mainmenu, tearoff=0)
aboutmenu=Menu(mainmenu, tearoff=0)



filemenu.add_command(label="new",command=new)
filemenu.add_command(label="open",command=openfile)
filemenu.add_command(label="save", command=save)
filemenu.add_separator()
filemenu.add_command(label="quit", command=closeapplication)

editmenu.add_command(label="select", command=allselect)
editmenu.add_command(label="cutall", command=cut)
editmenu.add_command(label="copy", command=copy)
editmenu.add_command(label="paste", command=paste)

aboutmenu.add_command(label="aboutus", command=aboutus)
aboutmenu.add_command(label="developer", command=teams)



mainmenu.add_cascade(label="file", menu=filemenu)
mainmenu.add_cascade(label="edit", menu=editmenu)
mainmenu.add_cascade(label="about", menu=aboutmenu)




root.mainloop()
