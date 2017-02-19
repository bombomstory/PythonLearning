from tkinter import *
import tkinter
import random

MAP = [-1, -1, -1,
-1, -1, -1,
-1, -1, -1]
layoutGrid = [(0, 1, 0), (1, 1, 1), (2, 1, 2),
(3, 2, 0), (4, 2, 1), (5, 2, 2),
(6, 3, 0), (7, 3, 1), (8, 3, 2)]
root = Tk()
layoutButtons = [] #keeps all game buttons
controlButtons = [] #keeps all control buttons
player = 1 #0 = Computer, 1 = You (default=You)
playMode = 0 # 0 = Easy, 1 = Hard

def drawMainWindow():
    global root
root.title("Tic-Tac-Toe")

def drawMenuBar():
        menubar = Menu(root, selectcolor="red")
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New Game",command=resetGame)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.destroy)
        menubar.add_cascade(label="File", menu=filemenu)
        root.config(menu=menubar)
        
        return menubar

def setMode(mode) :
    def set() :
        global playMode
        if mode == 0: playMode = 0
        else: playMode = 1
    return set

def resetGame():
    global MAP
    global layoutButtons
    global controlButtons
    controlButtons[1]['text']=""
    layoutButtons = []
    controlButtons = []
    playMode = 0
    for i in range(9):
        MAP[i] = -1
    TicTacToe()

def checkStatus():
    global MAP
    for i in range(9):
        if MAP[i] == -1:
            return True
    return False

def comPlayModeEasy():
    global MAP
    global layoutButtons
    while checkStatus():
        ran = random.randrange(9)
        if MAP[ran] == -1:
            MAP[ran] = 0
            layoutButtons[ran]['text']='O'
            layoutButtons[ran]['state']=DISABLED
        break

def comPlayModeAI():
    global MAP
    global layoutButtons
    while checkStatus():
    # AI computing
        searchCom = AICheck(0)
        searchPly = AICheck(1)
        if searchCom == -1 and searchPly == -1:
            ran = random.randrange(9)
        if MAP[ran] == -1:
            MAP[ran] = 0
            layoutButtons[ran]['text']='O'
            layoutButtons[ran]['state']=DISABLED
            break
        else:
            if searchCom != -1:
                MAP[searchCom] = 0
                layoutButtons[searchCom]['text']='O'
                layoutButtons[searchCom]['state']=DISABLED
                break
            else:
                MAP[searchPly] = 0
                layoutButtons[searchPly]['text']='O'
                layoutButtons[searchPly]['state']=DISABLED
        break

def AICheck(who):
    global MAP
    count = 0
    for i in 0,1,2:
        if MAP[i]==who:
             count += 1

        if count == 2:
            for j in 0,1,2:
                if MAP[j]== -1:
                    return j
            count = 0
        for i in 3,4,5:
            if MAP[i]==who:
                count += 1
            if count == 2:
                for j in 3,4,5:
                    if MAP[j]== -1:
                        return j
            count = 0
    
        for i in 6,7,8:
            if MAP[i]==who:
                count += 1
            if count == 2:
                for j in 6,7,8:
                    if MAP[j]== -1:
                        return j
            count = 0
        for i in 0,3,6:
            if MAP[i]==who:
                count += 1
            if count == 2:
                for j in 0,3,6:
                    if MAP[j]== -1:
                        return j
            count = 0
    for i in 1,4,7:
        if MAP[i]==who:
            count += 1
        if count == 2:
            for j in 1,4,7:
                if MAP[j]== -1:
                    return j
    count = 0
    for i in 2,5,8:
        if MAP[i]==who:
            count += 1
        if count == 2:
            for j in 2,5,8:
                if MAP[j]== -1:
                    return j
    count = 0
    for i in 0,4,8:
        if MAP[i]==who:
            count += 1
    if count == 2:
        for j in 0,4,8:
            if MAP[j]== -1:
                return j
    count = 0
    for i in 2,4,6:
        if MAP[i]==who:
            count += 1
        if count == 2:
            for j in 2,4,6:
                if MAP[j]== -1:
                    return j
    return -1

    def checkWin():
        global MAP
    for i in range(2):
        if MAP[0]==i and MAP[1]==i and MAP[2]==i: #(r0)
            if i == 0: return "COM"
            elif i == 1: return "YOU"
        elif MAP[3]==i and MAP[4]==i and MAP[5]==i: #(r1)
            if i == 0: return "COM"
            elif i == 1: return "YOU"
            elif MAP[6]==i and MAP[7]==i and MAP[8]==i: #(r2)
                if i == 0: return "COM"
                elif i == 1: return "YOU"
            elif MAP[0]==i and MAP[3]==i and MAP[6]==i: #(c0)
                if i == 0: return "COM"
                elif i == 1: return "YOU"
            elif MAP[1]==i and MAP[4]==i and MAP[7]==i: #(c1)
                if i == 0: return "COM"
                elif i == 1: return "YOU"
            elif MAP[2]==i and MAP[5]==i and MAP[8]==i: #(c2)
                if i == 0: return "COM"
                elif i == 1: return "YOU"
            elif MAP[0]==i and MAP[4]==i and MAP[8]==i: #(s1)
                if i == 0: return "COM"
                elif i == 1: return "YOU"
            elif MAP[2]==i and MAP[4]==i and MAP[6]==i: #(s1)
                if i == 0: return "COM"
                elif i == 1: return "YOU"

    def onClick(userMarks):
        def click():
            global MAP
            global playMode
            global layoutButtons
    print(playMode)
    if playMode == 0:
        MAP[userMarks] = 1
    layoutButtons[userMarks]['text']='X'
    layoutButtons[userMarks]['state']=DISABLED
    comPlayModeEasy()
    check = checkWin()
    if check == "YOU":
        for button in layoutButtons:
            button['state']=DISABLED
            controlButtons[1]['fg']="red"
            controlButtons[1]['text']="You win"

    if check == "COM":
        for button in layoutButtons:
            button['state']=DISABLED
            controlButtons[1]['fg']="red"
            controlButtons[1]['text']="Com win"

    if playMode == 1:
        MAP[userMarks] = 1
        layoutButtons[userMarks]['text']='X'
        layoutButtons[userMarks]['state']=DISABLED
        comPlayModeAI()
    print(MAP)
    check = checkWin()
    if check == "YOU":
        for button in layoutButtons:
            button['state']=DISABLED
            controlButtons[1]['fg']="red"
            controlButtons[1]['text']="You win"

    if check == "COM":
        for button in layoutButtons:
            button['state']=DISABLED
            controlButtons[1]['fg']="red"
            controlButtons[1]['text']="Com win"
    return click

    def drawGraphic():
        global root
        global layoutButtons
        global layoutGrid
        global controlButtons
    control = Label(root, text="Result:")
    control.grid(row=0, column=0)
    controlButtons.append(control) #controlButtons[0]
    control = Label(root, text="")
    control.grid(row=0, column=1)
    controlButtons.append(control) #controlButtons[1]
    control = Label(root, text="You please\nplay first")
    control.grid(row=4, column=0)
    controlButtons.append(control) #controlButtons[2]
    control = Label(root, text="")
    control.grid(row=4, column=1)
    controlButtons.append(control) #controlButtons[3]
    control = Radiobutton(root, text="Easy", relief=GROOVE,
    value=0, command=setMode(0))
    control.grid(row=5, column=0)
    controlButtons.append(control) #controlButtons[4]
    control = Radiobutton(root, text="Hard", relief=GROOVE,
    value=1, command=setMode(1))
    control.grid(row=5, column=1)
    controlButtons.append(control) #controlButtons[5]
    control = Button(root, text="Start", width=8, height=3,
    relief=GROOVE, foreground="red", command=resetGame)
    control.grid(row=5, column=2)
    controlButtons.append(control) #controlButtons[6]

    for i,j in enumerate(layoutGrid):
        button = Button(root, text="", width=8, height=3,
    foreground="blue", command=onClick(j[0]))
    button.grid(row=j[1], column=j[2])
    layoutButtons.append(button)

    def TicTacToe():
        drawMainWindow()
        drawMenuBar()
        drawGraphic()
        mainloop()

    if __name__ == '__main__':
        TicTacToe()