#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 20:05:36 2023

@author: cenzodecarvalho
"""


import sys
def bfinteropt(code, mem=None):

    memory = [0]*30000 if mem==None else mem
    mempointer=0
    position=0
    bracketmatches = brackmatch(code)
    
    
    while position < len(code):
        
        command = code[position]
        if command in '1234567890-)':
            position+=1
            continue
        
        elif command == '+':
            a=number(position,code)
            memory[mempointer] = (memory[mempointer] + a[0]) &255
            position+=a[1]
            
        elif command == '>':
            a=number(position,code)
            mempointer = (mempointer + a[0])  %30000
            position+=a[1]
        
        elif command == '(':
            (offset,increment,move) = offinc(position, code)
            memory[(mempointer+offset)%30000] = (memory[(mempointer+offset)%30000] + increment) &255
            position+=move+2
        
        elif command == ':':
            (offset,increment,move) = offinc(position, code)
            memory[(mempointer+offset)%30000] = (memory[(mempointer+offset)%30000] + increment*memory[mempointer]) &255
            position+=move+2
        
        elif command == ';':
            (offset,increment,move) = offinc(position, code)
            memory[(mempointer+offset)%30000] = (memory[(mempointer+offset)%30000] + increment*(256-memory[mempointer])) &255
            position+=move+2
        
        
        elif command =='|':
            a=number(position, code)    
            if a[0]==1:
                mempointer = ((memory[mempointer:]+memory[:mempointer]).index(0) + mempointer)%30000
            else:
                mempointer = ((memory[mempointer:]+memory[:mempointer]).rindex(0) + mempointer)%30000
        
        elif command == '=':
            a=number(position, code)   
            memory[mempointer]=a[0]&255
            position+=1
            
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
            
        position+=1




def number(pos,string):
    negative=False
    num=''
    for i in string[pos+1:]:
        if i=='-':
            negative=True
        elif i in ['0','1','2','3','4','5','6','7','8','9']:
            num+=i
        else:
            if negative:
                return (int(num)*(-1),len(num)+1)
            else:
                return (int(num),len(num))
    if negative:
        return (int(num)*(-1),len(num)+1)
    else:
        return (int(num),len(num))
    
def offinc(pos,string):
    a=number(pos,string)
    b=number(pos+a[1]+1,string)
    off=a[0]
    inc=b[0]
    return (off,inc,a[1]+b[1])


