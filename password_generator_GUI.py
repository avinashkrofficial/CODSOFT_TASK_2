from tkinter import *
import string
import random
import pyperclip


root = Tk()

def generate():
    s1 = string.ascii_lowercase 
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    passlen = int(uservalue.get())
    strength = var.get()
    
    outputentry.delete(0, END)  

    if strength == 1:
        easy = []
        easy.extend(s1)
        easy.extend(s2)
        password = ''.join(random.sample(easy, passlen))
        outputentry.insert(0, password)
    
    elif strength == 2:
        medium = []
        medium.extend(s1)
        medium.extend(s2)
        medium.extend(s3)
        password = ''.join(random.sample(medium, passlen))
        outputentry.insert(0, password)

    elif strength == 3:
        hard = []
        hard.extend(s1)
        hard.extend(s2)
        hard.extend(s3)
        hard.extend(s4)
        password = ''.join(random.sample(hard, passlen))
        outputentry.insert(0, password)

def copy():
    password = outputvalue.get()
    pyperclip.copy(password)



f2 = Frame(root, borderwidth=20, relief=RIDGE, bg="cyan")
f2.grid(row=2)

l1 = Label(f2, text="Password Generator", font="Times 20 bold", background="cyan",fg="black")
l1.grid(columnspan=2,pady=30)

Label(f2, text="Enter the length of the password: ", font="Times 15", bg="cyan",fg="black").grid(row=1, column=0, pady=20)
uservalue = StringVar()
userentry = Entry(f2, textvariable=uservalue, font="Times 15",justify=RIGHT)
userentry.grid(row=1, column=1)

Label(f2, text="Choose the strength of the password: ", font="Times 15", bg="cyan",fg="black").grid(row=2, column=0)
var = IntVar()
R1 = Radiobutton(f2, text="Weak", font="Times 15", variable=var, value=1, bg="cyan",fg="black")
R1.grid(row=2, column=1)
R2 = Radiobutton(f2, text="Medium", font="Times 15", variable=var, value=2, bg="cyan",fg="black")
R2.grid(row=3, column=1)
R3 = Radiobutton(f2, text="Strong", font="Times 15", variable=var, value=3, bg="cyan",fg="black")
R3.grid(row=4, column=1)

Button(f2, text="Generate", command=generate, font="Times 15",bg="#041f60",bd=5,relief=GROOVE,fg="white").grid(column=1, pady=20)

Label(f2, text="Click here to generate: ", font="Times 15", bg="cyan",fg="black").grid(row=5, column=0)

Label(f2, text="Your generated password is: ", font="Times 15", bg="cyan",fg="black").grid(row=6, column=0,padx=10)

outputvalue = StringVar()
outputentry = Entry(f2, textvariable=outputvalue, font="Times 15", width=30, fg="black",justify=RIGHT)
outputentry.grid(row=6, column=1, pady=20,padx=10)

Label(f2, text="Click below to quit the application: ", font="Times 15", bg="cyan",fg="black").grid(row=7, column=1,pady=20)
Label(f2, text="Click below to copy the password: ", font="Times 15", bg="cyan",fg="black").grid(row=7, column=0,pady=20)

Button(f2, text="Quit", command=quit, font="Times 15", fg="white",bg="#041f60",bd=5,relief=GROOVE).grid(row=8,column=1,pady=20 )
Button(f2, text="Copy", command=copy, font="Times 15", fg="white",bg="#041f60",bd=5,relief=GROOVE).grid(row=8,column=0, pady=20)

root.wm_iconbitmap("key_password_lock_800.ico")
root.title("Avinash Password Generator")
root.geometry("665x611")
root.configure(background="white")
root.resizable(0,0)
root.mainloop()
