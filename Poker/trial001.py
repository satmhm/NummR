
from re import L
from stat import FILE_ATTRIBUTE_REPARSE_POINT
import pandas as pd
import numpy as np
import random
import tensorflow as tf

def player():
    Nplayer = np.random.lognormal(mean = 6, sigma= 0., size =1)


def distribute(Nplayer):
    Nplayer = 2*Nplayer
    whole = []
    card_on_hands =[]
    flop_table = []
    turn_table = []
    river_table = []

    for i in range(1,53,1):
       whole.append(i)
    
    for j in range(Nplayer):
        a = random.choice(whole)
        card_on_hands.append(a)
    
    for k in card_on_hands:
        whole.remove(k)
    
    #bet_1


    #round_1: Flop
    for l in range(1,4,1):
        b = random.choice(whole)
        flop_table.append(b)
    
    for i in flop_table:
        whole.remove(i)
    
    #bet_2

    
    #round_2: Turn
    for i in range(0,1):
        c = random.choice(whole)
        turn_table.append(c)
    turn_table = flop_table + turn_table
    whole.remove(c)

    #bet_3

    #round_3: River

    for i in range(0,1):
        d = random.choice(whole)
        river_table.append(d)
    river_table = turn_table + river_table
    whole.remove(d)

    #bet_4
        
    return card_on_hands, whole, flop_table, turn_table, river_table

print(distribute(4))
        
    

    

    








