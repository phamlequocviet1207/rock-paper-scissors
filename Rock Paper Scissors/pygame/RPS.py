#import everything from tkinter module
from tkinter import *
from PIL import Image, ImageTk
from random import randint
# main window

#creat a tkinter window 
root = Tk()
root.title("Rock Paper Scissors")
root.configure(background = "#9b59b6")

#picture
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
scissors_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))

rock_img_comp = ImageTk.PhotoImage(Image.open("rock-comp.png"))
scissors_img_comp = ImageTk.PhotoImage(Image.open("scissors-comp.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper-comp.png"))

#insert picture
user_lable = Label(root, image=paper_img, bg="#9b59b6")
comp_lable = Label(root, image=scissors_img_comp, bg="#9b59b6")

user_lable.grid(row=1,column=0)
comp_lable.grid(row=1,column=4)

#scores
playerScore = Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerScore = Label(root,text=0,font=100,bg="#9b59b6",fg="white")
playerScore.grid(row=1,column=1)
computerScore.grid(row=1,column=3)

#messages
msg = Label(root, font=50, bg="#9b59b6", fg="white")
msg.grid(row=3, column=2)

#update message
def updateMessage(x):
    msg['text'] = x

def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score) 

#check winner
def is_win(player, opponent):
    if ((player == 'rock') and (opponent == 'scissors')) or ((player == 'scissors') and (opponent == 'paper')) or \
       ((player == 'paper') and (opponent == 'rock')):
        return True
    return False

def checkWin(player, computer):
    if player == computer:
        text  ="It's a tie"
        updateMessage(text)
    elif is_win(player, computer):
        text = "You won!"
        updateUserScore()
        updateMessage(text)
    else:
        text = "You lost!"
        updateCompScore()
        updateMessage(text)
    

#update choices
choices = ["rock","paper","scissors"]
def updateChoice(x):
    #for computer
    compChoice = choices[randint(0,2)]
    if compChoice=="rock":
        comp_lable.configure(image=rock_img_comp)
    elif compChoice=="paper":
        comp_lable.configure(image=paper_img_comp)
    else:
        comp_lable.configure(image=scissors_img_comp)

    #for user
    if x=="rock":
        user_lable.configure(image=rock_img)
    elif x=="paper":
        user_lable.configure(image=paper_img)
    else:
        user_lable.configure(image=scissors_img)
    
    checkWin(x,compChoice)

#indicators
user_indicator = Label(root,font=50,text="USER",bg="#9b59b6",fg="white")
comp_indicator = Label(root,font=50,text="COMPUTER",bg="#9b59b6",fg="white")
user_indicator.grid(row=0,column=0)
comp_indicator.grid(row=0,column=4)

#buttons

rock = Button(root,width=20,height=2,text="ROCK",command = lambda:updateChoice("rock"), bg="#FF3E4D").grid(row=2,column=1)
paper = Button(root,width=20,height=2,text="PAPER",command = lambda:updateChoice("paper"), bg="#FAD02E").grid(row=2,column=2)
scissors = Button(root,width=20,height=2,text="SCISSORS",command = lambda:updateChoice("scissors"), bg="#0ABDE3").grid(row=2,column=3)

root.mainloop()

