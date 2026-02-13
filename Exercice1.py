# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 20:02:55 2026

@author: turet
"""

def Reverse (nb):
    if nb<0:
        print ('nop')
        return -1
    alone=nb
    result=0
    while nb!=0 :
        alone=nb%10
        result=result*10+alone
        nb-=alone
        nb=nb//10
    print (result)
    return result
Reverse(123)
Reverse(-5)
Reverse(5)