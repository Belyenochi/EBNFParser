#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 18:47:20 2017

@author: misakawa
"""
# ===========
import re

L_Number = '\d+|\d*\.\d+'  

L_Name   = '[a-zA-Z_][a-zA-Z0-9]*'

L_String = '[a-z]{0,1}"[\w|\W]*"'

L_Bracket= '\{|\}|\(|\)|\[|\]'

L_END    = ';'

L_NEWLINE= '\n'

L_Comment = '#[\w|\W]*?\n'

L_Op = '|'.join(['//', 
               '/' ,
               '\|',
               '\|\|',
               '>>','<<',
               '>=','<=',
               '<-',
               '>' ,'<', 
               '=>','->',
               '\?', 
               '--',
               '\+\+', 
               '\*\*',
               '\+','-','\*','==','=','~',
               '@',
               '\$',
               '%',
               '\^',
               '&',
               '\!',
               '\:\:',
               '\:',
               ])

def reMatch(x, make = lambda x:x, escape = False):
    
    re_ = re.compile( re.escape(x) if escape else x)
    def _1(ys):
        if not ys: return None
        r = re_.match(ys[0])
        if not r : return None
        a, b = r.span()
        if a!=0 : raise Exception('a is not 0')
        if b is not len(ys[0]):
            return None
        return 1, ys[0]
    return _1

class Liter:
    def __init__(self, i):
        self.f = reMatch(i)
    def match(self, objs, partial = True):
        r = self.f(objs)
        if r:
            if partial or len(objs) == 1:
                return r
            return None
class ELiter:
    def __init__(self, i):
        self.f = reMatch(i, escape = True)
    def match(self, objs, partial = True):
        r = self.f(objs)
        if r:
            if partial or len(objs) == 1:
                return r
            return None
    

Name   = Liter(L_Name)
String = Liter(L_String)
Number = Liter(L_Number)
Bracket= Liter(L_Bracket)
NEWLINE= Liter(L_NEWLINE)
END    = Liter(L_END)
Comment= Liter(L_Comment)
Op     = Liter(L_Op)

class recur:pass
def redef(self, *args, **kwargs):
    self.__init__(*args, **kwargs)
    return self
    
class mode(list):
    def setName(self, name):
        self.name = name
        return self



class ast:
    def __init__(self, *ebnf, name = None):
        
        self.name     = name
        self.parent   = None
        self.possibles: 'list[mode[ast, re]]' = \
                    [ mode([self if e is recur else e for e in es]) for es in ebnf ] 
        
    
    def setP(self, parent): self.parent = parent; parent.append(self); return self
    
    def match(self, objs, partial = True):
        res   = mode().setName(self.name)
        count = 0
        for possible in self.possibles:
            for thing in possible:
                r = thing.match(objs[count:], partial = partial)
                if not r:
                    # nexr possible
                    res.clear()
                    count = 0
                    break
                
                a, b = r
                count +=  a
                
                if b:
                    if isinstance(thing, Seq):
                        res.extend(b)
                    else:
                        res.append(b)
                        
            return count, res
                
                    
class Seq(ast):
    def __init__(self, *ebnf, name = None, atleast = 1):
        super(Seq, self).__init__(*ebnf, name = name)
        self.atleast = atleast
        
    def match(self, objs, partial = True):
        
        res = mode().setName(self.name)
        if not objs:
            if self.atleast is 0:
                return 0 , None
            return None
        count = 0
        # debug
        i = 0
        while True:
            
            # debug
            i+=1
            if i>50:raise
            # ===
            
            
            r = super(Seq, self).match(objs, partial = True)
            if not r:
                break
            
            # debug
            print(r, objs)
            # ===
            a , b = r
            res.extend(b)
            
            count += a
            
        if count < self.atleast:
            return  None
        
        return count, res
                
                    
                
            
    
                
            
    
    
    