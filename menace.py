"""/************************************/
/*             MENACE               */
/*     Machine Educable Noughts     */
/*       and Crosses Engine         */
/************************************/
/* Based on the first MENACE built  */
/* by Donald Michie in 1960 using   */
/* 304 matchboxes.                  */
/************************************/
/* This implementation was written  */
/*                   by Kade Nylen  */
/************************************/"""

#Import Zelle's button class for the GUI
from button import *
import random
import time

colors=['red','orange','yellow','green','blue','purple','pink','white','brown']

infile=open('matchboxes.txt','r')
matchboxes = []
for line in infile:
    matchboxes.append(line.replace('\n','').split(','))
infile.close()

def updateColor(boxNum):
    #more saturated = more lead?
    arr=[]
    mx = 0
    for i in range(9):
        try:
            box = int(matchboxes[boxNum][i])
            arr.append(box)
            if box > mx:
                mx = box
                arr = []
        except:
            pass
    for i in range(len(arr)):
        if arr[i] == int(mx):
            return "grey"
    return colors[matchboxes[boxNum].index(str(mx))]

win=GraphWin("tic tac toe",1675,1000)
win.setCoords(0,0,38,24)
bg=Rectangle(Point(0,0),Point(38,24))
bg.setFill('black')
bg.draw(win)
box = 0
rects=[]
for x in range(38):
    for y in range(8):
        r=Rectangle(Point(x,y),Point(x+1,y+1))
        r.setFill(updateColor(box))
        box+=1
        rects.append(r)
        r.draw(win)
l=[Line(Point(36,18),Point(24,18)),Line(Point(36,14),Point(24,14)),
Line(Point(32,10),Point(32,22)),Line(Point(28,10),Point(28,22))]
for line in l:
    line.setFill('white')
    line.draw(win)
    
b=[Button(win,Point(26,20),2,2,""),Button(win,Point(30,20),2,2,""),
Button(win,Point(34,20),2,2,""),Button(win,Point(26,16),2,2,""),
Button(win,Point(30,16),2,2,""),Button(win,Point(34,16),2,2,""),
Button(win,Point(26,12),2,2,""),Button(win,Point(30,12),2,2,""),
Button(win,Point(34,12),2,2,"")]
for i in range(9):
    b[i].rect.setFill(colors[i])
    b[i].activate()

infile=open('words.txt','r', encoding="utf-8")
text = []
l = ""
for line in infile:
    if line == "TURN\n":
        text.append(l[:-1])
        l = ""
    else:
        l+=line
infile.close()

textNum = 0
t=Text(Point(11,16),text[textNum])
textNum+=1
t.setFill('white')
t.setSize(25)
t.draw(win)

def updateTxt():
    infile=open('matchboxes.txt','w')
    for box in range(304):
        line=''
        for b in matchboxes[box]:
            line+=str(b)+','
        if box == 303:
            infile.write(line[:-1])
        else:
            infile.write(line[:-1]+'\n')
    infile.close()
    
def click():
    if b[0].clicked(p):
        t.undraw()
        t.setText(text[textNum])
        t.draw(win)
        b[0].rect.setFill('black')
        b[0].deactivate()
        return 0
    if b[1].clicked(p):
        t.undraw()
        t.setText(text[textNum])
        t.draw(win)
        b[1].rect.setFill('black')
        b[1].deactivate()
        return 1
    if b[2].clicked(p):
        t.undraw()
        t.setText(text[textNum])
        t.draw(win)
        b[2].rect.setFill('black')
        b[2].deactivate()
        return 2
    if b[3].clicked(p):
        t.undraw()
        t.setText(text[textNum])
        t.draw(win)
        b[3].rect.setFill('black')
        b[3].deactivate()
        return 3
    if b[4].clicked(p):
        t.undraw()
        t.setText(text[textNum])
        t.draw(win)
        b[4].rect.setFill('black')
        b[4].deactivate()
        return 4
    if b[5].clicked(p):
        t.undraw()
        t.setText(text[textNum])
        t.draw(win)
        b[5].rect.setFill('black')
        b[5].deactivate()
        return 5
    if b[6].clicked(p):
        t.undraw()
        t.setText(text[textNum])
        t.draw(win)
        b[6].rect.setFill('black')
        b[6].deactivate()
        return 6
    if b[7].clicked(p):
        t.undraw()
        t.setText(text[textNum])
        t.draw(win)
        b[7].rect.setFill('black')
        b[7].deactivate()
        return 7
    if b[8].clicked(p):
        t.undraw()
        t.setText(text[textNum])
        t.draw(win)
        b[8].rect.setFill('black')
        b[8].deactivate()
        return 8
        
def chooseBead(boxNum):
    if boxNum == 304:
        return gamePos.index(0)
    arr = {}
    b=0
    for i in range(9):
        try:
            b = int(matchboxes[boxNum][i])
            if b != 0:
                arr[i]=b
        except:
            pass
    summ = sum(arr.values())
    if summ == 0:
        return gamePos.index(0)
    rand = random.randint(1,summ)
    print(arr)
    for i in arr:
        rand -= int(arr[i])
        if rand <= 0:
            if gamePos[i] == 'x' or gamePos[i] == 'o':
                return 'x','x'
            return i,introSym(i,boxNum)
            
def introSym(b,boxNum):
    if b == 4:
        return 4
    arr=[]
    #edges
    if b == 0 or b == 2 or b == 6 or b == 8:
        if matchboxes[boxNum][0] != 'x' and matchboxes[boxNum][0] != 'o':
            if gamePos[0] == 0:
                arr.append(0)
        if matchboxes[boxNum][2] != 'x' and matchboxes[boxNum][2] != 'o':
            if gamePos[2] == 0:
                arr.append(2)
        if matchboxes[boxNum][6] != 'x' and matchboxes[boxNum][6] != 'o':
            if gamePos[6] == 0:
                arr.append(6)
        if matchboxes[boxNum][8] != 'x' and matchboxes[boxNum][8] != 'o':
            if gamePos[8] == 0:
                arr.append(8)
    #sides
    if b == 1 or b == 3 or b == 5 or b == 7:
        if matchboxes[boxNum][1] != 'x' and matchboxes[boxNum][1] != 'o':
            if gamePos[1] == 0:
                arr.append(1)
        if matchboxes[boxNum][3] != 'x' and matchboxes[boxNum][3] != 'o':
            if gamePos[3] == 0:
                arr.append(3)
        if matchboxes[boxNum][5] != 'x' and matchboxes[boxNum][5] != 'o':
            if gamePos[5] == 0:
                arr.append(5)
        if matchboxes[boxNum][7] != 'x' and matchboxes[boxNum][7] != 'o':
            if gamePos[7] == 0:
                arr.append(7)
    if len(arr) > 0:
        return random.choice(arr)
    else:
        return b

rotations=[
    [0,3,6,1,4,7,2,5,8],
    [6,3,0,7,4,1,8,5,2],
    [6,7,8,3,4,5,0,1,2],
    [8,7,6,5,4,3,2,1,0],
    [8,5,2,7,4,1,6,3,0],
    [2,5,8,1,4,7,0,3,6],
    [2,1,0,5,4,3,8,7,6]]
errors = -1

def findBox():
    length=len(moves)
    xArr=[]
    oArr=[]
    for i in range(9):
        if gamePos[i] == 'x':
            xArr.append(i)
        if gamePos[i] == 'o':
            oArr.append(i)
    if length == 1:
        for i in range(1,13):
            match=True
            for x in xArr:
                if matchboxes[i][x] != 'x':
                    match=False
                    break
            if match:
                for o in oArr:
                    if matchboxes[i][o] != 'o':
                        match=False
                        break
            if match:
                return i
    if length == 2:
        for i in range(13,121):
            match=True
            for x in xArr:
                if matchboxes[i][x] != 'x':
                    match=False
                    break
            if match:
                for o in oArr:
                    if matchboxes[i][o] != 'o':
                        match=False
                        break
            if match:
                return i
    if length == 3:
        for i in range(121,304):
            match=True
            for x in xArr:
                if matchboxes[i][x] != 'x':
                    match=False
                    break
            if match:
                for o in oArr:
                    if matchboxes[i][o] != 'o':
                        match=False
                        break
            if match:
                return i
    if length <= 3:
        submit=False
        errors=-1
        while not submit:
            errors+=1
            if errors > 6:
                print('Failed rotations test')
                raise Exception('Failed rotations test.')
                break
            tempPos=[0,0,0,0,0,0,0,0,0]
            r=0
            for i in rotations[errors]:
                tempPos[r]= gamePos[i]
                r+=1
            xArr=[]
            oArr=[]
            for i in range(0,9):
                if tempPos[i] == 'x':
                    xArr.append(i)
                if tempPos[i] == 'o':
                    oArr.append(i)
            if length == 1:
                for i in range(1,13):
                    match=True
                    for x in xArr:
                        if matchboxes[i][x] != 'x':
                            match=False
                            break
                    if match:
                        for o in oArr:
                            if matchboxes[i][o] != 'o':
                                match=False
                                break
                    if match:
                        return i
            if length == 2:
                for i in range(13,121):
                    match=True
                    for x in xArr:
                        if matchboxes[i][x] != 'x':
                            match=False
                            break
                    if match:
                        for o in oArr:
                            if matchboxes[i][o] != 'o':
                                match=False
                                break
                    if match:
                        return i
            if length == 3:
                for i in range(121,304):
                    match=True
                    for x in xArr:
                        if matchboxes[i][x] != 'x':
                            match=False
                            break
                    if match:
                        for o in oArr:
                            if matchboxes[i][o] != 'o':
                                match=False
                                break
                    if match:
                        return i
    else:
        raise Exception("You're fucked.")
    return 304
   
def resurrect():
    matchboxes[0]=[0,0,0,0,8,0,0,8,8]
    
nax=[]
    
def drawGamePos():
    for obj in nax:
        obj.undraw()
    nax.clear()
    for i in range(9):
        if gamePos[i] == 'x':
            if i == 0:
                l1=Line(Point(25,21),Point(27,19))#24,22, 28,18
                l2=Line(Point(25,19),Point(27,21))
                l1.setFill('white')
                l2.setFill('white')
                nax.append(l1)
                nax.append(l2)
            if i == 1:
                l1=Line(Point(29,21),Point(31,19))
                l2=Line(Point(29,19),Point(31,21))
                l1.setFill('white')
                l2.setFill('white')
                nax.append(l1)
                nax.append(l2)
            if i == 2:
                l1=Line(Point(33,21),Point(35,19))#32,22, 36,18
                l2=Line(Point(33,19),Point(35,21))#32,18, 36,22
                l1.setFill('white')
                l2.setFill('white')
                nax.append(l1)
                nax.append(l2)
            if i == 3:
                l1=Line(Point(25,17),Point(27,15))
                l2=Line(Point(25,15),Point(27,17))
                l1.setFill('white')
                l2.setFill('white')
                nax.append(l1)
                nax.append(l2)
            if i == 4:
                l1=Line(Point(29,17),Point(31,15))
                l2=Line(Point(29,15),Point(31,17))
                l1.setFill('white')
                l2.setFill('white')
                nax.append(l1)
                nax.append(l2)
            if i == 5:
                l1=Line(Point(33,17),Point(35,15))
                l2=Line(Point(33,15),Point(35,17))
                l1.setFill('white')
                l2.setFill('white')
                nax.append(l1)
                nax.append(l2)
            if i == 6:
                l1=Line(Point(25,13),Point(27,11))
                l2=Line(Point(25,11),Point(27,13))
                l1.setFill('white')
                l2.setFill('white')
                nax.append(l1)
                nax.append(l2)
            if i == 7:
                l1=Line(Point(29,13),Point(31,11))
                l2=Line(Point(29,11),Point(31,13))
                l1.setFill('white')
                l2.setFill('white')
                nax.append(l1)
                nax.append(l2)
            if i == 8:
                l1=Line(Point(33,13),Point(35,11))
                l2=Line(Point(33,11),Point(35,13))
                l1.setFill('white')
                l2.setFill('white')
                nax.append(l1)
                nax.append(l2)
        if gamePos[i] == 'o':
            if i == 0:
                c1=Circle(Point(26,20),1)
                c2=Circle(Point(26,20),0.9)
                c1.setFill('white')
                c2.setFill('black')
                nax.append(c1)
                nax.append(c2)
            if i == 1:
                c1=Circle(Point(30,20),1)
                c2=Circle(Point(30,20),0.9)
                c1.setFill('white')
                c2.setFill('black')
                nax.append(c1)
                nax.append(c2)
            if i == 2:
                c1=Circle(Point(34,20),1)
                c2=Circle(Point(34,20),0.9)
                c1.setFill('white')
                c2.setFill('black')
                nax.append(c1)
                nax.append(c2)
            if i == 3:
                c1=Circle(Point(26,16),1)
                c2=Circle(Point(26,16),0.9)
                c1.setFill('white')
                c2.setFill('black')
                nax.append(c1)
                nax.append(c2)
            if i == 4:
                c1=Circle(Point(30,16),1)
                c2=Circle(Point(30,16),0.9)
                c1.setFill('white')
                c2.setFill('black')
                nax.append(c1)
                nax.append(c2)
            if i == 5:
                c1=Circle(Point(34,16),1)
                c2=Circle(Point(34,16),0.9)
                c1.setFill('white')
                c2.setFill('black')
                nax.append(c1)
                nax.append(c2)
            if i == 6:
                c1=Circle(Point(26,12),1)
                c2=Circle(Point(26,12),0.9)
                c1.setFill('white')
                c2.setFill('black')
                nax.append(c1)
                nax.append(c2)
            if i == 7:
                c1=Circle(Point(30,12),1)
                c2=Circle(Point(30,12),0.9)
                c1.setFill('white')
                c2.setFill('black')
                nax.append(c1)
                nax.append(c2)
            if i == 8:
                c1=Circle(Point(34,12),1)
                c2=Circle(Point(34,12),0.9)
                c1.setFill('white')
                c2.setFill('black')
                nax.append(c1)
                nax.append(c2)
    for obj in nax:
        obj.draw(win)
        
def checkWin():
    #all horizontal lines
    if gamePos[:3] == ['x','x','x']:
        return 'playerWin'
    elif gamePos[3:6] == ['x','x','x']:
        return 'playerWin'
    elif gamePos[6:] == ['x','x','x']:
        return 'playerWin'
    elif gamePos[:3] == ['o','o','o']:
        return 'menaceWin'
    elif gamePos[3:6] == ['o','o','o']:
        return 'menaceWin'
    elif gamePos[6:] == ['o','o','o']:
        return 'menaceWin'
    #top left -> bottom right diagonal
    elif gamePos[:1] == ['x'] and gamePos[4:5] == ['x'] and gamePos[8:] == ['x']:
        return 'playerWin'
    elif gamePos[:1] == ['o'] and gamePos[4:5] == ['o'] and gamePos[8:] == ['o']:
        return 'menaceWin'
    #top right -> bottom left diagonal
    elif gamePos[2:3] == ['x'] and gamePos[4:5] == ['x'] and gamePos[6:7] == ['x']:
        return 'playerWin'
    elif gamePos[2:3] == ['o'] and gamePos[4:5] == ['o'] and gamePos[6:7] == ['o']:
        return 'menaceWin'
    #left vertical
    elif gamePos[:1] == ['x'] and gamePos[3:4] == ['x'] and gamePos[6:7] == ['x']:
        return 'playerWin'
    elif gamePos[:1] == ['o'] and gamePos[3:4] == ['o'] and gamePos[6:7] == ['o']:
        return 'menaceWin'
    #middle vertical
    elif gamePos[1:2] == ['x'] and gamePos[4:5] == ['x'] and gamePos[7:8] == ['x']:
        return 'playerWin'
    elif gamePos[1:2] == ['o'] and gamePos[4:5] == ['o'] and gamePos[7:8] == ['o']:
        return 'menaceWin'
    #right vertical
    elif gamePos[2:3] == ['x'] and gamePos[5:6] == ['x'] and gamePos[8:] == ['x']:
        return 'playerWin'
    elif gamePos[2:3] == ['o'] and gamePos[5:6] == ['o'] and gamePos[8:] == ['o']:
        return 'menaceWin'
    return ''
        
def winUpdate():
    print(gamePos)
    print('won')
    for box,move in moves.items():
        matchboxes[box][move]=int(matchboxes[box][move])+3
        matchboxes[box][move]=str(matchboxes[box][move])
        rects[box].undraw()
        rects[box].setFill(updateColor(box))
        rects[box].draw(win)
        
def loseUpdate():
    print(gamePos)
    print('lost')
    for box,move in moves.items():
        matchboxes[box][move]=int(matchboxes[box][move])-1
        matchboxes[box][move]=str(matchboxes[box][move])
        rects[box].undraw()
        rects[box].setFill(updateColor(box))
        rects[box].draw(win)
        
def drawUpdate():
    print(gamePos)
    print('draw')
    for box,move in moves.items():
        matchboxes[box][move]=int(matchboxes[box][move])+1
        matchboxes[box][move]=str(matchboxes[box][move])
        rects[box].undraw()
        rects[box].setFill(updateColor(box))
        rects[box].draw(win)

gameFinished=False
moves={}
gamePos=[0,0,0,0,0,0,0,0,0]

x,y = chooseBead(0)
moves[0]=x
gamePos[y]='o'
b[y].rect.setFill('black')
b[y].deactivate()
drawGamePos()

games=0

gameResult=Text(Point(30,9),"")
gameResult.setFill('white')
gameResult.setSize(25)
gameResult.draw(win)

loops=0
while textNum < len(text):
    loops+=1
    print(loops)
    if gameFinished:
        drawGamePos()
        time.sleep(1)
        gameResult.undraw()
        gameResult.setText('')
        gameResult.draw(win)
        games+=1
        print(games)
        for i in range(9):
            b[i].rect.setFill(colors[i])
            b[i].activate()
        updateTxt()
        moves={}
        gamePos=[0,0,0,0,0,0,0,0,0]
        for i in range(9):
            b[i].rect.setFill(colors[i])
        x,y = chooseBead(0)
        moves[0]=x
        gamePos[y]='o'
        b[y].rect.setFill('black')
        b[y].deactivate()
        drawGamePos()
    gameFinished=False
    p=win.getMouse()
    try:
        gamePos[click()]='x'
        textNum+=1
    except:
        continue
    if len(moves)>=2:
        winCheck = checkWin()
        if winCheck == 'playerWin':
            gameResult.undraw()
            gameResult.setText('MACHINE LOST')
            gameResult.draw(win)
            loseUpdate()
            gameFinished = True
            continue
        if winCheck == 'menaceWin':
            gameResult.undraw()
            gameResult.setText('MACHINE WON')
            gameResult.draw(win)
            winUpdate()
            gameFinished = True
            continue
        try:
            gamePos.index(0)
        except:
            if winCheck == 'playerWin':
                gameResult.undraw()
                gameResult.setText('MACHINE LOST')
                gameResult.draw(win)
                loseUpdate()
                gameFinished = True
                continue
            if winCheck == 'menaceWin':
                gameResult.undraw()
                gameResult.setText('MACHINE WON')
                gameResult.draw(win)
                winUpdate()
                gameFinished = True
                continue
            if winCheck == '':
                gameResult.undraw()
                gameResult.setText("IT'S A DRAW")
                gameResult.draw(win)
                drawUpdate()
                gameFinished = True
                continue
    #def menaceTurn():
    try:
        box = findBox()
    except:
        if len(moves)>=2:
            winCheck = checkWin()
            if winCheck == 'playerWin':
                gameResult.undraw()
                gameResult.setText('MACHINE LOST')
                gameResult.draw(win)
                loseUpdate()
                gameFinished = True
                continue
            if winCheck == 'menaceWin':
                gameResult.undraw()
                gameResult.setText('MACHINE WON')
                gameResult.draw(win)
                winUpdate()
                gameFinished = True
                continue
            try:
                gamePos.index(0)
            except:
                if winCheck == 'playerWin':
                    gameResult.undraw()
                    gameResult.setText('MACHINE LOST')
                    gameResult.draw(win)
                    loseUpdate()
                    gameFinished = True
                    continue
                if winCheck == 'menaceWin':
                    gameResult.undraw()
                    gameResult.setText('MACHINE WON')
                    gameResult.draw(win)
                    winUpdate()
                    gameFinished = True
                    continue
                if winCheck == '':
                    gameResult.undraw()
                    gameResult.setText("IT'S A DRAW")
                    gameResult.draw(win)
                    drawUpdate()
                    gameFinished = True
                    continue
    x,y = chooseBead(box)
    failSafe = False
    if x == 'x':
        for redo in range(3):
            x,y = chooseBead(box)
            print(box)
            print('beads: ' + str(x) + ' (' + str(y) + ')')
            if x != 'x':
                break
    if x == 'x':
        x = gamePos.index(0)
        y = gamePos.index(0) 
        print(box)  
        print('beads: ' + str(x) + ' (' + str(y) + ')') 
        failSafe = True            
    moves[box]=x
    if failSafe:
        moves.pop(box)
    gamePos[y]='o'
    b[y].rect.setFill('black')
    b[y].deactivate()
    if len(moves)>2:
        winCheck = checkWin()
        if winCheck == 'playerWin':
            gameResult.undraw()
            gameResult.setText('MACHINE LOST')
            gameResult.draw(win)
            loseUpdate()
            gameFinished = True
            continue
        if winCheck == 'menaceWin':
            gameResult.undraw()
            gameResult.setText('MACHINE WON')
            gameResult.draw(win)
            winUpdate()
            gameFinished = True
            continue
        try:
            gamePos.index(0)
        except:
            if winCheck == 'playerWin':
                gameResult.undraw()
                gameResult.setText('MACHINE LOST')
                gameResult.draw(win)
                loseUpdate()
                gameFinished = True
                continue
            if winCheck == 'menaceWin':
                gameResult.undraw()
                gameResult.setText('MACHINE WON')
                gameResult.draw(win)
                winUpdate()
                gameFinished = True
                continue
            if winCheck == '':
                gameResult.undraw()
                gameResult.setText("IT'S A DRAW")
                gameResult.draw(win)
                drawUpdate()
                gameFinished = True
                continue
    drawGamePos()
drawGamePos()
p=win.getMouse()
gameResult.undraw()
gameResult.setText("GAME OVER")
gameResult.draw(win)
