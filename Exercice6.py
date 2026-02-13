# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 18:47:47 2026

@author: turet
"""

def findF(word):
    dic={}
    l=len(word)
    print(l)
    if l==0:
        print('rien')
        return -1
    if l==1:
       return 0
    for i in range (0,l):
        if word[i] in dic :
            dic[word[i]]='null'
        else :
            dic[word[i]]=i
    print(dic)
    for i in range (0,l):
        if dic[word[i]]!='null':
            print (i)
            return i
   
    
    print(-1)
    return -1

def findFordered(word):
    dic={}
    l=len(word)
    print(l)
    if l==0:
       
        return -1
    if l==1:
       return 0
    for i in range (0,l):
        if word[i] in dic :
            dic[word[i]]='null'
        else :
            dic[word[i]]=i
    print(dic)
    for key,value in dic.items():
            if value!='null' :
                print (value)
                return value
   
    return -1


findF('tortue genial')
findF('')
findF('aabb')
findF('a')

findFordered('tortue genial')
findFordered('')
findFordered('a')
findFordered('aabb')
