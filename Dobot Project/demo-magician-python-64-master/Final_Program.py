# -*- coding: utf-8 -*-
"""
Created on Thu May  4 12:14:23 2023

@author: danie
"""

from Functions import*
import time
from Definir_posições import*
import numpy as np
import cv2

cap = cv2.VideoCapture(1)

# Minimum and maximum area thresholds for object filtering
min_area = 500
max_area = 5000

# Kernel for morphological operations
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (45, 45))

calibration()

board = {1: ' ', 2: ' ', 3: ' ',
          4: ' ', 5: ' ', 6: ' ',
          7: ' ', 8: ' ', 9: ' '}
player = 'O'
computer = 'X'

# Array to store previous object positions
prev_positions = []

def printBoard(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("\n")

def spaceIsFree(position):
    if board[position] == ' ':
        return True
    return False

def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if checkDraw():
            print("Draw!")
            return
        if checkWin():
            if letter == 'X':
                print("Dobot Magician wins!")
                #victory dance
                dance()
                return
            else:
                print("Player wins!")
                return
        return
    else:
        print("Invalid position")
        position = int(input("Please enter a new position: "))
        insertLetter(letter, position)
        return

def checkWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

def checkWhichMarkWon(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

def playerMove():

    position = 0  # Declare and initialize position outside the loop

    while True:
        ret, frame = cap.read()
        width = int(cap.get(3))
        height = int(cap.get(4))

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # Green color
        low_green = np.array([25, 52, 72])
        high_green = np.array([102, 255, 255])

        mask = cv2.inRange(hsv, low_green, high_green)

        # Perform morphological operations to remove noise
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        object_detected = False
        for contour in contours:
            # Calculate the position of the object
            x, y, w, h = cv2.boundingRect(contour)
            centroid_x = x + (w // 2)
            centroid_y = y + (h // 2)

            # Calculate the area of the contour
            area = cv2.contourArea(contour)

            if min_area <= area <= max_area:
                # Determine the position number based on the centroid coordinates
                if centroid_x < width / 3:
                    if centroid_y < height / 3:
                        position = 1
                    elif centroid_y < 2 * height / 3:
                        position = 4
                    else:
                        position = 7
                elif centroid_x < 2 * width / 3:
                    if centroid_y < height / 3:
                        position = 2
                    elif centroid_y < 2 * height / 3:
                        position = 5
                    else:
                        position = 8
                else:
                    if centroid_y < height / 3:
                        position = 3
                    elif centroid_y < 2 * height / 3:
                        position = 6
                    else:
                        position = 9

                if position != 0 and position not in prev_positions:
                    object_detected = True
                    prev_positions.append(position)
                    print("Object detected at position:", position)
                    break

        if object_detected:
            break

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    insertLetter(player, position)
    return



def dobotmove(bestMove):
    if(bestMove ==1):
        pick_inicial()
        setPosition(160,-105,-20) #posição
        posi_inicial()
    if(bestMove == 2):
        pick_inicial()
        setPosition(164,-11,-20) #posição
        posi_inicial()
    if(bestMove == 3):
        pick_inicial()
        setPosition(164,78,-20) #posição
        posi_inicial()
    if(bestMove == 4):
        pick_inicial()
        setPosition(241,-98,-20) #posição
        posi_inicial()
    if(bestMove == 5):
        pick_inicial()
        setPosition(241,-7,-20) #posição
        posi_inicial()
    if(bestMove == 6):
        pick_inicial()
        setPosition(230, 92,-20) #posição
        posi_inicial()
    if(bestMove == 7):
        pick_inicial()
        setPosition(310,-98,-20) #posição
        posi_inicial()
    if(bestMove == 8):
        pick_inicial()
        setPosition(310,-6,-20) #posição
        posi_inicial()
    if(bestMove == 9):
        pick_inicial()
        setPosition(310,100,-20) #posição
        posi_inicial()



def compMove():
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = computer
            score = minimax(board, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key
    #Robo Movement
    dobotmove(bestMove)
    
    insertLetter(computer, bestMove)

    return

def minimax(board, isMaximizing):
    if checkWhichMarkWon(computer):
        return 1
    elif checkWhichMarkWon(player):
        return -1
    elif checkDraw():
        return 0

    if isMaximizing:
        bestScore = -800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = computer
                score = minimax(board, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore
    else:
        bestScore = 800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, True)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore


# Change according to who you want to play first

while not checkWin() and not checkDraw():
    #compMove()
    playerMove()
    if not checkWin() and not checkDraw():
        compMove()
        #playerMove()