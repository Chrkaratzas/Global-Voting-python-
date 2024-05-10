from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from matplotlib import pyplot as plt

def global_voting_app(root,username):
    root.destroy()
    gv = Tk()
    gv.title("Global Voting")
    vote_label = Label(gv, text="BASKETBALL OR FOOTBALL ?")
    vote_label.grid(row = 0, column = 0, columnspan = 5)

    def option1(name):
        vote1 = []
        with open('vote1.txt', 'r') as file:
            lines = file.readlines()
        for line in lines:
            vote1.append(line.strip())
        vote2 = []
        with open('vote2.txt', 'r') as file:
            lines = file.readlines()
        for line in lines:
            vote2.append(line.strip())

        if name in vote1:
            accound_voted_error = messagebox.showerror('Already voted', 'You have already voted, wait for the next vote!')
        elif name in vote2:
            accound_voted_error = messagebox.showerror('Already voted','You have already voted, wait for the next vote!')
        else:
            with open('vote1.txt','a') as file:
                file.write(name+'\n')
    def option2(name):
        global  vote1
        vote1 = []
        with open('vote1.txt', 'r') as file:
            lines = file.readlines()
        for line in lines:
            vote1.append(line.strip())

        global vote2
        vote2 = []
        with open('vote2.txt', 'r') as file:
            lines = file.readlines()
        for line in lines:
            vote2.append(line.strip())
        if name in vote2:
            accound_voted_error = messagebox.showerror('Already voted','You have already voted, wait for the next vote!')
        elif name in vote1:
            accound_voted_error = messagebox.showerror('Already voted','You have already voted, wait for the next vote!')
        else:
            with open('vote2.txt','a') as file:
                file.write(name+'\n')

    def result():

        options = ['Football', 'Basketball']
        weights = [len(vote1)+1,len(vote2)+1]
        fix, ax = plt.subplots()
        ax.pie(weights,labels=options)
        plt.show()

    button1 = Button(gv,text="FOOTBALL",command=lambda : option1(username))
    button1.grid(row = 1, column = 0)
    button2 = Button(gv,text="BASKETBALL",command=lambda : option2(username))
    button2.grid(row = 1, column = 2)
    image = ImageTk.PhotoImage(Image.open('global_voting.png'))
    image_label = Label(image=image)
    image_label.grid(row = 2, columnspan=3)

    result_button = Button(gv, text='See results',command=result)
    result_button.grid(row = 3, column = 2, columnspan = 4)

    gv.mainloop()