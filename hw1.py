#################################################
# Hw1
# Your andrewID:
# Your section: 
#################################################

import cs112_s19_week1_linter

# For collaborative problems, you must list your collaborators!
# Each collaborative problem has a function which you should modify to 
# return a comma-separated string with the andrewIDs of your collaborators.
# Here is an example which you should not modify!
def exampleCollaborators():
    return "mdtaylor, krivers, acarnegie"

#################################################
# Lab1 COLLABORATIVE LAB problems 
# (Their problem descriptions will be released Friday, Jan 18)
#################################################
# The problems in this section are LAB PROBLEMS, which means you MUST
#     work on these with at least one collaborator.  See the collaboration
#     policy in the syllabus for more details.  Always list your collaborators!
#     For lab problems, YOU MUST LIST AT LEAST ONE COLLABORATOR
import math

#### distance is a COLLABORATIVE problem ####
# Modify the output of distanceCollaborators to return the andrewIDs
#     of your collaborators as a string.  Separate each with a comma.
def distanceCollaborators():
    return "peterwu"

def distance(x1, y1, x2, y2):
    return math.sqrt((y2-y1)**2+(x2-x1)**2)

#### isRightTriangle is a COLLABORATIVE problem ####
# Modify the output of isRightTriangleCollaborators to return the andrewIDs
#     of your collaborators as a string.  Separate each with a comma.
def isRightTriangleCollaborators():
    return "bzaslavs"
    
def almostEqual(x, y):
    return abs(x - y) < 10**-9

def isRightTriangle(x1, y1, x2, y2, x3, y3):
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x1, y1, x3, y3)
    return (almostEqual(a**2 + b**2, c**2) or almostEqual(b**2 + c**2,  a**2) or  almostEqual(a**2 + c**2,  b**2))

#### roundPegRectangularHole and rectangularPegRoundHole are COLLABORATIVE ####
# Modify the output of pegProblemCollaborators to return the andrewIDs
#     of your collaborators as a string.  Separate each with a comma.
def pegProblemCollaborators():
    return "bzaslavs"
    
def roundPegRectangularHole(r, w, h):
    return (2*r <= w) and (2*r <= h)
    
    
def rectangularPegRoundHole(r, w, h):
    return (math.sqrt((w/2)**2 + (h/2)**2) <= r)  or almostEqual(((w/2)**2 + (h/2)**2), r**2 )

    
#################################################
# Hw1 COLLABORATIVE problem
#################################################
# The problems in this section are COLLABORATIVE, which means you may
#     work on them with your classmates if you wish.  See the collaboration
#     policy in the syllabus for more details.  Always list your collaborators!
    
#### nearestOdd is a COLLABORATIVE problem ####
# Modify the output of nearestOddCollaborators to return the andrewIDs
#     of your collaborators as a string.  Separate each with a comma.
def nearestOddCollaborators():
    return "nobody"

def nearestOdd(n):
    if not almostEqual(n%1, 0):
        if almostEqual((n//1)%2, 0) == True:  # if n is an oven float number
            return int(n//1+1)
        return int(n//1) 
    else:                  #Checking if this is an integer number
       if almostEqual(n%2, 0) == True:        # if n is an oven number
            return int(n-1)
       return int(n)

#### colorBlender is a COLLABORATIVE problem ####
# Modify the output of colorBlenderCollaborators to return the andrewIDs
#     of your collaborators as a string.  Separate each with a comma.
'''
import decimal
def roundHalfUp(d):
   # Round to nearest with ties going away from zero.
   rounding = decimal.ROUND_HALF_UP
   return int(decimal.Decimal(d).to_integral_value(rounding=rounding))
   
def colorBlenderCollaborators():
    return "nobody"
   
def colorBlender(rgb1, rgb2, midpoints, n):
    a_0 = rgb1//1000000
    b_0 = (rgb1//1000)%1000
    c_0 = rgb1%1000
    a_last = rgb2//1000000
    b_last = rgb2//1000%1000
    c_last = rgb2%1000
 
    n1 = a_last + roundHalfUp((a_0 - a_last)/ (midpoints + 1) * (midpoints + 1 - n))
    n2 = b_last + roundHalfUp((b_0 - b_last)/ (midpoints + 1)* (midpoints + 1 - n))
    n3 = c_last + roundHalfUp((c_0 - c_last)/ (midpoints + 1) * (midpoints + 1 - n))
    if 0 <= n <= midpoints:
        return n1 * 1000000 + n2 * 1000 + n3
    return None
print(colorBlender(220020060, 189252201, 3, 0))
print(colorBlender(220020060, 189252201, 3, 2))
'''

import decimal

def roundHalfUp(d):
   # rounding = decimal.ROUND_HALF_UP
   return decimal.Decimal(d).to_integral_value()

def colorBlender(rgb1, rgb2, midpoints, n):
    a_0 = rgb1 // 1000000
    # print(a_0)
    b_0 = (rgb1 // 1000) % 1000
    # print(b_0)
    c_0 = rgb1 % 1000
    # print(c_0)
    a_last = rgb2 // 1000000
    # print(a_last)
    b_last = rgb2 // 1000 % 1000
    # print(b_last)
    c_last = rgb2 % 1000
    # print(c_last)

    n1 = a_last + roundHalfUp((a_0 - a_last) / (midpoints + 1) * (midpoints + 1 - n))
    n2 = b_last + roundHalfUp((b_0 - b_last) / (midpoints + 1) * (midpoints + 1 - n))
    n3 = c_last + roundHalfUp((c_0 - c_last) / (midpoints + 1) * (midpoints + 1 - n))
    if 0 <= n <= midpoints + 1:
        return n1 * 1000000 + n2 * 1000 + n3
    return None

print(colorBlender(220020060, 189252201, 3, 0))
print(colorBlender(220020060, 189252201, 3, 1))
print(colorBlender(220020060, 189252201, 3, 2))
print(colorBlender(220020060, 189252201, 3, 3))


#################################################
# Hw1 SOLO problems
#################################################
# These problems must be completed WITHOUT COLLABORATION.  See the collaboration
#     policy in the syllabus for more details.  You may always use piazza, 
#     office hours, and other official 15-112 course resources for questions.

def syllabusAnswer():
    return """
1: Family/Personal Emergencies
2: Students are allowed to use a laptop in lecture when learning activities involve electronic devices, which may involve the use of computers to write programs or phones to submit quiz responses.. 
3: You can't use both grace days on one assignment
4: You can't fill out the attendance forms later in the day and still get credit.
5: Submit a regrade request using the online form. The head TAs will review your request and get back to you within two weeks.
"""

def debuggingAnswer():
    return "1. This is a logical error. The code if-if-if tests all the conditions, whereas the code should test conditions only as many as needed: if it tells that one condition is true, then it can stop and doesn't need to execute others. 2. The bug can be fixed by changing if x <= 10 to elif x <= 10 and changing if x > 10 to elif x > 10"

def rocAnswer():
    return 126


#### the following three functions go together ####
# Note: You'll need to use distance(x1,y1,x2,y2) as a helper function!
# Wait to do this problem until after you write distance in Friday's lab

def lineIntersection(m1, b1, m2, b2):
    if m1 != m2:
        return (b2 - b1)/(m1 - m2)
    if m1 == m2:
        return (None)

def triangleArea(s1, s2, s3):
    p = (s1 + s2 + s3)/2
    S = (p*(p-s1)*(p-s2)*(p-s3))**.5
    return S

def threeLinesArea(m1, b1, m2, b2, m3, b3):
    x1 = lineIntersection(m1, b1, m2, b2)
    x2 = lineIntersection(m2, b2, m3, b3)
    x3 = lineIntersection(m1, b1, m3, b3)
    y1 = m1 * x1 + b1
    y2 = m2 * x2 + b2
    y3 = m3 * x3 + b3
    s1 = distance(x1,y1,x2,y2)
    s2 = distance(x1,y1,x3,y3)
    s3 = distance(x2,y2,x3,y3)
    return triangleArea(s1, s2, s3)

#### the following two functions go together ####

def getKthDigit(n, k):
    return (abs(n)//10**k)%10

def setKthDigit(n, k, d):
    if n >= 0:
        return n - (abs(n)//10**k)%10 * 10**k + d * 10**k 
    return - (abs(n) - (abs(n)//10**k)%10 * 10**k + d * 10**k)

#### bonusFindIntRootsOfCubic is a bonus problem, and therefore optional ####
# Note: Bonus problems are solo. Do not collaborate on bonus problems. 
for i in range(4, 9):
    print(i)

import math
math.floor(2.9)
12.57 - 12.57//1
12.57//1+1 - 12.57%1
len(str(12.57))
def bonusFindIntRootsOfCubic(a, b, c, d):
    p = -b/(3*a)
    q = p**3 + (b*c-3*a*d)/(6*a**2)
    r = c/(3*a)
    root1 = (q + (q**2 + (r-p**2)**3)**(1/2))**(1/3) + (q - (q**2 + (r-p**2)**3)**(1/2))**(1/3) + p
    root2 = (-b-root1*a + (b**2 - 4*a*c -2*a*b*root1 - 3*a**2*root1**2)**(1/2))/(2*a)
    root3 = (-b-root1*a - (b**2 - 4*a*c -2*a*b*root1 - 3*a**2*root1**2)**(1/2))/(2*a)
    if isinstance(root1, complex):
        root1 = round(root1.real)
    root1 = int(round(root1, 0))
    if isinstance(root2, complex):
        root2 = round(root2.real)
    root2 = int(round(root2, 0))
    if isinstance(root3, complex):
        root3 = round(root3.real)
    root3 = int(round(root3, 0))
    if root1 <= root2:
        if root2 <= root3:
            return root1, root2, root3
        elif root1 <= root3 <= root2:
            return root1, root3, root2
        return root3, root1, root2
    elif root1 > root2:
        if root3 >= root1:
            return root2, root1, root3
        elif root1 >= root3 >= root2:
            return root2, root3, root1
        return root3, root2, root1
bonusFindIntRootsOfCubic(1, 3, -9, 5)

#################################################
# Hw1 Test Functions
# ignore_rest
#################################################

def testDistance():
    import math
    print("Testing distance()...", end="")
    assert(math.isclose(distance(0, 0, 1, 1), 2**0.5))
    assert(math.isclose(distance(3, 3, -3, -3), 6*2**0.5))
    assert(math.isclose(distance(20, 20, 23, 24), 5))
    print("Passed.")

def testIsRightTriangle():
    print('Testing isRightTriangle()... ', end='')
    assert(isRightTriangle(0, 0, 0, 3, 4, 0) == True)
    assert(isRightTriangle(1, 1.3, 1.4, 1, 1, 1) == True)
    assert(isRightTriangle(9, 9.12, 8.95, 9, 9, 9) == True)
    assert(isRightTriangle(0, 0, 0, math.pi, math.e, 0) == True)
    assert(isRightTriangle(0, 0, 1, 1, 2, 0) == True)
    assert(isRightTriangle(0, 0, 1, 2, 2, 0) == False)
    assert(isRightTriangle(1, 0, 0, 3, 4, 0) == False)
    print('Passed.')

    
def testRoundPegRectangularHole():
    print("Testing roundPegRectangularHole()...", end="")
    assert(roundPegRectangularHole(1,2,3)==True)
    assert(roundPegRectangularHole(4,5,6)==False)
    assert(roundPegRectangularHole(1,20,10)==True)
    assert(roundPegRectangularHole(10,2,30)==False)
    print("Passed.")
    
def testRectangularPegRoundHole():
    print("Testing rectangularPegRoundHole()...", end="")
    assert(rectangularPegRoundHole(1,2,3)==False)
    assert(rectangularPegRoundHole(5,4,6)==True)
    assert(rectangularPegRoundHole(2,4,4)==False)
    assert(rectangularPegRoundHole(5,8,6)==True)
    assert(rectangularPegRoundHole(6,10,8)==False)
    print("Passed.")
    
def testNearestOdd():
    print('Testing nearestOdd()... ', end='')
    assert(nearestOdd(13) == 13)
    assert(nearestOdd(12.001) == 13)
    assert(nearestOdd(12) == 11)
    assert(nearestOdd(11.999) == 11)
    assert(nearestOdd(-13) == -13)
    assert(nearestOdd(-12.001) == -13)
    assert(nearestOdd(-12) == -13)
    assert(nearestOdd(-11.999) == -11)
    print('Passed.')

def testColorBlender():
    print("Testing colorBlender()...", end="")
    # http://meyerweb.com/eric/tools/color-blend/#DC143C:BDFCC9:3:rgbd
    assert(colorBlender(220020060, 189252201, 3, -1) == None)
    assert(colorBlender(220020060, 189252201, 3, 0) == 220020060)
    assert(colorBlender(220020060, 189252201, 3, 1) == 212078095)
    assert(colorBlender(220020060, 189252201, 3, 2) == 205136131)
    assert(colorBlender(220020060, 189252201, 3, 3) == 197194166)
    assert(colorBlender(220020060, 189252201, 3, 4) == 189252201)
    assert(colorBlender(220020060, 189252201, 3, 5) == None)
    # http://meyerweb.com/eric/tools/color-blend/#0100FF:FF0280:2:rgbd
    assert(colorBlender(1000255, 255002128, 2, -1) == None)
    assert(colorBlender(1000255, 255002128, 2, 0) == 1000255)
    assert(colorBlender(1000255, 255002128, 2, 1) == 86001213)
    assert(colorBlender(1000255, 255002128, 2, 2) == 170001170)
    assert(colorBlender(1000255, 255002128, 2, 3) == 255002128)
    print("Passed.")
   

def testSyllabusAnswer():
    print("Your answer to the syllabus question is:")
    print(syllabusAnswer())
    print("The TAs will grade this later.")
    print()

def testDebuggingAnswer():
    print("Your answer to the debugging question is:")
    print(debuggingAnswer())
    print("The TAs will grade this later.")
    print()

def roc(x):
    if type(x) != int:
        return False
    elif x <= 120:
        return False
    elif x % 100 == x - 100:
        a = x // 10
        b = x % 10
        if a != 2 * b:
            return False
        return True
    else:
        return x == 42

def testRocAnswer():
    print("Testing rocAnswer()...", end="")
    answer = rocAnswer()
    assert(roc(answer) == True)
    print("Passed.")

def testLineIntersection():
    import math
    print("Testing lineIntersection()...", end="")
    assert(lineIntersection(2.5, 3, 2.5, 11) == None)
    assert(lineIntersection(25, 3, 25, 11) == None)
    # y=3x-5 and y=x+5 intersect at (5,10)
    assert(math.isclose(lineIntersection(3,-5,1,5), 5))
    # y=10x and y=-4x+35 intersect at (2.5,25)
    assert(math.isclose(lineIntersection(10,0,-4,35), 2.5))
    print("Passed.")

def testTriangleArea():
    import math
    print("Testing triangleArea()...", end="")
    assert(math.isclose(triangleArea(3,4,5), 6))
    assert(math.isclose(triangleArea(2**0.5, 1, 1), 0.5))
    assert(math.isclose(triangleArea(2**0.5, 2**0.5, 2), 1))
    print("Passed.")

def testThreeLinesArea():
    import math
    print("Testing threeLinesArea()...", end="")
    assert(math.isclose(threeLinesArea(1, 2, 3, 4, 5, 6), 0))
    assert(math.isclose(threeLinesArea(0, 7, 1, 0, -1, 2), 36))
    assert(math.isclose(threeLinesArea(0, 3, -.5, -5, 1, 3), 42.66666666666))
    assert(math.isclose(threeLinesArea(1, -5, 0, -2, 2, 2), 25))
    assert(math.isclose(threeLinesArea(0, -9.75, -6, 2.25, 1, -4.75), 21))
    print("Passed.")

def testGetKthDigit():
    print("Testing getKthDigit()...", end="")
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print("Passed.")

def testSetKthDigit():
    print("Testing setKthDigit()...", end="")
    assert(setKthDigit(809, 0, 7) == 807)
    assert(setKthDigit(809, 1, 7) == 879)
    assert(setKthDigit(809, 2, 7) == 709)
    assert(setKthDigit(809, 3, 7) == 7809)
    assert(setKthDigit(0, 4, 7) == 70000)
    assert(setKthDigit(-809, 0, 7) == -807)
    print("Passed.")

def getCubicCoeffs(k, root1, root2, root3):
    # Given roots e,f,g and vertical scale k, we can find
    # the coefficients a,b,c,d as such:
    # k(x-e)(x-f)(x-g) =
    # k(x-e)(x^2 - (f+g)x + fg)
    # kx^3 - k(e+f+g)x^2 + k(ef+fg+eg)x - kefg
    e,f,g = root1, root2, root3
    return k, -k*(e+f+g), k*(e*f+f*g+e*g), -k*e*f*g

def testFindIntRootsOfCubicCase(k, z1, z2, z3):
    import math
    a,b,c,d = getCubicCoeffs(k, z1, z2, z3)
    result1, result2, result3 = bonusFindIntRootsOfCubic(a,b,c,d)
    m1 = min(z1, z2, z3)
    m3 = max(z1, z2, z3)
    m2 = (z1+z2+z3)-(m1+m3)
    actual = (m1, m2, m3)
    assert(math.isclose(m1, result1))
    assert(math.isclose(m2, result2))
    assert(math.isclose(m3, result3))

def testBonusFindIntRootsOfCubic():
    print("Testing bonusFindIntRootsOfCubic()...", end="")
    testFindIntRootsOfCubicCase(5, 1, 3,  2)
    testFindIntRootsOfCubicCase(2, 5, 33, 7)
    testFindIntRootsOfCubicCase(-18, 24, 3, -8)
    testFindIntRootsOfCubicCase(1, 2, 3, 4)
    print("Passed.")

#################################################
# Hw1 Main
#################################################

def testAll():
    testDistance()
    testIsRightTriangle()
    testRoundPegRectangularHole()
    testRectangularPegRoundHole()
    testNearestOdd()
    testColorBlender()
    testSyllabusAnswer()
    testDebuggingAnswer()
    testRocAnswer()
    testLineIntersection()
    testTriangleArea()
    testThreeLinesArea()
    testGetKthDigit()
    testSetKthDigit()
    
    #Uncomment the next line if you want to try the bonus!
    #testBonusFindIntRootsOfCubic() 

def main():
    cs112_s19_week1_linter.lint() # check for banned tokens
    testAll()

if __name__ == '__main__':
    main()