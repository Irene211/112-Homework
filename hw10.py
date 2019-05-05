# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 22:36:07 2019

@author: tianminz
"""
import os

#returns the full path to the largest file in the folder
def findLargestFile(path):
    biggest = ["", 0]
    return findLargestWrapper(path, biggest)

#wrapper function for find largest file
def findLargestWrapper(path, biggest):
    for item in os.listdir(path):
        item = path + "/" + item
        if os.path.isdir(item):
            findLargestWrapper(item, biggest)
        else:
            itemsize = os.path.getsize(item)
            if itemsize > biggest[1]:
                biggest[0] = item
                biggest[1] = itemsize
    return biggest[0]

#returns a 2D list representing a valid knight's tour 
#On an n-by-n chessboard, or None if no solution exists
def createKnightsTour(n):
    board = [ ([0] * n) for row in range(n) ]
    col, row = 0, 0
    startNum = 1
    return findKnightsTour(board, n, col, row, startNum)

#find the knight tour    
def findKnightsTour(board, n, col, row, startNum):
    boardLen = len(board)
    if boardLen == 1: 
        return [[1]]
    #base case:
    board[col][row] = startNum
   
    if startNum == n ** 2:
        return True
    
    else:
        #recursive case:
        possStep = [[2, 1], [1, 2], [-2, 1], [1, -2],
                    [2, -1], [-1, 2], [-2, -1], [-1, -2]]
        for step in possStep:
            newc = col + step[0]
            newr = row + step[1]
            #test if new in the board and new is new
            if (0 <= newc < n) and (0 <= newr < n): 
                if board[newc][newr] == 0: 
                    if findKnightsTour(board, n, newc, newr, startNum + 1):
                        return board
        board[col][row] = 0     
    return None                   

#print pretty 2D list
#The version that submitted
def print2DListResult1111(f):
    def g(*arg):
        lst = f(*arg)
        output = ""
        for i in lst:
            newRow = " "
            for j in i:
                newRow += str(j) + "\t"
            output += "[ " + newRow + "]" + "\n"
        return output
    return g

#The version after changing
def print2DListResult(f):
    def g(*arg):
        output = []
        distance = 7
        if not isinstance(f(*arg), list):
            return None
        for row in range(len(f(*arg))):
            output.append("[" + " " * distance)
            for num in range(len(f(*arg)[row])):
                length = len(str(f(*arg)[row][num]))
                output.append(str(f(*arg)[row][num]) + " " * (distance - length))
            output.append("]" + "\n")
        print(output)
        output = "".join(output)
        return output
    return g

#a, b = "How are you doing today?".split("a")
#print(a) # prints ['How', 'are', 'you', 'doing', 'today?']
#
#You could use a,b = split(' ', 1).
#
#The second argument 1 is the maximum number of splits that would be done.
#
#s = 'abcd efgh hijk'
#a,b = s.split(' ', 1)
#print(a) #abcd
#type(a)
#print(b) 

#test function for printing 2D list
@print2DListResult
def makeExample2DList(n):
    myList=[]
    for row in range(n):
        myList.append([col*row for col in range(n)])
    return myList

lst = makeExample2DList(8)      
print(lst)

from functools import reduce
#return a single string with the values in L separated by the sep.
def myJoin(L, sep):

    return reduce(lambda add, nextAdd: \
                  str(add) + sep + str(nextAdd), map(str,L))


#ignore_rest
def init(data):
    data.level = 3

#displays a majestic fractal sun centered at the (xc, yc) position
#with the given radius r, and at the specified recursion level
def drawFractalSun(data, canvas, xc, yc, r, level):
    if level == 2:
        color = "red"
    elif level == 1:
        color = "orange red"
    elif level == 3:
        color = "orange"
    else: 
        color = "yellow"
    if level == 0:
        canvas.create_oval(xc - r, yc - r,
                           xc + r, yc + r,
                           fill = color, width = 0)
    else:
        canvas.create_line(xc , yc ,xc-2*r, yc, fill = color)
        canvas.create_line(xc , yc ,xc+2*r, yc, fill = color)
        canvas.create_line(xc , yc ,xc, yc-2*r, fill = color)
        canvas.create_line(xc , yc ,xc, yc+2*r, fill = color)
        canvas.create_line(xc , yc ,xc-r*(2)**(1/2), yc-r*(2)**(1/2),
                           fill = color)
        canvas.create_line(xc , yc ,xc+r*(2)**(1/2), yc-r*(2)**(1/2),
                           fill = color)
        canvas.create_line(xc , yc , xc-r*(2)**(1/2), yc+r*(2)**(1/2),
                           fill = color)
        canvas.create_line(xc , yc ,xc+r*(2)**(1/2), yc+r*(2)**(1/2), 
                           fill = color)
        
        drawFractalSun(data, canvas, xc-2*r, yc, r/4, level-1)
        drawFractalSun(data, canvas, xc+2*r, yc, r/4, level-1)
        drawFractalSun(data, canvas, xc, yc-2*r, r/4, level-1)
        drawFractalSun(data, canvas, xc, yc+2*r, r/4, level-1)
        drawFractalSun(data, canvas, 
                       xc-r*(2)**(1/2), yc-r*(2)**(1/2), r/4, level-1)
        drawFractalSun(data, canvas, 
                       xc+r*(2)**(1/2), yc-r*(2)**(1/2), r/4, level-1)
        drawFractalSun(data, canvas, 
                       xc-r*(2)**(1/2), yc+r*(2)**(1/2), r/4, level-1)
        drawFractalSun(data, canvas, 
                       xc+r*(2)**(1/2), yc+r*(2)**(1/2), r/4, level-1)

        canvas.create_oval(xc - r, yc - r,
                           xc + r, yc + r,
                           fill = color, width = 0)
    
def mousePressed(event, data):  
    pass

#Press up to increase level
#Press down to decrease level
def keyPressed(event, data):
    if (event.keysym == "Up" or event.keysym == "Right"):
        data.level += 1
    elif (event.keysym == "Down" or event.keysym == "Left") \
    and data.level>=0:
        data.level -= 1

#Draw background and text.
def redrawAll(canvas, data):
    canvas.create_rectangle(0,0, data.width, data.height, fill = "black")
    xc = data.width/2
    yc = data.height/2
    r = data.width/6
    drawFractalSun(data, canvas, xc, yc, r, data.level)
    canvas.create_text(data.width/2, data.height/17,
                       text = "Level " + str(data.level) + " Fractal Sun",
                       font="Arial 20", fill = "white")
    canvas.create_text(data.width/2, data.height/9,
                       text = "Use arrows to change level",
                       font="Arial 20",fill = "white")

# Updated Animation Starter Code
from tkinter import *
####################################
# use the run function as-is
####################################
def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAllWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(500, 500)
#################################################
# Hw10 Test Functions
#################################################
def testfindLargestFile():
    print("testfindLargestFile...")
    assert(findLargestFile("sampleFiles/folderA") ==
                           "sampleFiles/folderA/folderC/giftwrap.txt")
    assert(findLargestFile("sampleFiles/folderB") ==
                           "sampleFiles/folderB/folderH/driving.txt")
    assert(findLargestFile("sampleFiles/folderB/folderF") == "")
    print("Done...")
    
def testcreateKnightsTour():
    print("testing createKnightsTour...")
    assert(createKnightsTour(1) == [[1]]) 
    assert(createKnightsTour(2) == None) 
    assert(createKnightsTour(3) == None) 
    assert(createKnightsTour(4) == None)
    
    board = createKnightsTour(5) 
    assert(isKnightsTour(board) == True)
    board2 = createKnightsTour(6) 
    assert(isKnightsTour(board2) == True)
    print("Done...")
  
import copy    
def checkNN(board):
    n = len(board)
    lst = []
    for row in board:
        lst += row
    lst.sort()
    nnLst = list(range(1, n ** 2 + 1))
    return nnLst == lst

#Return the row and col
def findN(board, n):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == n:
                return i, j
    return None, None

#Return True if legal and False if not
def legalMove(row, col, nrow, ncol):
    num = 2
    numSecond = -1
    dr = nrow - row
    dc = ncol - col
    valid = [(2, 1), (1, 2),  
             (-2, 1), (1, -2),  
             (2, -1), (-1, 2),  
             (-2, -1), (-1, -2)]  
    return (dr, dc) in valid

#returns True if it represents 
#a legal knight's tour and False otherwise.
def isKnightsTour(board):
    num = 2
    if not checkNN(board):
        return False
    size = len(board)
    for n in range(1, size ** 2):
        row, col = findN(board, n)
        nrow, ncol = findN(board, n + 1)
        if not legalMove(row, col, nrow, ncol):
            return False
    return True
    
def testmyJoin():
    print("testing myJoin...")
    assert(myJoin(['a','b','c'], '-') == 'a-b-c')
    assert(myJoin([1, 2, 3], '@@') == '1@@2@@3')
    print("Done...")
    
def testAll():
    testfindLargestFile()
    testcreateKnightsTour()
    testmyJoin()
    
    
testAll()