# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 15:37:00 2019

@author: Yelena
"""
import copy

#Check if the 2d list is right
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
    valid = [(2, 1), (1, 2),  3
             (-2, 1), (1, -2),  -1
             (2, -1), (-1, 2),  1
             (-2, -1), (-1, -2)]  -3
    return (dr, dc) in valid

#returns True if it represents a legal knight's tour and False otherwise.
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



#return a new list and should not modify the provided list
def nondestructiveRemoveRowAndCol(lst, row, col):
    ret = []
    for i, r in enumerate(lst):
        if i != row:
            ret.append(copy.deepcopy(lst[i]))
    for i in range(len(ret)):
        ret[i].pop(col)
    return ret

#modify the original list, and should not return anything
def destructiveRemoveRowAndCol(lst, row, col):
    lst.pop(row)
    for i in range(len(lst)):
        lst[i].pop(col)


#################################################
# Hw5 Test Functions
#################################################
def test_isKnightsTour_1():
    board = [[1, 60, 39, 34, 31, 18, 9, 64],
             [38, 35, 32, 61, 10, 63, 30, 17],
             [59, 2, 37, 40, 33, 28, 19, 8],
             [36, 49, 42, 27, 62, 11, 16, 29],
             [43, 58, 3, 50, 41, 24, 7, 20],
             [48, 51, 46, 55, 26, 21, 12, 15],
             [57, 44, 53, 4, 23, 14, 25, 6],
             [52, 47, 56, 45, 54, 5, 22, 13],
             ]
    assert (isKnightsTour(board) == True)
    print("Passed.")


def test_isKnightsTour_2():
    board = [[1, 62, 39, 34, 31, 18, 9, 64],
             [38, 35, 32, 61, 10, 63, 30, 17],
             [59, 2, 37, 40, 33, 28, 19, 8],
             [36, 49, 42, 27, 62, 11, 16, 29],
             [43, 58, 3, 50, 41, 24, 7, 20],
             [48, 51, 46, 55, 26, 21, 12, 15],
             [57, 44, 53, 4, 23, 14, 25, 6],
             [52, 47, 56, 45, 54, 5, 22, 13],
             ]
    assert (isKnightsTour(board) == False)
    print("Passed.")


def test_isKnightsTour_3():
    board = [[1, 60, 39, 34, 31, 18, 9, 64],
             [38, 2, 32, 61, 10, 63, 30, 17],
             [59, 35, 37, 40, 33, 28, 19, 8],
             [36, 49, 42, 27, 62, 11, 16, 29],
             [43, 58, 3, 50, 41, 24, 7, 20],
             [48, 51, 46, 55, 26, 21, 12, 15],
             [57, 44, 53, 4, 23, 14, 25, 6],
             [52, 47, 56, 45, 54, 5, 22, 13],
             ]
    assert (isKnightsTour(board) == False)
    print("Passed.")

def test_nondestructiveRemoveRowAndCol():
    lst = [[2, 3, 4, 5],
           [8, 7, 6, 5],
           [0, 1, 2, 3]]
    result = [[2, 3, 5],
              [0, 1, 3]]
    lstCopy = copy.deepcopy(lst)
    assert (nondestructiveRemoveRowAndCol(lst, 1, 2) == result)
    assert(lst == lstCopy), "input list should not be changed"
    print("Passed.")

def test_destructiveRemoveRowAndCol():
    lst = [[2, 3, 4, 5],
           [8, 7, 6, 5],
           [0, 1, 2, 3]]
    result = [[2, 3, 5],
              [0, 1, 3]]
    assert (destructiveRemoveRowAndCol(lst, 1, 2) == None)
    assert (lst == result), "input list should be changed"
    print("Passed.")

if __name__ == '__main__':
    test_isKnightsTour_1()
    test_isKnightsTour_2()
    test_isKnightsTour_3()
    test_nondestructiveRemoveRowAndCol()