# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:01:18 2020

@author: RAHUL SINGH
"""

import numpy as np 
import random as ran
import matplotlib.pyplot as plt

def cointoss(trials,coins): #cointoss function
    N = trials    
    number_of_coins = coins 

    heads = []  #number of heads in a trial array
    Q_heads = [] 
    tails = [] #number of tails in a trial array
    Q_tails = []
    numero  = []
    head_count_array = np.linspace(0,number_of_coins,number_of_coins + 1)
    head_freq_count = np.zeros(number_of_coins + 1) #head frequency array
    tail_freq_count = np.zeros(number_of_coins + 1) #tails frequency array
    
    for trial in range(N): #result generator loop
        head_count = 0
        
        for coin_number in range(number_of_coins):
            toss_outcome = ran.randint(0,1)
            if toss_outcome == 1:
                head_count += 1       
        heads.append(head_count)
        tails.append(number_of_coins - head_count)
        
    #print("\nhead outcome: ",heads)
    #print("\ntails outcome: ",tails)        
    
    for counts in heads:  #head counting loop
        for number in range(0,number_of_coins+1):
            if counts == number:
                head_freq_count[number] += 1
    
    for counts in tails: #tails counting loop
        for number in range(0,number_of_coins+1):
            if counts == number:
                tail_freq_count[number] += 1
                
    print("\nfrequency of heads: ",head_freq_count)
    print("\nfrequency of tails: ",tail_freq_count)
    
    sum_heads = np.sum(heads) 
    if number_of_coins < 10:
        plt.figure(1)
        plt.subplot(2,1,1)
        plt.plot(head_count_array,head_freq_count/sum_heads,".-",label= "coins= "+str(number_of_coins))
        plt.legend()
        plt.grid(5)
        plt.xlabel("NUMBER OF HEADS")
        plt.ylabel("PROBABLITY OF FREQUENCY OF HEADS")
        plt.title("")
    if number_of_coins == 10:
        plt.figure(2)
        plt.plot(head_count_array,head_freq_count/sum_heads,"-.",label = "trials= "+str(N))
        plt.legend()
        plt.grid(5)
        plt.xlabel("NUMBER OF HEADS")
        plt.ylabel("PROBABLITY OF FREQUENCY OF HEADS")
        plt.title("PLOT FOR 10 COINS WITH VARYING TRIALS")
        
        sum_cum_heads = 0
        sum_cum_tails = 0
    
        if N == 10000:
        
            for index in range(N):
                sum_cum_heads += heads[index]
                sum_cum_tails += tails[index]
                Q_heads.append(sum_cum_heads/(10*(index+1))) #cumilitive heads 
                Q_tails.append(sum_cum_tails/(10*(index+1))) #cumilitive tails
                numero.append(index) 

            plt.figure(3)
            plt.plot(numero,Q_heads,"*",label="heads")
            plt.plot(numero,Q_tails,".",label="tails")
            plt.grid(5) 
            plt.title("CUMALATIVE PLOT")
            plt.legend()

    if number_of_coins > 10:
        plt.figure(1)
        plt.subplot(2,1,2)
        plt.plot(head_count_array,head_freq_count/sum_heads,".-",label= "coins= "+str(number_of_coins))
        plt.legend()
        plt.grid(5)
        plt.xlabel("NUMBER OF HEADS")
        plt.ylabel("PROBABLITY OF FREQUENCY OF HEADS")                    
        
x1 = cointoss(10000,2)
x2 = cointoss(10000,3)
x3 = cointoss(10000,4)
x4 = cointoss(10000,5)
x5 = cointoss(10000,6) 
x101 = cointoss(10,10)
x102 = cointoss(100,10)
x103 = cointoss(10000,10)
y1 = cointoss(100000,20)
y2 = cointoss(100000,30)
y3 = cointoss(100000,40)
plt.show()