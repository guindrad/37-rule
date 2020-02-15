#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ------------------
# SECRETARY PROBLEM
# Link: https://en.wikipedia.org/wiki/Secretary_problem
# ------------------

# IMPORTS
# ------------------
# STANDART LIBRARY
import random

#THIRT PARTY
import numpy as np

# VARIABLES
# ------------------
ARRAY_SIZE = 100
incremental_percentage = 0.01


def randomize_array(min, max, size):
    """Randomize between min & max
    """

    return np.random.choice(range(ARRAY_SIZE),ARRAY_SIZE,replace=False)

def get_bigger(arr):

    return np.amax(arr)


def run_simulation(num_iterations,percentage_of_research):

    num_executions = 0
    win = 0
    thirtysevenpercent = int(ARRAY_SIZE*percentage_of_research)

    while(num_executions<num_iterations):
        
        num_compar = thirtysevenpercent
        arr = randomize_array(1,ARRAY_SIZE,ARRAY_SIZE)
        bigger_37 = get_bigger(arr[0:(thirtysevenpercent)])
        bigger_all = get_bigger(arr)

        while(num_compar<ARRAY_SIZE):

            if(arr[num_compar]>=bigger_37):

                if(arr[num_compar]>=bigger_all):
                    #print("Winner!")
                    win = win + 1

                break
            
            num_compar = num_compar + 1
             
        num_executions = num_executions+1
        
        

    print("%.4f,%.4f" % (percentage_of_research,float(win)/num_iterations))


print("\n------ 37% RULE RESULTS ------")
while(incremental_percentage<=0.99):
    run_simulation(100000,incremental_percentage)
    incremental_percentage=incremental_percentage+0.01
