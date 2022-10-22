# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 11:19:25 2022

@author: Stefan Hausner
"""

import numpy as np
import pandas as pd


def convert_text_to_array():
    trianglematrix = np.zeros((100,100),int)
    with open('./Problem/triangle.txt') as f:
        rowcount = 0
        for line in f:
            numbers = line.strip()
            numbers_list = numbers.split(" ")
            for it in range(len(numbers_list)):
                trianglematrix[rowcount,it] = numbers_list[it]
            rowcount += 1
    return trianglematrix

def convert_list_to_array(inputlist):
    
    inputmatrix = np.zeros((15,15),int)
    matrixrowsize = inputmatrix.shape[0]+1
    count = 0
    for i in range(1,matrixrowsize):
        for j in range(i):
            inputmatrix[i-1,j] = inputlist[count]
            count += 1
    return inputmatrix
                        
def max_path_sum(inputmatrix):
    matrixrowsize = inputmatrix.shape[0]-1
    for i in range(matrixrowsize-1, -1, -1):
        for j in range(i+1):
            inputmatrix[i,j] = max(inputmatrix[i,j]+inputmatrix[i+1,j],inputmatrix[i,j]+inputmatrix[i+1,j+1])
    return  inputmatrix[0,0]

def choose_exercise(exercise):
    
    if exercise == 1:
        trianglelist = [
                        75,
                        95,64,
                        17,47,82,
                        18,35,87,10,
                        20,4,82,47,65,
                        19,1,23,75,3,34,
                        88,2,77,73,7,63,67,
                        99,65,4,28,6,16,70,92,
                        41,41,26,56,83,40,80,70,33,
                        41,48,72,33,47,32,37,16,94,29,
                        53,71,44,65,25,43,91,52,97,51,14,
                        70,11,33,27,77,73,17,78,39,58,17,57,
                        91,71,52,38,17,14,91,43,58,50,27,29,48,
                        63,66,4,68,89,53,67,30,73,16,69,87,40,31,
                        4,62,98,27,23,9,70,98,73,93,38,53,60,4,23
                        ]
        trianglematrix1 = convert_list_to_array(trianglelist)
        maxsum = max_path_sum(trianglematrix1)
        print(maxsum)    
    
    elif exercise == 2:
        trianglematrix2 = convert_text_to_array() 
        maxsum = max_path_sum(trianglematrix2)
        print(maxsum)
    
def main():
    # choose exercise by inserting 1 or 2
    choose_exercise(2)
             
        
if __name__ == "__main__":
    main()