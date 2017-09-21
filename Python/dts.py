#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:48:52 2017

@author: misakawa
dev-test-script
"""

from Misakawa.Bootstrap.Parser import *
from Misakawa.ObjectRegex.Node import MetaInfo, Ast
from Misakawa.ErrorFamily import handle_error
from Misakawa.Bootstrap.Ast import ast_for_stmts
from Misakawa.Bootstrap.Compile import compile as bootstrap_comp

_compose_eq = 0
_literal_eq = 1
_newline    = 2
def go():
    with open('../bootstrap.ebnf') as f:
        lex = f.read()
    bootstrap_comp(lex, '')
    tokens = token.findall(lex)
    parser = handle_error(Stmt.match)
    res = parser(tokens, partial=False)
    print(res)
    return res
with open('../bootstrap.ebnf') as f:
        lex = f.read()
s= bootstrap_comp(lex, '')
with open('bs.py','w') as f:f.write(s)
def grpFunc(stmt : Ast):
   return  _newline if stmt.name == 'NEWLINE' else  \
           _literal_eq if stmt[2].name == 'Str' else \
           _compose_eq
           
           
#Expr = AstParser([Ref('Or'),
#                  SeqParser([LiteralParser.Eliteral('|', name = '\'|\''),Ref('Or')], 
#                             atleast = 0, atmost = None)], name = 'Expr')
#Or = AstParser([SeqParser([Ref('AtomExpr')], 
#                           atleast = 1, atmost = None)], name = 'Or')
