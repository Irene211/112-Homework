# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:52:29 2019
HW9
@author: tianminz
"""
import math

#returns the alternating sum of the list
def alternatingSum(lst, depth = 0):
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    return lst[0] - lst[1] + alternatingSum(lst[2:]) 
     
#returns a list of tuples of the values that binary search
# must check to verify whether or not item is in lst.
def binarySearchValues(lst, item, low = 0):    
    if len(lst) == 0:
        return []
    high = len(lst) 
    mid = (high - 1) // 2
    if item == lst[mid]:
        return [(mid + low, lst[mid])]
    #Recursion case
    #add low to index
    elif item < lst[mid]: 
        return [(mid + low, lst[mid])] + \
                 binarySearchValues(lst[:mid], item, low)
    else:
        return [(mid + low, lst[mid])] + \
                 binarySearchValues(lst[mid + 1 :], item, low + mid + 1)

#find the given item as a value in one of the path dictionaries. 
#If the item is found, returns a list of keys that lead to the item; 
#if it is not found, the function returns None.
def findCategoryPath(d, value):
    for key, v in d.items():
        if isinstance(v, dict):
            res = findCategoryPath(v, value)
            temp = [key]
            if res is not None:
                temp.extend(res)
                return temp
        else:
            if value == v:
                return [key]

#returns a list of the positive powers of 3 up to and including n
def powersOf3ToN(n):
    value = math.floor(n)
    #corner case
    if value <= 0:
        return []
    elif value < 3:
        return [1]
    #recursive case
    else:
        return powersOf3ToN(value//3) + [powersOf3ToN(value//3) [-1] * 3]
powersOf3ToN(30)
powersOf3ToN(10) + [powersOf3ToN(10) [-1] * 3] 
powersOf3ToN(3) + [powersOf3ToN(3) [-1] * 3] + [(  powersOf3ToN(3) + [powersOf3ToN(3) [-1] * 3)]  )  [-1] * 3] 
powersOf3ToN(1) +  [powersOf3ToN(1) [-1] * 3] + [ (  powersOf3ToN(1) +  [powersOf3ToN(1) [-1] * 3]   )  [-1] * 3]
[1] + [3] + 

#returns a tuple of two lists
#The two lists must contain all the elements of lst between them
#and the difference between the two lists is as small as possible. 
def loadBalance(lst):
    lst.sort()
    if len(lst) == 0: 
        return [], []
    if len(lst) == 1:
        return lst, []
    t1,t2 = [],[]
    while lst:
        val = lst.pop()
        if sum(t1)>sum(t2):
            t2.append(val)
        else:
            t1.append(val)
    return t1, t2

#returns a set of all balanced strings
# that can be created using n parentheses and no other characters
def generateValidParentheses(n):
    if n == 0:
        return set()
    if n%2 == 1:
        return set()
    res = set()
    genParents(res, n/2, n/2, "")
    return res   
    
def genParents(out, left, right, src):
    if left == 0 and right == 0:
        return out.add(src)
    if left > 0:
        genParents(out, left-1, right, src+"(")
    if right > 0 and right > left:
        genParents(out, left, right-1, src + ")")
            
# test function
def testalternatingSum():
    print("Testing alternatingSum...")
    assert(alternatingSum([1,2,3,4,5]) == 3)
    assert(alternatingSum([1,7,3,10,0]) == -13)
    assert(alternatingSum([11,71,3,1,20]) == -38)
    assert(alternatingSum([11,71,3,1,20,18,3,4,29,20]) == -48)
    assert(alternatingSum([]) == 0)
    return "Done..."

def testbinarySearchValues():
    print("Testing binarySearchValues...")
    assert(binarySearchValues(['a', 'c', 'f', 'g', 'm', 'q'], 'c')\
           == [(2, 'f'), (0, 'a'), (1, 'c')])
    assert(binarySearchValues(['a', 'c', 'f', 'g', 'm', 'q'], 'n')\
           == [(2, 'f'), (4, 'm'), (5, 'q')])
    
    assert(binarySearchValues(['a', 'c', 'f', 'g', 'm', 'q'], 'g') \
           == [(2, 'f'), (4, 'm'), (3, 'g')])
    return "Done..."

def testfindCategoryPath():
    d = { "Sporting" : 
        { "Spaniel" :
            { "English Springer" : "Betsy" },
          "Weimaraner" : "Xeva",
          "Retriever" :
            { "Golden" : "Sammo",
              "Labrador" : "Nya" } 
        },
      "Working" : 
        { "Husky" : "Stella",
          "Saint Bernard" : "Rutherfurd",
          "Boxer" : "Paximus" },
      "Herding" : 
        { "Corgi" :
            { "Welsh" :
                { "Cardigan" : "Geb",
                  "Pembroke" : "Niinja" } 
            },
          "Sheepdog" :
            { "Bergamasco" : "Samur",
              "Old English" : "Duggy",
              "Shetland" : "Walker" } 
        },
      "Other" : "Kimchee"
    }
    assert(findCategoryPath(d, "Samur") \
           == ["Herding", "Sheepdog", "Bergamasco"])
    assert(findCategoryPath(d, "Weimaraner") == None)
    return "Done..."


def testloadBalance():
    print("Testing loadBalance...")
    assert(loadBalance([3, 6, 1, 7, 9, 8, 22, 3]) == \
           ([3, 6, 1, 7, 9, 3], [8, 22]) or ([3, 6, 9, 8, 3], [1, 7, 22]) )
    return "Done..."

def testpowerOf3ToN():
    print("Testing powerOf3ToN...")
    assert(powersOf3ToN(10.5) == [1, 3, 9])
    assert(powersOf3ToN(2187) == [1, 3, 9, 27, 81, 243, 729, 2187])
    assert(powersOf3ToN(2000) == [1, 3, 9, 27, 81, 243, 729])
    return "Done..."

def testgenerateValidParentheses():
    print("Testing generateValidParentheses...")
    assert(generateValidParentheses(4) == { "(())", "()()" })
    assert(generateValidParentheses(6) == \
           { "((()))", "()(())", "(())()", "(()())", "()()()" })
    assert(generateValidParentheses(0) == set())
    return "Done..."

def testAll():
    print(testalternatingSum())
    print(testbinarySearchValues())
    print(testfindCategoryPath())
    print(testloadBalance())
    print(testpowerOf3ToN())
    print(testgenerateValidParentheses())
    
testAll()

