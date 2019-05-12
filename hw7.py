    # -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 17:10:59 2019

@author: tianminz
"""
#################################################
# Hw7 Big-O Calculation
#################################################

# 1A: Exchange the first and last element of the list
def slow1(lst): # N is the length of the list lst
    assert(len(lst) >= 2)
    a = lst.pop()    # O(1)
    b = lst.pop(0)   # O(N)
    lst.insert(0, a) # O(N)
    lst.append(b)    # O(1)
# 1B: O(N)  
def fast1(lst):
    assert(len(lst) >= 2) 
    first = lst[0]               # O(1)
    lst[0] = lst[len(lst) - 1]   # O(1)
    lst[len(lst) - 1] = first    # O(1)
# 1D: O(1)

# 2A: Count the unrepeated elements in lst
def slow2(lst): # N is the length of the list lst
    counter = 0                   # O(1)
    for i in range(len(lst)):     # N Loops
        if lst[i] not in lst[:i]: # O(N)
            counter += 1          # O(1)
    return counter                # O(1)
# 2B: O(N**2)
def fast2(lst):
    newLst = set(lst)   # O(1)
    return len(newLst)  # O(1)
# 2D: O(1)

# 3A: return the element which shows the most times, 
# 3A:if more than one, return the smallest one.
import string
def slow3(s): # N is the length of the string s
    maxLetter = ""                              # O(1)
    maxCount = 0                                # O(1)
    for c in s:                                 # N Loops
        for letter in string.ascii_lowercase:   # 26 Loops
            if c == letter:                     # O(1)
                if s.count(c) > maxCount or \
                   s.count(c) == maxCount and \
                   c < maxLetter:               # O(N)
                    maxCount = s.count(c)       # O(N)
                    maxLetter = c               # O(1)
    return maxLetter                            # O(1)
# 3B: O(N**2) 
def fast3(s):
    dic = dict()                        # O(1)
    maxCount = 0                        # O(1)
    maxLetter = ""                      # O(1)
    for i in s:                         # O(N)
        for i in string.ascii_lowercase: # 26 Loops
            key = i                     # O(1)
            if i in dic:                # O(1)
                dic[key] += 1           # O(1)
            else:                       # O(1)
                dic[key] = 1            # O(1)
    for item in dic:                    # O(N)
        if dic[item] > maxCount or \
           dic[item] == maxCount and \
           item < maxLetter:            # O(1)
            maxCount = dic[item]        # O(1)
            maxLetter = item            # O(1)
    return maxLetter                    # O(1)           
# 3D:O(N)

# 4A: The largest absulote value of element in one list subtracts
# 4A: element in the other list.
def slow4(a, b): # a and b are lists with the same length N
    assert(len(a) == len(b))
    result = abs(a[0] - b[0])    # O(1)
    for c in a:                  # N Loops
        for d in b:              # N Loops
            delta = abs(c - d)   # O(1)  
            if (delta > result): # O(1)
                result = delta   # O(1)
    return result                # O(1)
# 4B: O(N**2)
def fast4(a, b):
    assert(len(a) == len(b))     # O(1)
    testA = abs(max(a) - min(b)) # O(N)
    testB = abs(max(b) - min(a)) # O(N)
    if testA > testB:            # O(1)
        return testA             # O(1)
    return testB
# 4D: O(N)

import time
#returns True if 3 values anywhere in the list 
#form a Pythagorean Triple
def containsPythagoreanTriple(lst):
    newLst = [i ** 2 for i in lst] 
    setLst = set(newLst)
    for i in setLst:
        for j in setLst:
            if i + j in setLst:
                return True
    return False

#if a pair of numbers in the given list add up to target
#returns that pair as a tuple; otherwise, it returns None.
def getPairSum(lst, target):
    dic = dict()
    for i in lst:
        if i in dic:
            dic[i] += 1  
        else:
            dic[i] = 1
    for key in dic:
        j = target - key
        if j in dic:
            if key == j and dic[key]>1:
                return (key,j)
            if key != j:
                return (key,j)
    return None

#returns a tuple of: the number of selection comparisons, 
#the number of swaps and the time it takes in seconds to run.
def instrumentedSelectionSort(a):
    start = time.time()
    numSwap = 0
    comparisons = 0
    n = len(a)
    for startIndex in range(n):
        minIndex = startIndex
        for i in range(startIndex+1, n):
            comparisons += 1 
            if (a[i] < a[minIndex]):
                minIndex = i
        swap(a, startIndex, minIndex)
        numSwap += 1 
    end = time.time()
    elapsed1 = end - start
    return (comparisons, numSwap, elapsed1)  

#returns a tuple of: number of bubble comparisons, 
#number of swaps, time it takes in seconds to run the sort.
def instrumentedBubbleSort(a):
    start = time.time()
    numSwap = 0
    comparisons = 0
    n = len(a)
    end = n
    swapped = True
    while (swapped):
        swapped = False
        for i in range(1, end):
            comparisons += 1 #Compare
            if (a[i-1] > a[i]):
                swap(a, i-1, i)
                swapped = True
                numSwap += 1 #Swaps
        end -= 1  
    end = time.time()
    elapsed1 = end - start
    return (comparisons, numSwap, elapsed1)     
    
def swap(a, i, j):
    (a[i], a[j]) = (a[j], a[i])

import random
#Compare two corts and show which sort runs in less time
#Show which sort uses fewer comparisons
#Show which sort makes fewer swaps
def selectionSortVersusBubbleSort(): 
    listLength = 1000
    square = 2
    list1 = [i for i in range(listLength, 1, -1)]
    totalTimeB = instrumentedBubbleSort(list1)[2]
    totalTimeS = instrumentedSelectionSort(list1)[2]       
    print("\nReport of Comparison Sort:",\
          "\nThis is a list of length", listLength, \
          "\nIn bubble sort it takes", totalTimeB, \
          "\nIn selection sort it takes", totalTimeS)  
    for n in range(2,6): # n times the origianl length
        listN = [i for i in range(listLength * n, 1, -1)]
        totalTimeBN = instrumentedBubbleSort(listN)[2]
        totalTimeSN = instrumentedSelectionSort(listN)[2]    
        print("\nThis is a list of length", listLength * n,\
              ", which is", n, "times the first length,"\
              "\nin bubble sort it takes", totalTimeBN, \
              ", which is", round(totalTimeBN/totalTimeB,1),\
              "times the first list.",\
              "\nIn selection sort it takes", totalTimeSN,\
              ", which is", round(totalTimeSN/totalTimeS,1),\
              "times the first list.")
        print("As", round(totalTimeBN/totalTimeB,1),\
              "is close to", n**square, ","\
              " and", round(totalTimeSN/totalTimeS,1),\
              "is also close to", n**square , ","\
              " both selectionSort and bubbleSort\
              are quadratic (O(N**2))")
    compareSwapAndCom()

#Generates random lists and compares swaps and comparisons 
#used in bubble sort and selection sort.
def compareSwapAndCom(): 
    testTime = 4     
    numMax = 10000
    listLength = 1000
    for i in range(1,testTime):
        sampleList = random.sample(range(numMax), listLength * i) 
        if instrumentedBubbleSort(sampleList)[2] > \
           instrumentedSelectionSort(sampleList)[2]:    
            print("Length is", listLength * i,\
                  "Selection sort runs in less time")
        else:
            print("Length is", listLength * i,\
                  "Bubble sort runs in less time")
        if  instrumentedBubbleSort(sampleList)[0] > \
            instrumentedSelectionSort(sampleList)[0]:
            print("Length is",listLength * i,\
                  "Selection sort uses fewer comparisons")
        else:
            print("Length is", listLength * i,\
                  "Bubble sort uses fewer comparisons")     
        if instrumentedBubbleSort(sampleList)[1] > \
           instrumentedSelectionSort(sampleList)[1]:
            print("Length is", listLength * i, \
                  "Selection sort makes fewer swaps")
        else:
            print("Length is", listLength * i, \
                  "Bubble sort makes fewer swaps")  


#################################################
# Hw7 SOLO problems
#################################################
def movieAwards(a):
    dic = dict()
    for item in a:
        if item[1] in dic:
            key = item[1]
            dic[key] += 1
        else:
            key = item[1]
            dic[key] = 1
    return dic       

def friendsOfFriends(d):
    output = dict()
    for key in d: #pod
        value = set()
        output[key] = value
        for ele in d[key]: #"tyrion", "brienne", "jaime"
            for item in d[ele]:  #"jon", "jaime", "pod"
                if (item != key and item not in d[key]):
                    value.add(item)
        output[key] = value
    return output

#################################################
# Hw2 test function
#################################################
def testBigO():
    print("Testing bigO...", end="")
    lst = [1,2,3,2,3,4]
    lst2 = "absgdehDF"
    lst3 = [1,6,8,9,10,2]
    assert(slow1(lst) == fast1(lst))
    assert(slow2(lst) == fast2(lst))
    assert(slow3(lst2) == fast3(lst2))
    assert(slow4(lst, lst3) == fast4(lst, lst3))
    print("Done.")
    
def testContainsPythagoreanTriple():
    print("Testing containsPythagoreanTriple...", end="")
    assert(containsPythagoreanTriple([1, 3, 6, 2, 5, 1, 4]) == True)
    assert(containsPythagoreanTriple([3, 7, 2, 5, 4]) == True)
    assert(containsPythagoreanTriple([1, 3, 6, 2, 1, 4]) == False)
    print("Done.")
    
def testGetPairSum():
    print("Testing getPairSum...", end="")
    assert(getPairSum([1], 1) == None)
    assert(getPairSum([5, 2], 7) in [ (5, 2), (2, 5) ])
    assert(getPairSum([10, -1, 1, -8, 3, 1], 2) \
           in [ (10, -8), (-8, 10), (-1, 3), (3, -1), (1, 1) ])
    assert(getPairSum([10, -1, 1, -8, 3, 1], 10) == None)
    assert(getPairSum([1,4,3],2) == None)
    print("Done.")
    
def testInstrumentedSelectionSort():
    print("Testing instrumentedSelectionSort...", end="")
    print(instrumentedSelectionSort([1,3,5,7,9,2,4,6,8,10,11,13,15,\
                                     1,3,5,7,9,2,4,6,8,10,11,13,15,\
                                     1,3,5,7,9,2,4,6,8,10,11,13,15,\
                                     1,3,5,7,9,2,4,6,8,10,11,13,15]))
    print("Done.")
    
def testInstrumentedBubbleSort():
    print("Testing instrumentedBubbleSort...", end="")
    print(instrumentedBubbleSort([1,3,5,7,9,2,4,6,8,10,11,13,15,\
                                  1,3,5,7,9,2,4,6,8,10,11,13,15,\
                                  1,3,5,7,9,2,4,6,8,10,11,13,15,\
                                  1,3,5,7,9,2,4,6,8,10,11,13,15]))

def testmovieAwards():
    print("Testing movieAwards...", end="")
    print(movieAwards(\
  { 
    ("Best Picture", "Green Book"), 
    ("Best Actor", "Bohemian Rhapsody"),
    ("Best Actress", "The Favourite"),
    ("Film Editing", "Bohemian Rhapsody"),
    ("Best Original Score", "Black Panther"),
    ("Costume Design", "Black Panther"),
    ("Sound Editing", "Bohemian Rhapsody"),
    ("Best Director", "Roma")
  }) ==

  { 
    "Black Panther" : 2,
    "Bohemian Rhapsody" : 3,
    "The Favourite" : 1,
    "Green Book" : 1,
    "Roma" : 1
  })
  
def testFriendsOfFriends():  
    print("Testing friendsOfFriends...", end="")
    d = { }
    d["jon"] = set(["arya", "tyrion"])
    d["tyrion"] = set(["jon", "jaime", "pod"])
    d["arya"] = set(["jon"])
    d["jaime"] = set(["tyrion", "brienne"])
    d["brienne"] = set(["jaime", "pod"])
    d["pod"] = set(["tyrion", "brienne", "jaime"])
    d["ramsay"] = set()  
    assert(friendsOfFriends(d) == 
    {
     'tyrion': {'arya', 'brienne'}, 
     'pod': {'jon'}, 
     'brienne': {'tyrion'}, 
     'arya': {'tyrion'}, 
     'jon': {'pod', 'jaime'}, 
     'jaime': {'pod', 'jon'}, 
     'ramsay': set()
    })
    print("Done.")
    
def testAll():
    testBigO()
    testContainsPythagoreanTriple()
    testGetPairSum()
    testInstrumentedSelectionSort()
    testInstrumentedBubbleSort()
    selectionSortVersusBubbleSort()
    ### Solo problems ###
    testmovieAwards()
    testFriendsOfFriends()

testAll()
