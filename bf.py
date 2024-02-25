#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 18:17:15 2023

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

    return(mempointer,memory)

   
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
                      
def simplusfyhelper(plusstring):
    if '+' not in plusstring or '-' not in plusstring:
        if '+' in plusstring:
            return len(plusstring)
        else:
            return '-'+str(len(plusstring))
    counter=0
    for i in plusstring:
        if i == '+':
            counter+=1
        elif i == '-':
            counter-=1
    if counter < 0:
        return '-'+str(abs(counter))
    return counter

def contraction_inc_dec(string):
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
                
            else :
                part+=string[i]
                
    textsep.append(part)
    for i in range(len(textsep)):
        if ('+' in textsep[i]) or ('-' in textsep[i]):
            textsep[i]=f'+{simplusfyhelper(textsep[i])}'
    finalplus=''
    for i in textsep:
        finalplus+=i
    return finalplus

def simarrowhelper(arrowstring):
    if '>' not in arrowstring or '<' not in arrowstring:
        if '>' in arrowstring:
            return len(arrowstring)
        else:
            return '-'+str(len(arrowstring))
        
    counter=0
    for i in arrowstring:
        if i == '>':
            counter+=1
        elif i == '<':
            counter-=1
    if counter < 0:
        return '-'+str(abs(counter))
    return counter

def contraction_data_pointer(string):
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
                
            else:
                part+=string[i]
    textsep.append(part)
    for i in range(len(textsep)):
        if ('>' in textsep[i]) or ('<' in textsep[i]):
            textsep[i]=f'>{simarrowhelper(textsep[i])}'
    finalarrow=''
    for i in textsep:
        finalarrow+=i
    return finalarrow

     
def replace(string):
    '''ex: replace >1+2>-2+-2>1 by (1)+2(-1)+-2
    >+>>--< by (1)+1(3)+-2>2 '''
    side=0
    new=''
    i=0
    while i < len(string):
        
        if string[i]=='>':
            a=number(i,string)
            side= side + a[0]
            i+=a[1]
            
        elif string[i]=='+':
            a=number(i,string)
            new+=f'({side}/{a[0]})'
            i+=a[1]
            
        else:
            new+=string[i]
            
        i+=1
    if side ==0:        
        return new  
    else:
        return new+f'>{side}'
 
def bsplit(string):
    ''' splits a string between loop and non loop sections'''
    sp=[] 
    section=''
    for i in range(len(string)):
        if string[i] in'[].,|=':
            sp.append(section)
            sp.append(string[i])
            section=''
        
        else:
            section= str(section) +str(string[i])
            
    sp.append(section)
    return sp

def postpone_moves(string):
    new=''
    for i in bsplit(string):
        new+=replace(i)
    return new


def inc_dec_fixed_offset(string):
     return postpone_moves(string)


def scan(string):
    a=string
    if '[>1]' in a:
        a=a.replace('[>1]','|1')
    if '[>-1]' in a:
        a=a.replace('[>-1]','|-1')
    return a
             
def cancellation(string):

    for i in range(len(string)-6):
        if string[i:i+7] =='[(0/1)]':
            counter=0
            value=(0,0,-3)
            if string[i+7:i+9]=='(0':
                value=offinc(i+7,string)
                counter=value[1]
            string=string.replace(string[i:i+7+value[2]+3],f'={counter}=',1)
                
        elif string[i:i+8] =='[(0/-1)]':
              counter=0
              value=(0,0,-3)
              if string[i+8:i+10]=='(0':
                  value=offinc(i+8,string)
                  counter=value[1]
              string=string.replace(string[i:i+8+value[2]+3],f'={counter}',1)
              
  
            
            
    return string

def offinc(pos,string):
    a=number(pos,string)
    b=number(pos+a[1]+1,string)
    off=a[0]
    inc=b[0]
    return (off,inc,a[1]+b[1])

def copy_multiply_loop_simplification(string):
    b=bsplit(string)
    for i in range(len(b)-1):
        if b[i]=='[' and b[i+2]==']' and ('(0/-1)' in b[i+1]) and '>' not in b[i+1] and ',' not in b[i+1] and '.' not in b[i+1]:
            b[i]=''
            b[i+2]=''
            position=0
            newbi=''
            b[i+1]=b[i+1].replace('(0/-1)','')
            while position<len(b[i+1]):
                command=b[i+1][position]
                if command == '(':
                    (offset,increment,move) = offinc(position, b[i+1])
                    newbi= newbi + f':{offset}/{increment}:'
                    position+=move+2
                    
                position+=1
            b[i+1]=newbi+'=0'
        if b[i]=='[' and b[i+2]==']' and ('(0/1)' in b[i+1]) and '>' not in b[i+1] and ',' not in b[i+1] and '.' not in b[i+1]:
            b[i]=''
            b[i+2]=''
            position=0
            newbi=''
            b[i+1]=b[i+1].replace('(0/1)','')
            while position<len(b[i+1]):
                command=b[i+1][position]
                if command == '(':
                    (offset,increment,move) = offinc(position, b[i+1])
                    newbi= newbi + f';{offset}/{increment};'
                    position+=move+2
                    
                position+=1
            b[i+1]=newbi+'=0'
    a=''
    for j in b:
        a+=j
    return a
                    
            
            
    
def optimize(string):
    basic=contraction_data_pointer(contraction_inc_dec(string)) 
    return copy_multiply_loop_simplification(cancellation(scan(postpone_moves(basic))))
        
    

def optinterpret(code, mem=None):

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

    return(mempointer,memory)


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
    

    
    
    
    