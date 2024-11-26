import numpy as np
 
""
veri=[[1, 1, 1, 1, 1, 1, 1, 1],
      [0, 0, 1, 1, 0, 0, 0, 0],
      [1, 0, 1, 1, 0, 1, 1, 1],
      [1, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 1, 0, 1, 1, 0, 1],
      [1, 0, 1, 1, 0, 1, 0, 1],
      [1, 0, 0, 1, 0, 0, 0, 1],
      [1, 1, 1, 1, 1, 1, 1, 1]] 
 
correctpath = np.zeros((8,8),dtype=int)

matris = np.zeros((8,8),dtype=int)
matris = np.array(veri)

def findStart():
    for i in range(8):
        if matris[i][0] ==0:
           return i,0

def findEnd():
    for i in range(8):
        if matris[i][7] == 0:
            return i,7

x,y = findStart()
correctpath[x,y] = 3
turn = None
right = None
down = None 
up = None
left = None
 
fx,fy = findEnd()

 
def findPath(x,y):
    global turn
    global right
    global down
    global turn
    global left
    if x == fx and y == fy:
        print("YOL BULUNDU")
        print(correctpath)
    else:
       
        right = lookRight(x,y)
        up = lookUp(x,y)
        down = lookDown(x,y)
        left = lookleft(x,y)
       
        toplam = right + down + up
      
        if toplam == 1:
            if right == 1:
                x = x
                y = y +1 
                correctpath[x,y] = 3
                matris[x,y] = 1
                findPath(x,y)
            elif down == 1:
                x = x + 1
                y = y
                correctpath[x,y] = 3
                matris[x,y] = 1
                findPath(x,y)
            elif up == 1:
                x = x - 1
                y = y 
                correctpath[x,y] = 3
                matris[x,y] = 1
                findPath(x,y)
         
        elif toplam == 2:
            turn = [x,y]
            if right == 1 and down == 1:
                matris[x,y+1] = 5
                findPath(x,y)
            elif right == 1 and up == 1:
                matris[x-1,y] = 5
                findPath(x,y)
            elif down == 1 and up == 1:
                matris[x-1,y] = 5
                findPath(x,y)
        elif toplam == 0:
            if left == 1:
                x = x
                y = y -1
                correctpath[x,y] = 3
                matris[x,y] = 1
                findPath(x,y)
            
            x = turn[0]
            y = turn[1]
            
            if matris[x,y+1] == 5:
                matris[x,y+1] = 0
                matris[x+1,y] = 5
                findPath(x,y)
            elif matris[x-1,y] == 5:
                matris[x-1,y] = 0
                matris[x,y+1] = 5
                findPath(x,y)
            if matris[x-1,y] == 5:
                matris[x-1,y] == 0
                matris[x+1,y] = 5
                findPath(x,y)
 

def lookRight(x,y):
    if matris[x,y+1] == 0:
        return 1
    else:
        return 0
    
def lookleft(x,y):
    if matris[x,y-1] == 0:
        return 1
    else:
        return 0

def lookDown(x,y):
    if matris[x+1,y] == 0:
       return 1
    else:
        return 0

def lookUp(x,y):
    if matris[x-1,y] == 0:
        return 1
    else:
        return 0
 
findPath(x,y)
 