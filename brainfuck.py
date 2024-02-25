#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 13:06:26 2023

@author: cenzodecarvalho
"""

def readcode(file):
    with open(file) as infile:
        lines = infile.readlines()
    stringcode='' 
    for i in lines:
        stringcode += i
    return i
        
def simplusfyhelper(plusstring):
    if '+' not in plusstring or '-' not in plusstring:
        return plusstring
    counter=0
    for i in plusstring:
        if i == '+':
            counter+=1
        elif i == '-':
            counter-=1
    if counter>0:
        return (counter*'+')
    if counter<= 0:
        return (counter*'-')

def simplusfy(string):
    #divides a string into pieces with +- and other before
    #simplifying the +- using the helper
    textsep=[]
    part=''
    p = True
    for i in range(len(string)):
        if string[i] in '+-' and p==True:
            part+=string[i]
        
        elif string[i] in '+-' and p==False:
            textsep.append(part)
            part=''
            part+=string[i]  
            p=True
        
        else:
            if p==True:
                textsep.append(part)
                part=''
                part+=string[i]  
                p=False
                
            if p==False:
                part+=string[i]
    textsep.append(part)
    for i in range(len(textsep)):
        if ('+' in textsep[i]) or ('-' in textsep[i]):
            textsep[i]=simplusfyhelper(textsep[i])
    finalplus=''
    for i in textsep:
        finalplus+=i
    return finalplus

def simarrowhelper(arrowstring):
    if '>' not in arrowstring or '<' not in arrowstring:
        return arrowstring
    counter=0
    for i in arrowstring:
        if i == '>':
            counter+=1
        elif i == '<':
            counter-=1
    if counter>0:
        return (counter*'>')
    if counter<= 0:
        return (counter*'<')

def simarrow(string):
    #divides a string into pieces with <> and other before
    #simplifying the <> using the helper
    textsep=[]
    part=''
    p = True
    for i in range(len(string)):
        if string[i] in '<>' and p==True:
            part+=string[i]
        
        elif string[i] in '<>' and p==False:
            textsep.append(part)
            part=''
            part+=string[i]  
            p=True
        
        else:
            if p==True:
                textsep.append(part)
                part=''
                part+=string[i]  
                p=False
                
            if p==False:
                part+=string[i]
    textsep.append(part)
    for i in range(len(textsep)):
        if ('>' in textsep[i]) or ('<' in textsep[i]):
            textsep[i]=simarrowhelper(textsep[i])
    finalarrow=''
    for i in textsep:
        finalarrow+=i
    return finalarrow



