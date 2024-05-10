from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from test import global_voting_app

root = Tk()
root.title('GLOBAL VOTING')


create_label = Label(root,text="HELLO THERE! DO YOU HAVE AN ACCOUND IN GLOBAL VOTING?")
create_label.pack()



def create():
    top = Toplevel()
    top.title('Create an account')
    username_label = Label(top,text="Enter a username!")
    username_label.pack()
    e = Entry(top)
    e.pack()
    def add_username(periexomeno):
        with open('1.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.strip() == periexomeno:
                    error = messagebox.showerror('Name existing',f'The username {periexomeno} is already used')
                    if error == 'ok':
                        top.destroy()
                        return  False

        arxeio = open('1.txt', 'a')
        arxeio.write(periexomeno+'\n')
        arxeio.close()
        top.destroy()

    cont_button = Button(top,text='Continue',command=lambda : add_username(e.get()))
    cont_button.pack()

def login():
    top = Toplevel()
    top.title('Login to account')
    username_label = Label(top, text="Enter your username!")
    username_label.pack()
    e = Entry(top)
    e.pack()

    def find_username(periexomeno):
        arxeio = open('1.txt', 'r')
        grammes = arxeio.readlines()
        for grammi in grammes:
            if grammi == periexomeno+'\n':
                message_info = messagebox.showinfo('Login completed succefully',f"Welcome back {periexomeno}!!")
                if message_info == 'ok':
                    top.destroy()
                    # MAIN PROGRAMM
                    global_voting_app(root,periexomeno)

            else:
                no_name_label = Label(top,text=f"Sorry, the name {periexomeno} was not found,try another name!")
                no_name_label.pack()

    login_button = Button(top, text='Continue', command=lambda: find_username(e.get()))
    login_button.pack()


login_button = Button(root,text="YES",command=login)
login_button.pack()
no_button = Button(root,text='NO',command=create)
no_button.pack()
vote_image = ImageTk.PhotoImage(Image.open('Document.png'))
img_label = Label(root, image=vote_image)
img_label.pack()


root.mainloop()