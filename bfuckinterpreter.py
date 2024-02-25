#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 09:00:42 2023

@author: cenzodecarvalho
"""
import math
import sys

def interpret(code,ip=0, mem=None, steps=None):
    memory = [0]*30000 if mem==None else mem
    mempointer=0 if ip==0 else ip
    maxsteps=steps if steps!=None else math.inf
    position=0
    stepcount=0
    bracketmatches = brackmatch(code)
    
    
    while position < len(code) and stepcount<maxsteps:
        
        command = code[position]
        
        if command == '+':
            memory[mempointer] = (memory[mempointer] + 1) % 256
            
        elif command == '-':
            memory[mempointer] = (memory[mempointer] - 1) % 256
        
        elif command == '>':
            mempointer = (mempointer + 1)  %30000
        
        elif command == '<':
            mempointer = (mempointer - 1)  %30000
            
        elif command == '.':
            print(chr(memory[mempointer]), end='')
        
        elif command == ',':
            inp= sys.stdin.read(1)
            memory[mempointer] = ord(inp)
        
        elif command == '[':
            if memory[mempointer] == 0:
                position= bracketmatches[position]
                            
        elif command == ']':
            position=bracketmatches[position]-1
            
                
        stepcount+=1
        position+=1

 

   
def brackmatch(string):
    stack=[]
    brackpos=[None]* len(string)
    
    for position in range(len(string)):
        
        if string[position]=='[':
            stack.append(position)
            
        if string[position]==']':
            brac1 = stack.pop()
            brackpos[brac1]=position
            brackpos[position]=brac1
        
    return brackpos
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    