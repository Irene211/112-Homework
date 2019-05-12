#################################################
# Hw3
# Your andrewID:tianminz
# Your section: H
#################################################

import cs112_s19_week3_linter


#################################################
# Lab3 COLLABORATIVE LAB problem 
# (The problem description will be released Friday, Feb 1)
#################################################
# The problems in this section are LAB PROBLEMS, which means you MUST
#     work on them with at least one collaborator.  See the collaboration
#     policy in the syllabus for more details.  Always list your collaborators!
#     For lab problems, YOU MUST LIST AT LEAST ONE COLLABORATOR

# Note: You will need extra files for gradebookSummary.  These will be 
#     released FRIDAY during lab! Comment out the tests for now!
def gradebookSummaryCollaborators():
    return "nobody"

def gradebookSummary(gradebookFilename):
    file = readFile(gradebookFilename) 
    if file.count("\n") <= 1:
        newFile = file.replace("\n",",")
        newFile = newFile.split(",")
        newFile = finalResult34(newFile)
    else:  
        newFile = findName(file)[:-1]
        newFile = newFile.split(",")
        newFile = finalResult(newFile)
    return newFile   
 
def readFile(path):
    with open(path, "rt") as f:
        return f.read()     
    
def findName(file):
    Final = ""
    num = 1
    a = 3  #The number of "\n" except first one.
    while a > 0 : 
        dis = file.find('\n',num)   #1,50,        
        if file[dis + 1].isalpha(): #50
            nameIndex1 = file.find("\n", num) + 1 #名字的第一个字母的index
            for j in range(nameIndex1,len(file)):
               c = file[j] 
               if c == ",":
                   name1 = file[nameIndex1:j] # j = ","
                   scoreNum = file.find('\n', dis + 1)
                   score1 = file[j+1:scoreNum]
                   Final += name1 + "," + score1 + ","
                   break
               else: continue
            num = dis + 1
            a -= 1
        else:
            num = dis + 1
    return Final

def finalResult(n): 
    count = 0
    final = ""
    total = 0
    for i in range(len(n)):
        c = n[i]
        if c.isalpha():
            if count > 0: 
                total = total/count
                final += str("%0.2f" % total) + "\n" + c + "\t"
            else: final += c + "\t"
            count = 0
            total = 0
        elif not c.isalpha() and i < len(n) - 1:
            count += 1
            total += int(c)
        else:
            total += int(c)
            final += str("%0.2f" % total)
    return final
    
def finalResult34(n): 
    count = 0
    final = ""
    total = 0
    isAlpha = True
    for i in range(len(n)):
        c = n[i]
        if c.isalpha() and isAlpha:
            final += c + "\t"
            count = 0
            total = 0
        elif c.isalpha() and isAlpha == False:
            total = total/count
            final += str("%0.2f" % total) + "\n"
            final += c + "\t"
            isAlpha = True
            count = 0
            total = 0
        elif not c.isalpha() and isAlpha and i!=(len(n) - 1):
            count += 1
            total += int(c)
            isAlpha = False
        elif not c.isalpha() and isAlpha and i==(len(n) - 1):
            count += 1
            total += int(c)
            total = total/count
            final += str("%0.2f" % total)
        elif not c.isalpha() and isAlpha == False and i !=(len(n) - 1):
            count += 1
            total += int(c)
        else:
            count += 1
            total += int(c)
            total = total/count
            final += str("%0.2f" % total)
    return final 

    
    
def applyCaesarCipherCollaborators():
    return "nobody" 
    
def applyCaesarCipher(message, shiftNum):
    plainAlphaUp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plainAlphaLow = "abcdefghijklmnopqrstuvwxyz"
    cipherAlphaUp = newPatternUp(shiftNum)
    cipherAlphaLow = newPatternLow(shiftNum)
    finalMessage = ""
    for i in range(len(message)):
        c1 = message[i]
        if c1.isalpha():
            if c1.isupper():
                for j in range(len(plainAlphaUp)):
                    if c1 == plainAlphaUp[j]:
                        finalMessage += cipherAlphaUp[j]
            else:
                for s in range(len(plainAlphaLow)):
                    if c1 == plainAlphaLow[s]:
                        finalMessage += cipherAlphaLow[s]
        elif c1.isspace():
            finalMessage += " "
        else:
            finalMessage += c1
    return finalMessage

def newPatternUp(shiftNum):
    plainAlphaUp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipherAlphaUp = ""
    for i in range(len(plainAlphaUp)):
        cipherAlphaUp += plainAlphaUp[(i + shiftNum) % 26]
    return cipherAlphaUp

def newPatternLow(shiftNum):
    plainAlphaLow = "abcdefghijklmnopqrstuvwxyz"
    cipherAlphaLow = ""
    for i in range(len(plainAlphaLow)):
        cipherAlphaLow += plainAlphaLow[(i + shiftNum) % 26]
    return cipherAlphaLow    
#################################################
# Hw2 COLLABORATIVE problem
#################################################
# The problem in this section is COLLABORATIVE, which means you may
#     work on it with your classmates if you wish.  See the collaboration
#     policy in the syllabus for more details.  Always list your collaborators!

def rightJustifyTextCollaborators():
    return "nobody"

def rightJustifyText(text, width):
    text = ReplaceWhiteSpace(text)
    text = IndividualLine(text, width)
    text = RemoveLastSpaceGetNewSpace(text, width) 
    return text

def ReplaceWhiteSpace(text):
    HaveSpace = False
    result = ""
    for i in range(len(text)):
        c = text[i]
        if not HaveSpace and not c.isspace():
            result += c
        elif not HaveSpace and c.isspace():
            HaveSpace = True
        elif HaveSpace and not c.isspace():
            result += " "
            result += c
            HaveSpace = False
        else:
            HaveSpace = True
    return result

def IndividualLine(text,width):
    Num = ""
    Final = ""
    Boss = ""
    a = 0
    for i in range(len(text)):
        c = text[i]
        if not c.isspace():#If this is a number, then add the numbers together
            Num += c
            if i == len(text)-1:
                TestDigit = len(Final) + len(Num) 
                Digit = len(Final)
                if TestDigit + 1 <= width - a:
                    Final += Num + " "
                elif TestDigit == width - a:
                    Final += Num + "\n"
                    Final = ""
                else: #If there is no space for a new word & there are spaces for space, add certain number of space.   
                    Final += "\n" + Num + " "
                    a = len(Num + " ") 
                    Boss += Final
                    Final = ""
                Num = ""
        else: #If this is a space, then break the Num.
            TestDigit = len(Final) + len(Num) 
            Digit = len(Final)
            if TestDigit + 1 <= width - a:
                Final += Num + " "
            elif TestDigit == width - a:
                Final += Num + "\n"
                Final = ""
            else: #If there is no space for a new word & there are spaces for space, add certain number of space.   
                Final += "\n" + Num + " "
                a = len(Num) 
                Boss += Final
                Final = ""
            Num = ""
    return Boss[:-1] + "."
     
def RemoveLastSpaceGetNewSpace(n,width):
    Final = ""
    NumLines = n.count('\n')
    for i in range(NumLines + 1):
        if i < NumLines + 1:
            NewLine = n.splitlines()[i][:-1]
            SpacesToBeAdd = width - len(NewLine)
            for s in range(SpacesToBeAdd):
                NewLine = " " + NewLine
            Final += NewLine + "\n"
        else:
            NewLine = n.splitlines()[i]
            SpacesToBeAdd = width - len(NewLine)
            for s in range(SpacesToBeAdd):
                NewLine = " " + NewLine
            Final += NewLine          
    return Final 

#################################################
# Hw2 SOLO problems
#################################################


"""
List your style fixes here:
1: Comment: There is no comment in the code. I added 4 comments.

2: Vraible names: the variable names do not follow the camelCase format 
and one of them is a built-in function name. I changed the variable names 
'count_matches_1', 'count_matches_1', 'str' to 
'countMatches1', 'countMatches2', 'j'

3: Formatting: I added a whitespace: 
Changing 'count_matches_1= 0' to 'count_matches_1 = 0'

4: Test functions: This function is reasonably testable, so I added a test 
function.

5: Magic numbers: 1 is not a magic number, so there is no need to store the 
number in a variable. I delete 'one = 1' and change 'one' in the code to 1. 
"""

#Returns True if two strings contain the same letters in possibly-different orders
def areAnagrams(s1, s2):
    if len(s1) != len(s2): #Check if digits match
        return False
        print("bad case")
    if len(s1) == len(s2):
        for j in s1:
            countMatches1 = 0
            countMatches2 = 0
            for i in range(len(s1)): #Check s1 have how many letter j
                if s1[i] == j:
                    countMatches1 += 1
            for i in range(len(s2)): #Check s2 have how many letter j
                if s2[i] == j:
                    countMatches2 += 1
            if countMatches1 != countMatches2:
                return False
        return True
    
#Test if the function works
def testareAnagrams():
    print("areAnagrams()...", end="")
    assert(areAnagrams("smart", "trams") == True)
    assert(areAnagrams("read", "dared") == False)
    print("Passed.")
testareAnagrams()

#Find the longest substring in both s1 and s2
def longestCommonSubstring(s1, s2):
    final = ""
    final1 = ""
    for i in range(len(s1)):
        for j in range(1, len(s1)+1):
            strS1 = s1[i:j] #String in s1
            for s in range(len(s2)):
                for n in range(1, len(s2)+1):
                    strS2 = s2[s: n] #Stirng in s2
                    if strS1 == strS2: #Compare
                        final1 = strS1
                        if len(final1) > len(final):
                            if final == "":
                                final = final1
                            else: final = final1
                        elif len(final1) == len(final):
                            if final1 < final:
                                final = final1
    return final    
### getEvalSteps is a bonus problem, and therefore optional ###
# Note: Bonus problems are solo. Do not collaborate on bonus problems.
def getEvalSteps(expr):
    return

#################################################
# Hw3 Graphics Functions
# All graphics must go under here to avoid angering the autograder!
# ignore_rest
#################################################
from tkinter import *

def asciiDraw(canvas,artStr,width,height):
    if artStr.count("\n") == 1:
        artStr = artStr.replace("\n","")
        for i in range(8):
            x = deciToBi(i)
            canvas.create_rectangle(width/4 * (i % 4), height/2 * (i // 4), 
                                    width/4 * (i % 4 + 1), height/2 * (i // 4 + 1), fill=x, width = 0)
    else:
        num = 1
        countLoop = 0
        countNewLine = artStr.count("\n") - 1
        while countNewLine > 0: #Every Row
            dis = artStr.find('\n',num)   #1,50,        
            nIndexLeft = artStr.find("\n", num) #First letter index of the name
            for j in range(nIndexLeft + 1,len(artStr)):
                c = artStr[j] 
                if c == "\n":
                    thisIsSpace = False
                    newLine = countSpace = countRec = countDouble = 0 
                    for i in artStr[nIndexLeft:j]: #Every row every letter index 34,52
                        rows = artStr.count("\n") + 1
                        everyWidth = width/getRows(artStr)
                        everyHeight = height/rows
                        x1 = x2 = 0
                        if i == "\n":
                            countLoop += 1 #control height
                            thisIsSpace = "\n"
                        elif not i.isspace() and thisIsSpace == "\n":
                            countDouble += 1
                            x1 = (countRec-1) * everyWidth + countSpace * everyWidth + everyWidth * countDouble
                            y1 = countLoop * everyHeight
                            x2 = x1 + everyWidth  
                            y2 = y1 + everyHeight 
                            thisIsSpace = False
                            x = deciToBi(int(i))
                            canvas.create_rectangle(x1,y1,x2,y2,fill=x)
                            countRec += 1
                        elif i.isspace() and thisIsSpace == False:
                            countSpace += 1 #First space
                            thisIsSpace = True
                        elif i.isspace() and thisIsSpace:
                            countSpace += 1 #The second third...space
                            thisIsSpace = True
                        elif not i.isspace() and thisIsSpace:
                            x1 = countRec * everyWidth + countSpace * everyWidth
                            y1 = countLoop * everyHeight
                            x2 = x1 + everyWidth
                            y2 = y1 + everyHeight
                            x = deciToBi(int(i))
                            canvas.create_rectangle(x1,y1,x2,y2,fill=x)
                            thisIsSpace = False
                            countRec += 1 #How many rectangle that have been drawn this row
                        elif not i.isspace() and thisIsSpace == False:
                            countDouble += 1
                            x1 = (countRec + countSpace) * everyWidth 
                            y1 = countLoop * everyHeight
                            x2 = x1 + everyWidth  
                            y2 = y1 + everyHeight 
                            thisIsSpace = False
                            x = deciToBi(int(i))
                            canvas.create_rectangle(x1,y1,x2,y2,fill=x)
                            countRec += 1
                    break
                else:
                    continue
            countNewLine -= 1
            num = dis + 1

def getRows(artStr):  
    num = 1
    rowss = 0
    countNewLine = artStr.count("\n") - 1
    while countNewLine > 0: #Every row
        dis = artStr.find('\n',num)
        nIndexLeft = artStr.find("\n", num) #Name's first letter's index
        for j in range(nIndexLeft + 1,len(artStr)):
            c = artStr[j] 
            if c == "\n":
                rows = 0.99*(j - nIndexLeft)
                if rows > rowss:
                    rowss = rows 
                    break
                else:
                    break
        num = dis + 1
        countNewLine -= 1
    return rowss

def deciToBi(n):
    onesDigit = (n % 2 ** 1)//(2 ** 0)
    twosDigit = (n % 2 ** 2)//(2 ** 1)
    threesDigit = (n % 2 ** 3)//(2 ** 2)
    binaryValue = str(threesDigit*100 + twosDigit * 10 + onesDigit)
    binaryValue = binaryValue.zfill(3)
    binaryValue = binaryValue.replace("1","F")
    return "#" + binaryValue


#################################################
# Hw3 Test Functions
#################################################

import string


def testGradebookSummary():
    print("Testing gradebookSummary()...", end="")
    import os
    if not os.path.exists("hw3_files"):
        assert False,"You need to unzip hw3_files.zip to test gradebookSummary"

    assert(gradebookSummary("hw3_files/gradebook1.txt") == 
            "wilma\t92.67\nfred\t90.40\nbetty\t88.00")
    assert(gradebookSummary("hw3_files/gradebook2.txt") == 
            "wilma\t92.67\nfred\t90.40\nbetty\t88.00")
    assert(gradebookSummary("hw3_files/small1.txt") == 
            "fred\t0.00")
    assert(gradebookSummary("hw3_files/small2.txt") == 
            "fred\t-1.00\nwilma\t-2.00")
    assert(gradebookSummary("hw3_files/small3.txt") == 
            "fred\t100.50")
    assert(gradebookSummary("hw3_files/small4.txt") == 
            "fred\t49.00\nwilma\t50.00")
    print("Passed.")
    
testGradebookSummary()

def testApplyCaesarCipher():
    print("Testing applyCaesarCipher()...", end="")
    assert(applyCaesarCipher("abcdefghijklmnopqrstuvwxyz", 3) == \
        "defghijklmnopqrstuvwxyzabc")
    assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
    assert(applyCaesarCipher("1234", 6) == "1234")
    print("Passed.")
    
def testRightJustifyText():
    print("Testing rightJustifyText()...", end="")
    text1 = """\
We hold these truths to be self-evident:  that all men are created equal;
that they are endowed by their Creator with certain unalienable rights;
that among these are life, liberty, and the pursuit of happiness."""
    text1Result = """\
    We hold these truths to be
self-evident: that all men are
  created equal; that they are
 endowed by their Creator with
   certain unalienable rights;
    that among these are life,
   liberty, and the pursuit of
                    happiness."""
    assert(rightJustifyText(text1, 30) == text1Result)
    text2 = """\
Though, in reviewing the incidents of my administration,
I am unconscious of intentional error, I am nevertheless too sensible of my
defects not to think it probable that I may have committed many errors.
I shall also carry with me the hope that my country will view them with
indulgence; and that after forty-five years of my life dedicated to its service
with an upright zeal, the faults of incompetent abilities will be consigned to
oblivion, as I myself must soon be to the mansions of rest.

I anticipate with pleasing expectation that retreat in which I promise myself
to realize the sweet enjoyment of partaking, in the midst of my fellow-citizens,
the benign influence of good laws under a free government,
the ever-favorite object of my heart, and the happy reward,
as I trust, of our mutual cares, labors, and dangers."""
    text2Result = """\
         Though, in reviewing the incidents of my administration, I am
unconscious of intentional error, I am nevertheless too sensible of my
       defects not to think it probable that I may have committed many
 errors. I shall also carry with me the hope that my country will view
      them with indulgence; and that after forty-five years of my life
          dedicated to its service with an upright zeal, the faults of
 incompetent abilities will be consigned to oblivion, as I myself must
           soon be to the mansions of rest. I anticipate with pleasing
     expectation that retreat in which I promise myself to realize the
 sweet enjoyment of partaking, in the midst of my fellow-citizens, the
            benign influence of good laws under a free government, the
ever-favorite object of my heart, and the happy reward, as I trust, of
                                our mutual cares, labors, and dangers."""
    assert(rightJustifyText(text2, 70) == text2Result)
    print("Passed.")

def testLongestCommonSubstring():
    print("Testing longestCommonSubstring()...", end="")
    assert(longestCommonSubstring("abcdef", "abqrcdest") == "cde")
    assert(longestCommonSubstring("abcdef", "ghi") == "")
    assert(longestCommonSubstring("", "abqrcdest") == "")
    assert(longestCommonSubstring("abcdef", "") == "")
    assert(longestCommonSubstring("abcABC", "zzabZZAB") == "AB")
    print("Passed.")
   
def runAsciiDraw(artStr, width, height):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    asciiDraw(canvas, artStr, width, height)
    root.mainloop()
    
def testAsciiDraw():
    testPattern="0123\n4567"
    print("Testing asciiDraw with color pattern:\n",testPattern,end="")
    runAsciiDraw(testPattern, 600, 300)
    
    diamondPattern=''' 
  1     2     4
 111   222   444
11111 22222 44444
 111   222   444
  1     2     4
 '''
 
    print("Testing asciiDraw with diamond pattern:\n",diamondPattern,end="")
    runAsciiDraw(diamondPattern, 600, 300)
    
    facePattern = ''' 
                          0022222222222222222
                      02222222222222222222222220
                   02222222222222222222222222222220         02   02 02
   0 0 0        02222222222222222222222222222222222220       02 22 2202
0 2 2 02      0222222222    2222222222222    2222222220       02202202
022222202     0222222222      22222222222      22222222220    02222222
  0222222    02222222222      22222222222      22222222222222222222222
  02222222222222222222222    2222222222222    22222222222222  0222
   022202222222222222222222222222222222222222222222222222222    0222
    022   022222222222222222222222222222222222222222222222222     02220
   0220   222222222222222222222222222222222222222222222222222       2220
   022    222222222222222222222222222222222222222222222000222222022220
  0222022222  2222222222222222222222222222222222222   022222222222222222
  0222   202222   2222222222222222222222222222222222     02220
 0222       0222    022222222222222222222222222220      0222
            02220     02222222222222222220220           022
              0220          02202222220              0222
               02220                                02220
                022220      02222220022220        02222
                  0222220     022222222220   022220
                     0222220  022222222222220
                        02222222022222222222
                                022222222222
                                   022222222222
                                     02222222220
                                      02220
                                      
 '''
    print("Testing asciiDraw with face pattern:\n",facePattern,end="")
    runAsciiDraw(facePattern, 800, 600)

    hourglassPattern = ''' 
                            0000
        00000000000000000000    00
00000000            0000000000000 00
0 000000000000000000         000000 00
0000                11111    0 0   00 00
00 0        111111111111111110 0   0000 0
 0 000000111111111111111111110 00000 0000
 0 0   0 111111111111111111110 0   0 0
 0 0   0 111111111111111555550 0   0 0
 0 0   0 111111111555644644640 0   0 0
 0 0   0 111115546446446446440 0   0 0
 0 0   0 111546464464464464460 0   0 0
 0 0   0 154644644644644646660 0   0 0
 0 0   0 056446446446666666660 0   0 0
 0 0   0 0 5666666666666666650 0   0 0
 0 0   0 0  566666666666666510 0   0 0
 0 0   0 0   16666666666661  0 0   0 0
 0 0   0 0    116666666651   0 0   0 0
 0 0   0 0       1156111     0 0   0 0
 0 0   0 0         55        0 0   0 0
 0 0   0 0      11165111     0 0   0 0
 0 0   0 0    1111156111111  0 0   0 0
 0 0   0 0   111111551111111 0 0   0 0
 0 0   0 0  111111165111111110 0   0 0
 0 0   0 0 1111111155111111110 0   0 0
 0 0   0 011111111161111111110 0   0 0
 0 0   0 011111111161111111110 0   0 0
 0 0   0 111111115666511111110 0   0 0
 0 0   0 111111156666651111110 0   0 0
 0 0   0 111111566666665111110 0   0 0
 0 0   01111115666666666511110 0   0 0
 0 0 0001111156666666666651110 00000 0000
 0 00   1111566666666666665110 0   000 00
 0 0    1111566666666666666510 0     00 0
00000   0115666666666666666510 0   00  00
0    00000000006666660000    000 00  00
0000000000000  111111  0000000000  00
            00000000000000000000000
 '''
    print("Testing asciiDraw with hourglass pattern:\n",hourglassPattern,end="")
    runAsciiDraw(hourglassPattern, 400, 600)
    print("Done testing asciiDraw!")

def testBonusGetEvalSteps():
    print("Testing getEvalSteps()...", end="")
    assert(getEvalSteps("0") == "0 = 0")
    assert(getEvalSteps("2") == "2 = 2")
    assert(getEvalSteps("3+2") == "3+2 = 5")
    assert(getEvalSteps("3-2") == "3-2 = 1")
    assert(getEvalSteps("3**2") == "3**2 = 9")
    assert(getEvalSteps("31%16") == "31%16 = 15")
    assert(getEvalSteps("31*16") == "31*16 = 496")
    assert(getEvalSteps("32//16") == "32//16 = 2")
    assert(getEvalSteps("2+3*4") == "2+3*4 = 2+12\n      = 14")
    assert(getEvalSteps("2*3+4") == "2*3+4 = 6+4\n      = 10")
    assert(getEvalSteps("2+3*4-8**3%3") == """\
2+3*4-8**3%3 = 2+3*4-512%3
             = 2+12-512%3
             = 2+12-2
             = 14-2
             = 12""")
    assert(getEvalSteps("2+3**4%2**4+15//3-8") == """\
2+3**4%2**4+15//3-8 = 2+81%2**4+15//3-8
                    = 2+81%16+15//3-8
                    = 2+1+15//3-8
                    = 2+1+5-8
                    = 3+5-8
                    = 8-8
                    = 0""")
    print("Passed.")

#################################################
# Hw3 Main
#################################################

def testAll():
    testGradebookSummary()
    testApplyCaesarCipher()
    testRightJustifyText()
    testLongestCommonSubstring()
    testAsciiDraw()
    
    #Uncomment the next line if you want to try the bonus!
    #testBonusGetEvalSteps()


def main():
    cs112_s19_week3_linter.lint() # check for banned tokens
    testAll()

if __name__ == '__main__':
    main()