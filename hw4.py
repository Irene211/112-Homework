#################################################
# Hw4
# Your andrewID: tianminz
# Your section: H
#################################################

import math
import copy
    
#################################################
# Hw4 COLLABORATIVE problems
#################################################
# The problem in this section is COLLABORATIVE, which means you may
#     work on it with your classmates if you wish.  See the collaboration
#     policy in the syllabus for more details.  Always list your collaborators!

def lookAndSayCollaborators():
    return "nobody"

#Takes a list of numbers and returns a list of numbers using the look-and-say method
def lookAndSay(lst):
    #corner case
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [(1, lst[0])]
    
    #initial the first element
    lookup = [1,lst[0]]
    output = []
    
    #loop start from the second element
    for idx in range(1, len(lst)): 
        if lst[idx] == lookup[1]: #Same letter
            lookup[0] += 1
        else: #First letter 
            output.append((lookup[0],lookup[1]))
            lookup = [1, lst[idx]]
    output.append((lookup[0], lookup[1]))
    return output


def inverseLookAndSayCollaborators():
    return "nobody"

#Turning tuples of count and value into a single list
def inverseLookAndSay(lst):
    output = []
    for tup in lst:
        output += tup[0] * [tup[1]]
    return output

#################################################
# Hw4 SOLO problems
#################################################

# removes any repeating elements from a given list and implements the function nondestructively
def nondestructiveRemoveRepeats(lst):
    output = []
    
    for ele in lst:
        if ele not in output:
            output.append(ele)
    return output

# removes any repeating elements from a given list and implements the function destructively
def destructiveRemoveRepeats(lst):
    refer = [] 
    idx = 0
    while idx < len(lst):
        if lst[idx] in refer:
            lst.pop(idx)
        else:
            refer.append(lst[idx])
            idx = idx + 1

#Find the bestscrabblescore
def bestScrabbleScore(dictionary, letterScores, hand):
    letterAllow = [0] * 26
    for letter in hand:
        letterAllow[ord(letter) - ord('a')] += 1     
    wordsAllow = []
    for word in dictionary:    
#00000000000000000000000000
#abcdefghijklmnopqrstuvwxyz  
 
        #convert word into alphabet list
        letterInWord = [0] * 26
        for letter in word:
            letterInWord[ord(letter) - ord('a')] += 1     
            
        #check if word verified
        verified = True
        for idx in range(26):
            if letterInWord[idx] > letterAllow[idx]:
                verified = False
                break       
            
        #if yes, calculate the word score
        if verified:
            score = 0
            for idx in range(26):
                score += letterInWord[idx] * letterScores[idx]
            wordsAllow.append([word, score])
            
    #no word allow in the dictionary
    if len(wordsAllow) == 0:
        return None    
    
    #find the max score
    output_words = []
    max_val = 0
    for word in wordsAllow:
        if word[1] > max_val:
            output_words = [word[0]]
            max_val = word[1]
        elif word[1] == max_val:
            output_words += [word[0]]  
            
    #to meet the output format     
    if len(output_words) == 1:
        return (output_words[0], max_val)
    else:
        return (output_words, max_val)

#################################################
# Hw4 Graphics & Animation Functions
# All graphics must go under here to avoid angering the autograder!
# ignore_rest
#################################################
from tkinter import *

## Tortoise Animation functions ##
## Note - the Tortoise animation is collaborative! ##

## Tortoise Animation bonus features: none ##

def tortoiseAnimationCollaborators():
    return "nobody"

#Initialize data
def init(data):
    
    #When displaying the text on window, leave some spaces to the left 
    disToLeft = 10 
    #The number of buttons 
    colNum = 10
    
    data.lineX = data.width/2
    data.lineY = data.height/2
    data.charText = ""
    data.keysymText = data.code.split("\n")
    data.counter = 0
    data.lineColor = "yellow"
    data.angle = 0
    
    #Create an empty list to store the input text
    data.text = [] 
    data.textY = 0
    data.textX = disToLeft
    #Create an empty list to store lines
    data.lineSet = [] 
    
    data.rows = 1 # Buttons are in one row
    data.cols = colNum #Total number of buttons in column direction.
    data.margin = data.width/colNum

#Change text while press different button    
def mousePressed(event, data):
    x = event.x
    y = event.y
    if y > 450:
        data.counter = 0
        data.code = ""
        #Press certain button and get certain command
        if 0 < x < 50:
            data.code = "color red" + "\n"
        elif 50 < x < 100:
            data.code = "color orange" + "\n"
        elif 100 < x < 150:
            data.code = "color yellow" + "\n"
        elif 150 < x < 200:
            data.code = "color green" + "\n"
        elif 200 < x < 250:
            data.code = "color blue" + "\n"
        elif 250 < x < 300:
            data.code = "color purple" + "\n"
        elif 300 < x < 350:
            data.code = "color none" + "\n"
        elif 350 < x < 400:
            data.code = "move 5" + "\n"
        elif 400 < x < 450:
            data.code = "move 25" + "\n"
        else:
            data.code = "move 50" + "\n"
    data.keysymText = data.code.split("\n")
                    
#Count the Enter button pressed and change text if press other button.
def keyPressed(event, data):
    if event.keysym == "Return" and data.counter < len(data.keysymText) - 1:
        data.counter +=  1
    if event.keysym == "Left":
        data.counter = 0
        data.code = "left 30" + "\n"
    if event.keysym == "Right":
        data.counter = 0    
        data.code = "right 30" + "\n"
    data.keysymText = data.code.split("\n")   

#Draw 10 rectangles and 3 number
def redrawAll(canvas, data):
    currentLine = data.counter
    runProgram(canvas, data, currentLine)

    for row in range(data.cols): # 1,2,3,4,5,6,7,8,9,10
        (x0, y0, x1, y1) = getCellBounds(row, data)
        if row == 0: fill = "red"
        elif row == 1: fill = "orange" 
        elif row == 2: fill = "yellow" 
        elif row == 3: fill = "green"
        elif row == 4: fill = "blue"
        elif row == 5: fill = "purple"
        else: fill = "white"
        canvas.create_rectangle(x0, y0, x1, y1, fill=fill,width = 5)
    
    canvas.create_text(375, 475, text = "5")
    canvas.create_text(425, 475, text = "25")
    canvas.create_text(475, 475, text = "50")

#Loop the x, y location of the rectangles
def getCellBounds(row, data):
    
    # returns (x0, y0, x1, y1) of given button in window
    x0 = row * data.margin #0,1,2,3,4,5
    x1 = (row + 1) * data.margin
    y0 = data.height - data.margin
    y1 = data.height
    return (x0, y0, x1, y1)

#Draws graphics according to the provided tortoise program up to the given currentLine
def runProgram(canvas, data, currentLine):
    x1 = data.lineX
    y1 = data.lineY
    #Set the distance between lines displaying on the window.
    disBetweenLine = 14
    if data.keysymText != "":  
        line =  data.keysymText[data.counter]
        
        #Add together those lines, x, y position to display on the left-hand side of the window.
        data.text.append([line, data.textX, data.textY])
        data.textY += disBetweenLine
        
        if "#" in line:
            line = line[0:line.index("#")]                                           
        if len(line) == 0 : pass
        elif line[0] == "#": pass
        
        #Use function findColor(line) and findAngle(data.angle, line) to change color and angle
        elif "color" in line:
            data.lineColor = findColor(line)   
        elif "right" in line or "left" in line:
            data.angle = findAngle(data.angle, line) 
        elif "move" in line:       
            setLength = findLength(line)
            x2 = x1 + setLength*math.cos(math.radians(data.angle))
            y2 = y1 - setLength*math.sin(math.radians(data.angle))
            data.lineX = x2
            data.lineY = y2   
            data.lineSet.append([x1, y1, x2, y2, data.lineColor]) 
            
    #Display the program up to the currentLine in gray text on the left-hand side of the window
    for text in data.text:
        canvas.create_text(text[1], text[2], text=text[0], fill = "gray", anchor = "nw")  
    
    #Loop line in data.lineSet to draw lines.
    for line in data.lineSet:   
        canvas.create_line(line[0], line[1], line[2], line[3], fill = line[4], width = 4) 
        
    # Draw Arrow
    drawArrow(canvas, data.lineX, data.lineY, data.angle)

#Loop the name of the color
def findColor(line):
    setColor = ""
    line = line.split(" ")
    setColor = str(line[1])
    if setColor == "none": 
        setColor = "white"
    return setColor

#Loop the length of the move
def findLength(line):
    setLength = ""
    line = line.split(" ")
    setLength = str(line[1])
    return int(setLength)    

#Loop the angle of the 
def findAngle(origin, line):
    setAngle = 0
    if "left" in line:
        line = line.split(" ")
        setAngle = origin + int(line[1])
    elif "right" in line:
        line = line.split(" ")
        setAngle = origin - int(line[1])
    
    if setAngle > 360:
        return 360 - setAngle
    elif setAngle < 0:
        return 360 + setAngle
    else:
        return setAngle

""" This function is provided as part of the starter code.
You don't need to change it, but you should call it!"""
def drawArrow(canvas, x, y, angle):
    offset = 135
    r = 10
    x1 = x + r*math.cos(math.radians(angle))
    y1 = y - r*math.sin(math.radians(angle))
    x2 = x + r*math.cos(math.radians(angle + offset))
    y2 = y - r*math.sin(math.radians(angle + offset))
    x3 = x + r*math.cos(math.radians(angle - offset))
    y3 = y - r*math.sin(math.radians(angle - offset))
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="black")


### Timeline Game is a bonus problem, and therefore optional ###
# Note: Bonus problems are solo. Do not collaborate on bonus problems.

## Timeline Game functions ##

""" This function is provided as part of the starter code.
You don't need to change it, but you should call it!"""
def starterCards():
    import random
    cards = [ ("Domestication of the Cat", -4500),
              ("Creation of the Pythagorean Theorem", -548),
              ("Invention of Chess", 570),
              ("First Calculating Machine", 1642), 
              ("Invention of the Telegraph", 1837),
              ("Invention of Morse Code", 1838),
              ("Invention of the Plastic Bottle", 1963), 
              ("Invention of the Computer Mouse", 1963), 
              ("Invention of the Laptop Computer", 1981),
              ("First Public Internet Access", 1990)
            ]
    random.shuffle(cards)
    return cards

def initTimeline(data):
    pass

def mousePressedTimeline(event, data):
    pass

def keyPressedTimeline(event, data):
    pass

def redrawAllTimeline(canvas, data):
    pass

#################################################
# Hw4 Test Functions
#################################################

def _verifyLookAndSayIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    lookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    assert(_verifyLookAndSayIsNondestructive() == True)
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) ==  [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    print("Passed.")

def _verifyInverseLookAndSayIsNondestructive():
    a = [(1,2), (2,3)]
    b = copy.copy(a)
    inverseLookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testInverseLookAndSay():
    print("Testing inverseLookAndSay()...", end="")
    assert(_verifyInverseLookAndSayIsNondestructive() == True)
    assert(inverseLookAndSay([]) == [])
    assert(inverseLookAndSay([(3,1)]) == [1,1,1])
    assert(inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7])
    assert(inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10])
    print("Passed.")

def runTortoiseAnimation(code, width=500, height=500):
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

    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.code = code
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAllWrapper(canvas, data)
    root.mainloop()  # blocks until window is closed

def testTortoiseAnimation():
    print("Running Tortoise Animation...", end="")
    runTortoiseAnimation("""
# This is a simple tortoise program
color blue
move 50

left 90

color red
move 100

color none # turns off drawing
move 50

right 45

color green # drawing is on again
move 50

right 45

color orange
move 50

right 90

color purple
move 100
""")
    runTortoiseAnimation('''
# Y
color red
right 45
move 50
right 45
move 50
right 180
move 50
right 45
move 50
color none # space
right 45
move 25

# E
color green
right 90
move 85
left 90
move 50
right 180
move 50
right 90
move 42
right 90
move 50
right 180
move 50
right 90
move 43
right 90
move 50  # space
color none
move 25

# S
color blue
move 50
left 180
move 50
left 90
move 43
left 90
move 50
right 90
move 42
right 90
move 50
''')
    print("Done.")


def _verifyNondestructiveRemoveRepeatsIsNondestructive():
    a = [3, 5, 3, 3, 6]
    b = copy.copy(a)
    # ignore result, just checking for destructiveness here
    nondestructiveRemoveRepeats(a)
    return (a == b)

def testNondestructiveRemoveRepeats():
    print("Testing nondestructiveRemoveRepeats()", end="")
    assert(_verifyNondestructiveRemoveRepeatsIsNondestructive())
    assert(nondestructiveRemoveRepeats([1,3,5,3,3,2,1,7,5]) == [1,3,5,2,7])
    assert(nondestructiveRemoveRepeats([1,2,3,-2]) == [1,2,3,-2])
    print("Passed.")

def testDestructiveRemoveRepeats():
    print("Testing destructiveRemoveRepeats()", end="")
    a = [1,3,5,3,3,2,1,7,5]
    assert(destructiveRemoveRepeats(a) == None)
    assert(a == [1,3,5,2,7])
    b = [1,2,3,-2]
    assert(destructiveRemoveRepeats(b) == None)
    assert(b == [1,2,3,-2])
    print("Passed.")

def testBestScrabbleScore():
    print("Testing bestScrabbleScore()...", end="")
    def d1(): return ["a", "b", "c"]
    def ls1(): return [1] * 26
    def d2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"] 
    def ls2(): return [1 + (i % 5) for i in range(26)]
    assert(bestScrabbleScore(d1(), ls1(), ["b"]) == ("b", 1))
    assert(bestScrabbleScore(d1(), ls1(), ["a", "c", "e"]) == (["a", "c"], 1))
    assert(bestScrabbleScore(d1(), ls1(), ["b"]) == ("b", 1))
    assert(bestScrabbleScore(d1(), ls1(), ["z"]) == None)
    # x = 4, y = 5, z = 1
    # ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    #    10     10     7     10    9      -
    assert(bestScrabbleScore(d2(), ls2(), ["x","y","z"]) == (["xyz","zxy"], 10))
    assert(bestScrabbleScore(d2(), ls2(), 
                            ["x", "y", "z", "y"]) == (["xyz", "zxy", "yy"], 10))
    assert(bestScrabbleScore(d2(), ls2(), ["x", "y", "q"]) == ("yx", 9))
    assert(bestScrabbleScore(d2(), ls2(), ["y", "z", "z"]) == ("zzy", 7))
    assert(bestScrabbleScore(d2(), ls2(), ["w", "x", "z"]) == None)
    print("Passed.")
#0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 
#1 2 3 4 5 1 2 3 4 5 1  2  3  4  5  1  2  3  4  5  1  2  3  4  5  1  
#
#a b c d e f g h i j k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
def runTimelineGame(width=1200, height=400):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAllTimeline(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressedTimeline(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressedTimeline(event, data)
        redrawAllWrapper(canvas, data)

    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    initTimeline(data)
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAllWrapper(canvas, data)
    root.mainloop()  # blocks until window is closed

#################################################
# Hw4 Main
#################################################

def testAll():
    ## Collaborative Functions ##
    testLookAndSay()
    testInverseLookAndSay()
    testTortoiseAnimation()
    ## Solo Functions ##
    testNondestructiveRemoveRepeats()
    testDestructiveRemoveRepeats()
    testBestScrabbleScore()
    
    # Uncomment the next line if you want to try the bonus!
    #runTimelineGame()

def main():
    testAll()

if __name__ == '__main__':
    main()