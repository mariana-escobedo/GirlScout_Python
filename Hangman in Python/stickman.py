
def updateGame(x):
    stickman = "\n ☺/\n/[]\n /\﻿"
    if x == 5:
        print(stickman)
    if x == 4:
        print(stickman[:11])
    if x == 3:
        print(stickman[:10])
    if x == 2:
        print(stickman[:6])
    if x == 1:
        print(stickman[:5])
    if x == 0:
        print(stickman[:3])
    
    
    
    
    
def gameState(s1, s2): 
    for a in s1:
        for b in s2:
            if a == b:
                continue
    return ("Win");


def replaceLetters(s1, s2, z):
    for s in s1:
        for t in s2:
            if s == z:
                t == z
    return (s2);
