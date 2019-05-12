#################################################
# Hw2
# Your andrewID:tianminz
# Your section: H
#################################################

import cs112_s19_week2_linter

### You'll need isPrime for one of the problems, so it is provided here ###
def isPrime(n):
    if (n < 2):
        return False
    maxFactor = round(n**0.5)
    for factor in range(2, maxFactor+1):
        if (n % factor == 0):
            return False
    return True

#################################################
# Lab2 COLLABORATIVE LAB problems 
# (Their problem descriptions will be released Friday, Jan 25)
#################################################
# The problems in this section are LAB PROBLEMS, which means you MUST
#     work on these with at least one collaborator.  See the collaboration
#     policy in the syllabus for more details.  Always list your collaborators!
#     For lab problems, YOU MUST LIST AT LEAST ONE COLLABORATOR

def isSmithNumberCollaborators():
    return "stephan3"

def isPrime(n):
    if (n < 2):
        return False
    maxFactor = round(n**0.5)
    for factor in range(2, maxFactor+1):
        if (n % factor == 0):
            return False
    return True

def SumDigit(n):
    sum = 0
    m = n
    while (n > 0):
        m = n % 10
        n = n //10
        sum = sum + m
    return sum

def IsPrimeFactors(n):
    x = 1
    sum = 0
    count = 0
    while (x <= n):
        if n % x == 0:
            if isPrime(x):
                sum += SumDigit(x)
                n = n/x
                count += 1
            else: 
                x = x + 1
        else:
            x = x + 1
    if count == 1:
        return 0
    else:
        return sum

def isSmithNumber(n):
    if IsPrimeFactors(n) == SumDigit(n):
        return True
    return False

### You can find drawFlagOfCuba in the Graphics section below ###

#################################################
# Hw2 COLLABORATIVE problem
#################################################
# The problems in this section are COLLABORATIVE, which means you may
#     work on them with your classmates if you wish.  See the collaboration
#     policy in the syllabus for more details.  Always list your collaborators!

#### Debugging isMultiPowerfulNumber is a COLLABORATIVE problem ####
def isMultiPowerfulNumberCollaborators(n):
    return "nobody"
# Bug 1: 'if n % factor = 0' should be 'if n % factor == 0'
# Bug 2: 'for factor in range(n)' should be 'for factor in range(1,n)
# Bug 3: We should indent 'factorCount +=1' so that 'factorCount += 1' should be in the same position with the second 'if'.

#### Insert the isMultiPowerfulNumber code here ####
def isMultiPowerfulNumber(n):
    factorCount = 0
    for factor in range(1,n):
        if n % factor == 0 and isPrime(factor):
            if n % (factor**2) != 0:
                return False
            factorCount += 1
    return factorCount > 1
#################################################
# Hw2 SOLO problems
#################################################

def isKaprekarNumber(n):  
    a = n**2
    count = 0
    while a > 0:
        a = a // 10 
        count = count + 1
    a = n**2
    digit = count
    for i in range(digit):
        leftpart = a // 10**(i+1)
        rightpart = a % 10**(i+1)
        if leftpart + rightpart == n and rightpart != 0:
            return True
    return False

def nthKaprekarNumber(n):
    count = -1
    num = 0
    while(count < n):
        num += 1 #optimization
        if isKaprekarNumber(num):
            count += 1
    return num

def nearestKaprekarNumber(n):
    if n <= 0:
        return 1
    for i in range(int(n)):
        leftnew = int(n - i)
        rightnew = int(n + i)
        if isKaprekarNumber(leftnew):
            if isKaprekarNumber(rightnew):
                if n + i >= rightnew and n - i > leftnew:
                    return rightnew
                return leftnew
            elif isKaprekarNumber(rightnew + 1) and ((rightnew + 1) - n) < (n - leftnew):
                return rightnew + 1
            return leftnew
        elif isKaprekarNumber(rightnew):
            if isKaprekarNumber(leftnew - 1):
                if n - (leftnew - 1) < rightnew - n:
                    return leftnew - 1
            return rightnew

### The three following problems are bonus problems, and therefore optional ###
# Note: Bonus problems are solo. Do not collaborate on bonus problems.    
    
def squaresGenerator():
    return

def nswGenerator():
    return

def nswPrimesGenerator():
    return

#################################################
# Hw2 Graphics Functions
# All graphics must go under here to avoid angering the autograder!
# ignore_rest
#################################################

from tkinter import *

### Note that drawFlagOfCuba is COLLABORATIVE and a LAB problem ###
def drawFlagOfCubaCollaborators():
    return "shreyas2"

def drawFlagOfCuba(canvas, width, height):
    # draw a Belgian flag in the area bounded by (x0,y0) in
    # the top-left and (x1,y1) in the bottom-right
    stripe = height/5
    for i in range(1,6):
        if i % 2 == 0:
            canvas.create_rectangle(0, stripe* (i-1), width, stripe * i, 
                                    fill ="white", width = 0)
        else:
            canvas.create_rectangle(0, stripe * (i-1), width, stripe * i,
                                     fill ="darkblue", width = 0)
    canvas.create_polygon(0,0,0,height, 2.2/5 * width, 1/2 * height,
                          fill = 'red3', width = 0)
    r = height/8
    canvas.create_oval(3/10*2.2/5 * width - r, 1/2*height - r,
                       3/10*2.2/5 * width + r, 1/2*height + r, fill = 'white', width = 0)

### Note that drawThreadPattern is COLLABORATIVE ###
import math
def drawThreadPatternCollaborators():
    return "nobody"

def drawThreadPattern(canvas, size, numSpokes, startSpoke, numSkips):
    r = size/2.2
    cx = size/2
    cy = size/2
    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, width = 5) #Draw the large oval first
    #Then, draw the lines
    angle_startSpoke = 2 * math.pi * startSpoke / numSpokes
    x_startSpoke = cx - r*math.sin(angle_startSpoke)
    y_startSpoke = cy + r*math.cos(angle_startSpoke) 
    angle_start = 2 * math.pi * startSpoke / numSpokes
    x_start = cx - r*math.sin(angle_start)
    y_start = cy + r*math.cos(angle_start)
    x = 0
    y = 0
    while x_startSpoke != x or y_startSpoke != y:
        startSpoke = startSpoke + numSkips
        if startSpoke >= 10:
            startSpoke = startSpoke - numSpokes
        else:
            startSpoke = startSpoke
        angle = 2 * math.pi * startSpoke / numSpokes
        x = cx - r * math.sin(angle)
        y = cy + r * math.cos(angle)
        canvas.create_line(x, y, x_start, y_start, width = 0)
        x_start = x
        y_start = y
    #Finally, draw the small ovals and change the color
    for hour in range(numSpokes):
        angle = 2 * math.pi * hour / numSpokes
        x = cx - r*math.sin(angle)
        y = cy + r*math.cos(angle)
        if hour == startSpoke:
            canvas.create_oval(x - size/40, y - size/40, x + size/40, y + size/40, fill = 'green')
        else:
            canvas.create_oval(x - size/40, y - size/40, x + size/40, y + size/40, fill = 'red')
        
### Note that drawSteelersLogo is SOLO ###
            
def drawSteelersLogo(canvas, x, y, r):
    canvas.create_oval(x - r, y - r, x + r, y + r, fill = "gray", width = 0)
    canvas.create_oval(x - r*4/5, y - r*4/5, x + r*4/5, y + r*4/5, fill = "white", width = 0 )
    s = r * 1/14
    h = r * 35/54
    canvas.create_polygon(x, y - h - s, x - h*1/2, y - s - h*1/2,
                          x, y - s, x + h*1/2, y - s - h*1/2, fill = "gold", width = 0)
    canvas.create_polygon(x + s + h*1/2, y - h*1/2, x + s, y,
                          x + s + h*1/2, y + h*1/2,
                          x + s + h, y, fill = "red", width = 0)
    canvas.create_polygon(x, y + s,
                          x - h*1/2, y + s + h*1/2,
                          x, y + s + h,
                          x + h*1/2, y + s + h*1/2, fill = "blue", width = 0)
    textSize = int(r/6)
    canvas.create_text(x - r*2/5, y, text = "Steelers", font ="Times " + str(textSize))

### Note that drawButtonPattern is SOLO ###
def drawButtonPattern(canvas, size, n):
    canvas.create_rectangle(0,0,size,size, fill = "purple", width = 0) #Create background
    for i in range(n): #Row 
        for j in range(n): #Row 1, Column 1
            if (i + j) % 4 == 0 :
                canvas.create_oval(size/n*j, size/n*i, size/n*(j+1), size/n*(i+1), fill = "red", width = 1)
                r_smaller = r_larger = r_largest = size/(2*n)
                while r_smaller >= 1:
                    r_smaller = 2/3*r_larger
                    canvas.create_oval((r_largest - r_smaller) + (j*size/n), (r_largest - r_smaller) + (i*size/n), 
                                        (r_largest + r_smaller) + (j*size/n), (r_largest + r_smaller) + (i*size/n) , fill = "red", width = 1)
                    r_larger = r_smaller
            elif i % 3 == 0:
                canvas.create_oval(size/n*j, size/n*i, size/n*(j+1), size/n*(i+1), fill = "green", width = 1)
                r_smaller = r_larger = r_largest = size/(2*n)
                while r_smaller >= 1:
                    r_smaller = 2/3*r_larger
                    canvas.create_oval((r_largest - r_smaller) + (j*size/n), (r_largest - r_smaller) + (i*size/n), 
                                        (r_largest + r_smaller) + (j*size/n), (r_largest + r_smaller) + (i*size/n) , fill = "green", width = 1)
                    r_larger = r_smaller
            elif j % 2 != 0:
                canvas.create_oval(size/n*j, size/n*i, size/n*(j+1), size/n*(i+1), fill = "yellow", width = 1)
                r_smaller = r_larger = r_largest = size/(2*n)
                while r_smaller >= 1:
                    r_smaller = 2/3*r_larger
                    canvas.create_oval((r_largest - r_smaller) + (j*size/n), (r_largest - r_smaller) + (i*size/n), 
                                        (r_largest + r_smaller) + (j*size/n), (r_largest + r_smaller) + (i*size/n) , fill = "yellow", width = 1)
                    r_larger = r_smaller
                
            else:
                canvas.create_oval(size/n*j, size/n*i, size/n*(j+1), size/n*(i+1), fill = "blue", width = 1)
                r_smaller = r_larger = r_largest = size/(2*n)
                while r_smaller >= 1:
                    r_smaller = 2/3*r_larger
                    canvas.create_oval((r_largest - r_smaller) + (j*size/n), (r_largest - r_smaller) + (i*size/n), 
                                        (r_largest + r_smaller) + (j*size/n), (r_largest + r_smaller) + (i*size/n) , fill = "blue", width = 1)
                    r_larger = r_smaller

def testDrawButtonPattern():
    print("Testing drawButtonPattern()...", end="")
    runDrawButtonPattern(400, 400, 10)    
    runDrawButtonPattern(300, 300, 5)
    runDrawButtonPattern(250, 250, 25)
    print("Done.")
    
#### Note that drawNiceRobot is BONUS, and therefore optional ####
def drawNiceRobot(canvas, width, height):
    pass

#################################################
# Hw2 Test Functions
# ignore_rest
#################################################

def testIsSmithNumber():
    print("Testing isSmithNumber()...", end="")
    assert(isSmithNumber(22) == True)
    assert(isSmithNumber(21) == False)
    assert(isSmithNumber(4) == True)
    assert(isSmithNumber(378) == True)
    assert(isSmithNumber(1) == False)
    assert(isSmithNumber(27) == True)
    assert(isSmithNumber(9) == False)
    assert(isSmithNumber(7) == False)
    print("Passed.")

def runDrawFlagOfCuba(width, height):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # width must equal height
    assert(width == 2*height)
    drawFlagOfCuba(canvas, width, height)
    root.mainloop()

def testDrawFlagOfCuba():
    print("Testing drawFlagOfCuba()...", end="")
    runDrawFlagOfCuba(580, 290)
    runDrawFlagOfCuba(100, 50)
    runDrawFlagOfCuba(300, 150)
    print("Done.")

def testIsMultiPowerfulNumber():
    print("Testing isMultiPowerfulNumber()...", end="")
    assert(isMultiPowerfulNumber(36) == True)
    assert(isMultiPowerfulNumber(72) == True)
    assert(isMultiPowerfulNumber(100) == True)
    assert(isMultiPowerfulNumber(108) == True)
    print("Done!")

def runDrawThreadPattern(width, height, numSpokes, startSpoke, numSkips):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # width must equal height
    assert(width == height)
    drawThreadPattern(canvas, width, numSpokes, startSpoke, numSkips)
    root.mainloop()

def testDrawThreadPattern():
    print("Testing drawThreadPattern...", end="")
    runDrawThreadPattern(400, 400, 12, 0, 5)
    runDrawThreadPattern(200, 200, 10, 3, 4)
    runDrawThreadPattern(500, 500, 19, 8, 15)
    print("Done.")

def runDrawSteelersLogo(width, height, x, y, r):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawSteelersLogo(canvas, x, y, r)
    root.mainloop()

def testDrawSteelersLogo():
    print("Testing drawSteelersLogo...", end="")
    runDrawSteelersLogo(300, 300, 150, 150, 100)
    runDrawSteelersLogo(500, 600, 300, 200, 200)
    runDrawSteelersLogo(150, 100, 50, 60, 40)
    print("Done.")

def testIsKaprekarNumber():
    print("Testing isKaprekarNumber()...", end="")
    assert(isKaprekarNumber(0) == False)
    assert(isKaprekarNumber(1) == True)
    assert(isKaprekarNumber(4) == False)
    assert(isKaprekarNumber(9) == True)
    assert(isKaprekarNumber(36) == False)
    assert(isKaprekarNumber(45) == True)
    assert(isKaprekarNumber(450) == False)
    print("Passed.")

def testNthKaprekarNumber():
    print("Testing nthKaprekarNumber()...", end="")
    assert(nthKaprekarNumber(0) == 1)
    assert(nthKaprekarNumber(1) == 9)
    assert(nthKaprekarNumber(2) == 45)
    assert(nthKaprekarNumber(3) == 55)
    assert(nthKaprekarNumber(4) == 99)
    assert(nthKaprekarNumber(5) == 297)
    assert(nthKaprekarNumber(6) == 703)
    assert(nthKaprekarNumber(7) == 999)
    print('Passed.')

def testNearestKaprekarNumber():
    print("Testing nearestKaprekarNumber()...", end="")
    assert(nearestKaprekarNumber(1) == 1)
    assert(nearestKaprekarNumber(0) == 1)
    assert(nearestKaprekarNumber(-1) == 1)
    assert(nearestKaprekarNumber(-2) == 1)
    assert(nearestKaprekarNumber(-12345) == 1)
    assert(nearestKaprekarNumber(1.234) == 1)
    assert(nearestKaprekarNumber(4.99999999) == 1)
    assert(nearestKaprekarNumber(5) == 1)
    assert(nearestKaprekarNumber(5.00000001) == 9)
    assert(nearestKaprekarNumber(27) == 9)
    assert(nearestKaprekarNumber(28) == 45)
    assert(nearestKaprekarNumber(45) == 45)
    assert(nearestKaprekarNumber(50) == 45)
    assert(nearestKaprekarNumber(51) == 55)
    assert(nearestKaprekarNumber(1611) == 999)
    assert(nearestKaprekarNumber(1612) == 2223)
    assert(nearestKaprekarNumber(2475.4) == 2223)
    assert(nearestKaprekarNumber(2475.5) == 2223)
    assert(nearestKaprekarNumber(2475.51) == 2728)
    assert(nearestKaprekarNumber(2475.6) == 2728)
    assert(nearestKaprekarNumber(995123) == 994708)
    assert(nearestKaprekarNumber(9376543) == 9372385)
    assert(nearestKaprekarNumber(13641234) == 13641364)
    print("Passed.")

def runDrawButtonPattern(width, height, n):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # width must equal height
    assert(width == height)
    drawButtonPattern(canvas, width, n)
    root.mainloop()

def testDrawButtonPattern():
    print("Testing drawButtonPattern()...", end="")
    runDrawButtonPattern(400, 400, 10)    
    runDrawButtonPattern(300, 300, 5)
    runDrawButtonPattern(250, 250, 25)
    print("Done.")

def runDrawNiceRobot(width, height):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawNiceRobot(canvas, width, height)
    root.mainloop()

def testDrawNiceRobot():
    print("Testing drawNiceRobot()...", end="")
    runDrawNiceRobot(500, 500)
    runDrawNiceRobot(250, 250)
    print("Done.")

def testSquaresGenerator():
    print("Testing squaresGenerator()...", end="")
    g = squaresGenerator()
    assert(next(g) == 1)
    assert(next(g) == 4)
    assert(next(g) == 9)
    assert(next(g) == 16)

    # ok, now with a for loop.
    squares = ""
    for square in squaresGenerator():
        if (squares != ""): squares += ", "
        squares += str(square)
        if (square >= 100): break
    assert(squares == "1, 4, 9, 16, 25, 36, 49, 64, 81, 100")
    print("Passed.")

def testNswGenerator():
    print("Testing nswGenerator()...", end="")
    nswNumbers = ""
    for nswNumber in nswGenerator():
        if (nswNumbers != ""): nswNumbers += ", "
        nswNumbers += str(nswNumber)
        if (nswNumber >= 152139002499): break
    # from: http://oeis.org/A001333
    assert(nswNumbers == "1, 1, 3, 7, 17, 41, 99, 239, 577, 1393, 3363, 8119, "
                         "19601, 47321, 114243, 275807, 665857, 1607521, 3880899, "
                         "9369319, 22619537, 54608393, 131836323, 318281039, "
                         "768398401, 1855077841, 4478554083, 10812186007, "
                         "26102926097, 63018038201, 152139002499"
          )
    print("Passed.")
    
def testNswPrimesGenerator():
    print("Testing nswPrimesGenerator()...", end="")
    nswPrimes = ""
    for nswPrime in nswPrimesGenerator():
        if (nswPrimes != ""): nswPrimes += ", "
        nswPrimes += str(nswPrime)
        if (nswPrime >= 63018038201): break
    # from: http://oeis.org/A088165
    assert(nswPrimes == "7, 41, 239, 9369319, 63018038201")
    print("Passed.")

#################################################
# Hw2 Main
#################################################

def testAll():
    ### Lab problems ###
    testIsSmithNumber()
    testDrawFlagOfCuba()
    ### Collaborative problems ###
    testIsMultiPowerfulNumber()
    testDrawThreadPattern()
    ### Solo problems ###
    testDrawSteelersLogo()
    testIsKaprekarNumber()
    testNthKaprekarNumber()
    testNearestKaprekarNumber()
    testDrawButtonPattern()
    
    # Uncomment the next lines if you want to try the bonus!
    #testDrawNiceRobot()
    #testSquaresGenerator()
    #testNswGenerator()
    #testNswPrimesGenerator()

def main():
    cs112_s19_week2_linter.lint() # check for banned tokens
    testAll()

if __name__ == '__main__':
    main()