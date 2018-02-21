
from Misakawa.ObjectRegex.Node import Ref, AstParser, SeqParser, LiteralParser, MetaInfo
from etoken import token 
import re
namespace     = globals()
recurSearcher = set()
Test = AstParser([Ref('Lambdef')],[Ref('OrTest'),SeqParser([LiteralParser('if(?!\S)', name = '\'if(?!\S)\''),Ref('OrTest'),LiteralParser('else(?!\S)', name = '\'else(?!\S)\''),Ref('Test')], atmost = 1)], name = 'Test')
Lambdef = AstParser([LiteralParser('lambda(?!\S)', name = '\'lambda(?!\S)\''),Ref('NameList'),LiteralParser.Eliteral(':', name = '\':\''),Ref('Test')], name = 'Lambdef')
OrTest = AstParser([Ref('AndTest'),SeqParser([Ref('Or'),Ref('AndTest')])], name = 'OrTest')
AndTest = AstParser([Ref('NotTest'),SeqParser([Ref('And'),Ref('NotTest')])], name = 'AndTest')
NotTest = AstParser([Ref('Arith')],[Ref('Not'),Ref('NotTest')], name = 'NotTest')
Arith = AstParser([Ref('Term'),SeqParser([SeqParser([LiteralParser.Eliteral('+', name = '\'+\'')],[LiteralParser.Eliteral('-', name = '\'-\'')], atleast = 1, atmost = 1),Ref('Term')])], name = 'Arith')
Term = AstParser([Ref('Factor'),SeqParser([SeqParser([LiteralParser.Eliteral('*', name = '\'*\'')],[LiteralParser.Eliteral('/', name = '\'/\'')],[LiteralParser.Eliteral('%', name = '\'%\'')], atleast = 1, atmost = 1),Ref('Factor')])], name = 'Term')
Factor = AstParser([Ref('AtomExpr')],[SeqParser([LiteralParser.Eliteral('+', name = '\'+\'')],[LiteralParser.Eliteral('-', name = '\'-\'')], atleast = 1, atmost = 1),Ref('Factor')], name = 'Factor')
Not = LiteralParser('not(?!\S)', name = 'Not')
Or = LiteralParser('or(?!\S)', name = 'Or')
And = LiteralParser('and(?!\S)', name = 'And')
Atom = AstParser([Ref('Number')],[Ref('Const')],[Ref('Name')],[LiteralParser.Eliteral('(', name = '\'(\''),SeqParser([Ref('ListComp')],[Ref('TestList')], atleast = 1, atmost = 1),LiteralParser.Eliteral(')', name = '\')\'')],[LiteralParser.Eliteral('[', name = '\'[\''),SeqParser([Ref('ListComp')],[Ref('TestList')], atleast = 1, atmost = 1),LiteralParser.Eliteral(']', name = '\']\'')], name = 'Atom')
AtomExpr = AstParser([Ref('Atom'),SeqParser([SeqParser([LiteralParser.Eliteral('[', name = '\'[\''),Ref('TestList'),LiteralParser.Eliteral(']', name = '\']\'')],[LiteralParser.Eliteral('(', name = '\'(\''),Ref('TestList'),LiteralParser.Eliteral(')', name = '\')\'')], atleast = 1, atmost = 1)])], name = 'AtomExpr')
TestList = AstParser([Ref('Test'),SeqParser([LiteralParser.Eliteral(',', name = '\',\''),Ref('TestList')], atmost = 1)], name = 'TestList')
NameList = AstParser([Ref('Name'),SeqParser([LiteralParser.Eliteral(',', name = '\',\''),Ref('Name')])], name = 'NameList')
TestList = AstParser([Ref('Test'),SeqParser([LiteralParser.Eliteral(',', name = '\',\''),Ref('Test')])], name = 'TestList')
ListComp = AstParser([Ref('Test'),SeqParser([LiteralParser('for(?!\S)', name = '\'for(?!\S)\''),Ref('NameList'),LiteralParser('in(?!\S)', name = '\'in(?!\S)\''),Ref('Test')], atmost = 1)], name = 'ListComp')
Number = LiteralParser('\d+|\d*\.\d+', name = 'Number')
Const = LiteralParser('True(?!\S)|False(?!\S)|None(?!\S)', name = 'Const')
Name = LiteralParser('[a-zA-Z_][a-zA-Z0-9]*', name = 'Name')
NEWLINE = LiteralParser.Eliteral('\n', name = 'NEWLINE')
Test.compile(namespace, recurSearcher)
Lambdef.compile(namespace, recurSearcher)
OrTest.compile(namespace, recurSearcher)
AndTest.compile(namespace, recurSearcher)
NotTest.compile(namespace, recurSearcher)
Arith.compile(namespace, recurSearcher)
Term.compile(namespace, recurSearcher)
Factor.compile(namespace, recurSearcher)
Atom.compile(namespace, recurSearcher)
AtomExpr.compile(namespace, recurSearcher)
TestList.compile(namespace, recurSearcher)
NameList.compile(namespace, recurSearcher)
TestList.compile(namespace, recurSearcher)
ListComp.compile(namespace, recurSearcher)
