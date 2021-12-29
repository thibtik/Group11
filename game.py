
import tkinter as tk
import winsound
import random
root=tk.Tk()
root.geometry('1440x1024')
frame=tk.Frame()
frame.master.title('Game VC1')
cavas=tk.Canvas(frame)
#------- ---Variable--------
score=0
lifeOfUser=3
key = False
box = False

#---------------------NOTE-----------#
                #       0 = walls     #
                #       1 = player    #
                #       2 = Treasure  #
                #       3 = enamy     #
                #       4 = key       #
                #       5=dimand      #
                #       6 = space     #
                #       8 = coin      #
                #-----------------------#
#--------------Display image----------
marioImage = tk.PhotoImage(file='image/mario.png')
imageMonster=tk.PhotoImage(file='image/monster.png')
imageTreasure=tk.PhotoImage(file='image/treasure.png')
imageDimand=tk.PhotoImage(file='image/dimand.png')
life=tk.PhotoImage(file='image/life.png')
imageKey=tk.PhotoImage(file='image/key.png')
imagecoin=tk.PhotoImage(file='image/coin.png')
imagebg=tk.PhotoImage(file='image/bggame.png')
bgLost = tk.PhotoImage(file="image/bglost.png")
bgWin = tk.PhotoImage(file="image/bgwin.png")
bgStart = tk.PhotoImage(file="image/bgstart.png")
bgLevel = tk.PhotoImage(file="image/bglevel.png")                                      
brickBrown = tk.PhotoImage(file="image/brickBrown.png")  
grid = [    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,5,6,5,5,5,5,5,5,5,5,5,5,0,5,5,5,5,6,6,6,3,6,6,6,0],
                [0,5,3,0,0,0,0,0,0,0,0,5,5,0,5,5,5,5,0,0,0,0,0,0,6,0],
                [0,5,6,6,6,0,5,5,8,5,5,6,6,0,0,0,0,0,0,0,0,0,5,6,6,0],
                [0,0,0,0,6,0,0,0,0,0,0,0,6,5,5,5,5,5,5,5,8,5,5,6,5,0],
                [0,5,5,5,6,6,6,5,5,5,0,3,6,6,6,5,5,5,5,5,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,8,0,5,0,0,0,0,0,5,0,0,0,0,0,5,5,5,0],
                [0,5,6,6,6,6,5,5,5,0,5,0,5,5,5,5,6,5,5,5,5,5,5,3,5,0],
                [0,5,0,5,3,0,0,0,5,5,5,0,5,5,5,5,6,6,0,5,5,6,6,6,5,0],
                [0,5,0,0,0,5,5,0,0,0,0,0,0,0,0,0,3,6,0,5,5,6,0,0,0,0],
                [0,5,0,3,6,5,5,5,5,5,4,0,5,5,5,5,5,6,0,5,5,5,0,2,5,0],
                [0,5,0,6,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,8,0,5,5,0],
                [0,5,5,5,0,5,8,5,5,5,6,6,3,5,5,5,5,5,5,5,5,5,0,5,5,0],
                [0,0,0,0,0,0,0,0,5,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,5,0],
                [0,5,5,5,5,5,5,5,5,5,5,5,8,5,5,5,5,5,5,5,5,5,5,5,5,0],
                [0,6,6,6,3,5,5,5,5,5,0,0,0,5,5,5,5,5,0,3,6,0,5,5,5,0],
                [0,6,0,0,0,0,0,0,0,0,5,0,5,5,5,5,5,5,5,5,6,5,5,5,5,0],
                [0,6,6,5,5,6,3,6,6,5,5,0,5,0,0,0,0,0,0,0,0,0,0,0,5,0],
                [0,8,5,5,5,0,5,3,3,3,1,0,5,5,5,5,5,5,5,5,5,5,5,0,5,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

#---------------------------------------Drawing---------------------
def arrayToDrawing():
    global lifeOfUser,score
    cavas.delete("all")
    cavas.create_image(0,0,image=imagebg,anchor='nw')
    y1=10
    y2=40
    positionXOfUser = 1290
    if lifeOfUser > 0 :
        for value in grid:
            x1=80
            x2=110
            for j in value:
                if j==0:
                    cavas.create_image(x1+30,y1+30, image=brickBrown, anchor='nw')
                elif j==1:
                    cavas.create_image(x1+30,y1+30, image=marioImage, anchor='nw')
                elif j==2:
                    cavas.create_image(x1+30,y1+30, image=imageTreasure, anchor='nw')   
                elif j==3:
                    cavas.create_image(x1+30,y1+30, image=imageMonster, anchor='nw')
                elif j==4:
                    cavas.create_image(x1+30,y1+30, image=imageKey, anchor='nw')  
                elif j==5:
                    cavas.create_image(x1+30,y1+30, image=imageDimand, anchor='nw')                                       
                elif j==8:
                    cavas.create_image(x1+30,y1+30, image=imagecoin, anchor='nw')                                       
                x1=x2
                x2+=30
            y1=y2
            y2+=30
#------------------------Display Lost and Win---------------------
        if key and box:
            userWin()   
    elif lifeOfUser==0:
        userLost()       
#------------------------heart and score-----------------------
    for i in range(lifeOfUser):
        cavas.create_image(positionXOfUser,15, image=life , anchor = "nw", tags="heart")
        positionXOfUser -= 50
    cavas.create_text(1250, 90, text = "Your score: "+str(score), fill="darkblue", font="consolas 15", tags="score")

#------------------------Funtion Lost and Win---------------------
def userLost():
    cavas.delete("all")
    cavas.create_image(0,0,image=bgLost,anchor='nw')
    cavas.create_text(700,390, text="Game Over", font=('Roboto', "70"),fill='purple',tags='lost')
    winsound .PlaySound('sound/gameover5.wav', winsound.SND_FILENAME)
    cavas.create_rectangle(660, 470, 800, 530, outline="black", fill="orange", tags="comeback")
    cavas.create_text(730,500, text = "Try again", fill="darkblue", font="consolas 20", tags="comeback")
def userWin():
    cavas.delete('all')
    cavas.create_image(0,0,image=bgWin, anchor='nw')
    cavas.create_text(700,390, text="You Win", font=('Roboto', "70"),fill='black')

    cavas.create_rectangle(660, 470, 800, 530, outline="black", fill="orange", tags="comebackwin")
    cavas.create_text(730,500, text = "Next", fill="darkblue", font="consolas 20", tags="comebackwin")

def Easy(event):
    global grid, lifeOfUser,score
    grid = [    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,5,6,5,5,5,5,5,5,5,5,5,5,0,5,5,5,5,6,6,6,3,6,6,6,0],
                [0,5,3,0,0,0,0,0,0,0,0,5,5,0,5,5,5,5,0,0,0,0,0,0,6,0],
                [0,5,6,6,6,0,5,5,8,5,5,6,6,0,0,0,0,0,0,0,0,0,5,6,6,0],
                [0,0,0,0,6,0,0,0,0,0,0,0,6,5,5,5,5,5,5,5,8,5,5,6,5,0],
                [0,5,5,5,6,6,6,5,5,5,0,3,6,6,6,5,5,5,5,5,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,8,0,5,0,0,0,0,0,5,0,0,0,0,0,5,5,5,0],
                [0,5,6,6,6,6,5,5,5,0,5,0,5,5,5,5,6,5,5,5,5,5,5,3,5,0],
                [0,5,0,5,3,0,0,0,5,5,5,0,5,5,5,5,6,6,0,5,5,6,6,6,5,0],
                [0,5,0,0,0,5,5,0,0,0,0,0,0,0,0,0,3,6,0,5,5,6,0,0,0,0],
                [0,5,0,3,6,5,5,5,5,5,4,0,5,5,5,5,5,6,0,5,5,5,0,2,5,0],
                [0,5,0,6,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,8,0,5,5,0],
                [0,5,5,5,0,5,8,5,5,5,6,6,3,5,5,5,5,5,5,5,5,5,0,5,5,0],
                [0,0,0,0,0,0,0,0,5,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,5,0],
                [0,5,5,5,5,5,5,5,5,5,5,5,8,5,5,5,5,5,5,5,5,5,5,5,5,0],
                [0,6,6,6,3,5,5,5,5,5,0,0,0,5,5,5,5,5,0,3,6,0,5,5,5,0],
                [0,6,0,0,0,0,0,0,0,0,5,0,5,5,5,5,5,5,5,5,6,5,5,5,5,0],
                [0,6,6,5,5,6,3,6,6,5,5,0,5,0,0,0,0,0,0,0,0,0,0,0,5,0],
                [0,8,5,5,5,0,5,3,3,3,1,0,5,5,5,5,5,5,5,5,5,5,5,0,5,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    arrayToDrawing()

def medium(event):
    global grid,lifeOfUser,score
    grid = [    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,5,5,5,5,5,5,5,5,5,0,3,6,6,6,5,5,5,5,5,5,5,5,5,0],
                [0,0,0,0,0,0,0,0,6,0,0,0,0,0,0,5,5,0,0,0,0,5,5,5,5,0],
                [0,5,5,5,5,0,5,5,8,5,5,6,6,5,5,5,5,5,0,5,5,5,0,0,0,0],
                [0,0,0,0,5,0,3,6,0,0,5,5,0,0,0,0,0,0,0,5,5,5,5,6,3,0],
                [0,5,0,5,5,0,5,5,5,5,5,5,6,6,3,0,5,5,5,5,8,5,5,5,5,0],
                [0,5,0,5,5,0,0,0,0,0,0,0,0,0,0,0,5,5,0,0,0,0,0,0,6,0],
                [0,5,0,5,5,5,5,5,5,5,5,5,5,5,5,0,5,5,5,5,5,0,5,5,5,0],
                [0,5,0,3,6,6,5,5,0,0,0,0,0,0,0,0,5,0,0,5,5,0,5,5,5,0],
                [0,5,0,0,0,5,5,5,5,0,5,5,0,5,5,5,5,5,8,5,5,0,5,5,5,0],
                [0,6,6,5,5,0,0,0,5,0,5,5,0,5,5,5,0,0,0,0,0,0,0,0,0,0],
                [0,3,6,0,5,5,5,5,5,0,5,0,0,0,0,5,5,5,6,6,6,3,5,0,4,0],
                [0,0,0,0,0,0,0,5,5,0,5,0,3,6,6,6,5,5,5,5,5,5,5,0,6,0],
                [0,2,5,6,5,0,5,5,5,5,5,0,5,5,0,0,0,0,0,0,0,0,0,0,5,0],
                [0,5,0,0,5,0,3,6,6,5,5,0,0,3,6,5,5,0,5,5,6,6,3,0,5,0],
                [0,5,0,5,0,0,0,0,0,5,5,5,5,8,5,5,5,0,5,0,0,5,6,5,5,0],
                [0,5,5,5,5,8,5,5,5,5,5,0,0,0,0,0,5,0,5,0,5,5,6,0,5,0],
                [0,0,0,0,0,0,0,0,0,5,5,5,0,6,5,5,5,5,5,0,0,0,0,0,0,0],
                [0,3,6,6,6,5,5,5,5,5,5,5,0,3,5,5,5,8,5,5,5,5,5,5,5,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    arrayToDrawing()

def difficult(event):
    global grid,lifeOfUser,score
    grid = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,5,5,5,5,6,6,3,6,5,5,0,1,5,5,5,5,6,6,6,3,6,5,5,0,2,5,5,5,5,5,0],
            [0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,0,0,0,0,0,0,6,6,6,3,5,5,0],
            [0,5,0,5,5,0,5,6,5,5,5,0,5,0,5,5,5,5,8,5,5,5,5,5,0,5,0,0,0,0,0,0],
            [0,5,5,5,5,0,5,3,0,5,5,0,5,0,0,0,0,0,0,5,6,0,5,5,0,5,5,8,5,5,5,0],
            [0,5,0,5,5,0,5,6,0,5,4,0,5,5,0,5,5,5,0,5,6,0,5,5,0,5,5,0,0,0,0,0],
            [0,5,0,5,5,0,5,0,0,0,0,0,0,5,0,5,0,5,0,6,3,0,5,5,0,5,8,5,6,5,5,0],
            [0,5,0,5,5,5,5,5,0,5,5,0,5,6,0,5,0,5,5,5,5,0,5,0,0,0,0,0,6,0,5,0],
            [0,5,0,0,0,0,0,0,0,0,6,0,6,3,0,5,0,0,0,0,0,0,5,5,0,5,5,5,6,0,5,0],
            [0,5,5,5,8,5,5,0,6,3,6,0,6,6,0,5,0,5,5,8,5,0,5,5,0,5,5,5,3,0,5,0],
            [0,6,3,6,0,5,5,5,5,5,6,0,5,5,5,5,0,5,0,0,5,0,0,0,0,0,0,0,0,0,5,0],
            [0,0,0,0,0,0,0,0,0,0,5,0,5,0,5,5,0,5,5,0,5,0,3,6,0,5,0,5,5,0,5,0],
            [0,3,6,6,5,5,5,5,5,0,5,5,5,0,5,5,0,5,5,5,8,5,6,6,5,5,0,6,3,0,5,0],
            [0,6,0,6,6,0,0,0,0,0,0,0,5,0,0,0,0,0,0,5,5,0,0,0,0,0,0,6,6,0,5,0],
            [0,5,0,6,6,6,5,5,5,5,8,5,5,0,5,6,3,0,0,0,5,5,5,5,5,8,5,5,5,5,5,0],
            [0,5,0,0,0,0,5,5,5,5,5,5,5,0,5,6,6,0,5,0,5,5,5,5,5,5,5,5,5,5,5,0],
            [0,5,0,5,5,0,5,5,0,5,0,0,0,0,0,0,6,5,5,5,5,0,0,0,0,0,0,0,0,0,0,0],
            [0,5,0,5,5,0,0,0,0,0,0,5,0,5,0,0,0,0,0,0,5,5,5,5,8,5,5,5,5,5,5,0],
            [0,5,5,5,5,5,5,5,5,6,3,6,6,5,5,5,8,5,5,5,5,0,0,0,0,0,0,5,5,5,5,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    arrayToDrawing()
# -----------------------Monsterposition-----------------------------------
move=[]
def moveenimy(grid):
    enimey=[]
    for index in range(len(grid)):
        for col in range(len(grid[index])):
            if grid[index][col]==3:
                enimey.append([index,col])
    print(enimey)
    return enimey
def moveingrid(grid,right,col):
    move=[]
    if (grid[right][col-1]==6):
        move.append("left")
    if (grid[right][col+1]==6 ):
        move.append("right")
    if (grid[right-1][col]==6):
        move.append("up")
    if (grid[right+1][col]==6):
        move.append("down")
    return move
def canmove():
    global lifeOfUser
    getindexenimy=moveenimy(grid)
    print(getindexenimy)
    for enemy in getindexenimy:
        rowindex=enemy[0]
        colindex=enemy[1]
        wheretogo=moveingrid(grid,rowindex,colindex)
        if len(wheretogo)>0:
            move=random.choice(wheretogo)
            print(move)
            if move=="left":
                if grid[rowindex][colindex-1]==6 and grid[rowindex][colindex-1]!=1:
                    grid[rowindex][colindex]=6
                    grid[rowindex][colindex-1]=3
            if move=="right":
                if grid[rowindex][colindex+1]==6 and grid[rowindex][colindex+1]!=1:
                    grid[rowindex][colindex]=6
                    grid[rowindex][colindex+1]=3
            if move=="up":
                if grid[rowindex-1][colindex]==6 and grid[rowindex-1][colindex]!=1:
                    grid[rowindex][colindex]=6
                    grid[rowindex-1][colindex]=3
            if move=="down":
                if grid[rowindex+1][colindex]==6 and grid[rowindex+1][colindex]!=1:
                    grid[rowindex][colindex]=6
                    grid[rowindex+1][colindex]=3
    arrayToDrawing()
    cavas.after(450,canmove)   
cavas.delete("all")
cavas.after(22000,canmove)     
arrayToDrawing()

#---------------------Get index-------------------
def getIndexRow(grid):
    for i in range(len(grid)):
        if 1 in grid[i]:
            return i          

def getIndexCol(grid):
    row = getIndexRow(grid)
    for col in range(len(grid[row])):
        if grid[row][col] == 1:
            return col
    arrayToDrawing()

# -----------------Player move( left, right, up, down)----------------
def moveRight(event):
    global score,lifeOfUser,key,box
    indexRow=getIndexRow(grid)
    indexCol=getIndexCol(grid)
    if indexCol+1 < len(grid[indexRow])-1 and grid[indexRow][indexCol+1] != 0  :
        grid[indexRow][indexCol]=6
        if grid[indexRow][indexCol+1] == 5:
            score += 10
            winsound .PlaySound('sound/dimand.wav', winsound.SND_FILENAME)
        if grid[indexRow][indexCol+1] == 8:
            score += 20
        elif grid[indexRow][indexCol+1]==3:
            winsound .PlaySound('sound/touched.wav', winsound.SND_FILENAME)
            lifeOfUser-=1
        if grid[indexRow][indexCol+1]==2:
            key=True
        if grid[indexRow][indexCol+1]==4:
            box=True
        grid[indexRow][indexCol+1]=1
    arrayToDrawing()

def moveLeft(event):
    global score,lifeOfUser,key,box
    indexRow=getIndexRow(grid)
    indexCol=getIndexCol(grid)
    if indexCol>1 and grid[indexRow][indexCol-1] != 0 :
        grid[indexRow][indexCol]=6
        if grid[indexRow][indexCol-1]==5:
            score +=10
            winsound .PlaySound('sound/dimand.wav', winsound.SND_FILENAME)
        if grid[indexRow][indexCol-1]==8:
            score +=20
        elif grid[indexRow][indexCol-1]==3 :
            winsound .PlaySound('sound/touched.wav', winsound.SND_FILENAME)
            lifeOfUser-=1
        if grid[indexRow][indexCol-1]==2:
            key=True
        if grid[indexRow][indexCol-1]==4:
            box=True
        grid[indexRow][indexCol-1]=1

    arrayToDrawing()
arrayToDrawing()
def moveDown(event):
    global score,lifeOfUser,key,box
    indexRow=getIndexRow(grid)
    indexCol=getIndexCol(grid)
    if indexRow+1 < len(grid[0])-1 and grid[indexRow+1][indexCol] != 0 :
        grid[indexRow][indexCol]=6
        if grid[indexRow+1][indexCol]==5:
            score+=10
            winsound .PlaySound('sound/dimand.wav', winsound.SND_FILENAME)
        if grid[indexRow+1][indexCol]==8:
            score+=20
            winsound .PlaySound('sound/dimand.wav', winsound.SND_FILENAME)
        elif grid[indexRow+1][indexCol]==3:
            winsound .PlaySound('sound/touched.wav', winsound.SND_FILENAME)
            lifeOfUser-=1
        if grid[indexRow+1][indexCol]==2:
            key=True
        if grid[indexRow+1][indexCol]==4:
            box=True
        grid[indexRow+1][indexCol]=1
    arrayToDrawing()
def moveUp(event):
    global score,lifeOfUser,key,box
    indexRow=getIndexRow(grid)
    indexCol=getIndexCol(grid)
    if indexRow>1 and grid[indexRow-1][indexCol] != 0 :
        grid[indexRow][indexCol]=6
        if grid[indexRow-1][indexCol]==5:
            score+=10
            winsound .PlaySound('sound/dimand.wav', winsound.SND_FILENAME)
        if grid[indexRow-1][indexCol]==5:
            score+=20
        elif grid[indexRow-1][indexCol]==3:
            winsound .PlaySound('sound/touched.wav', winsound.SND_FILENAME)
            lifeOfUser-=1
        if grid[indexRow-1][indexCol]==2:
            key=True
        if grid[indexRow-1][indexCol]==4:
            box=True
        grid[indexRow-1][indexCol]=1
    arrayToDrawing()                                                                    
#------------------------scenBack-----------------------

def back(event):
    cavas.delete("easy")
    cavas.delete("medium")
    cavas.delete("difficult")
    cavas.delete("Back")
    graphic()
def comeback(event):
    global lifeOfUser, score
    lifeOfUser=3
    score=0
    cavas.delete("easy")
    cavas.delete("medium")
    cavas.delete("difficult")
    cavas.delete("lost")
    cavas.delete('backg')
    cavas.delete("start")
    Easy()
    medium()
    difficult()
    graphic()

def ScenBack(event):
    cavas.delete("ScenBack")
    cavas.delete("Scenarios")
    cavas.delete("easy")
    cavas.delete("medium")
    cavas.delete("difficult")
def Scenario(event):
    cavas.create_rectangle(200, 150,800,650, outline="pink", fill="pink", tags="Scenarios")
    cavas.create_text(510,280, text = "Follow by this scenario", fill="black", font="consolas 15 bold", tags="Scenarios")
    cavas.create_text(510,350, text = "1. You need to find key and treasure to win.", fill="black", font="consolas 15", tags="Scenarios")
    cavas.create_text(510,400, text = "2. If you can find key and treasure you will win.", fill="black", font="consolas 15", tags="Scenarios")
    cavas.create_text(510,450, text = "3. But if you cannot find you will lose.", fill="black", font="consolas 15", tags="Scenarios")
    cavas.create_text(510,500, text = "4. If enemies touch you will lose also", fill="black", font="consolas 15 ", tags="Scenarios")
    
    cavas.create_rectangle(220, 170, 290, 220, fill="purple", outline="purple", tags ="ScenBack")
    cavas.create_text(255,195, text = "Back", fill="white", font="consolas 15 ", tags="ScenBack")
def start(event):
    global bgLevel,lifeOfUser
    cavas.create_image( 0, 0, image = bgLevel, anchor = "nw")
    cavas.create_rectangle(240, 410, 490, 490, outline="", fill="purple", tags="easy")
    cavas.create_text(350, 440, text = "Easy", fill="orange", font="consolas 50", tags="easy")

    cavas.create_rectangle(950, 410, 1200, 490, outline="", fill="purple", tags="medium")
    cavas.create_text(1070, 440, text = "Medium", fill="orange", font="consolas 50", tags="medium")

    cavas.create_rectangle(540, 510, 900, 590, outline="", fill="purple", tags="difficult")
    cavas.create_text(730, 550, text = "Difficult", fill="orange", font="consolas 50", tags="difficult")

    cavas.create_rectangle(20, 40, 100, 90, outline="black", fill="orange", tags="Back")
    cavas.create_text(60,65, text = "Back", fill="darkblue", font="consolas 15", tags="Back")
def graphic():
    cavas.create_image( 0, 0, image = bgStart, anchor = "nw")
    cavas.create_rectangle(540,220,740,280, fill='purple', tags='Start')
    cavas.create_text(630,250,text='Start', fill='white', font='consolas 30', tags='Start')
    cavas.create_rectangle(500,310,780,370, fill='purple', tags='Scenario')
    cavas.create_text(640,335,text='Scenario', fill='white',font='consolas 30', tags='Scenario')
graphic()

cavas.tag_bind("Start", "<Button-1>", start)
cavas.tag_bind("Scenario", "<Button-1>", Scenario)
cavas.tag_bind("easy", "<Button-1>", Easy)
cavas.tag_bind("medium", "<Button-1>", medium)
cavas.tag_bind("difficult", "<Button-1>", difficult)
cavas.tag_bind("ScenBack", "<Button-1>", ScenBack)
cavas.tag_bind("Back", "<Button-1>", back)
cavas.tag_bind("comeback", "<Button-1>",comeback )
root.bind('<Right>',moveRight) 
root.bind('<Up>',moveUp)
root.bind('<Down>',moveDown)
root.bind('<Left>',moveLeft)
cavas.pack(expand=True,fill='both')
frame.pack(expand=True,fill='both')
root.mainloop()