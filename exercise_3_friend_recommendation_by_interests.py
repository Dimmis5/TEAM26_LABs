# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 19:07:57 2026

@author: turet

"""
import math
data = [
    [8, 0, 3, 10, 5, 2, 9, 1, 7, 4, 6],
    [1, 9, 4, 0, 8, 10, 2, 5, 3, 6, 7],
    [5, 2, 10, 7, 1, 3, 0, 8, 6, 9, 4],
    [0, 8, 1, 5, 9, 4, 7, 10, 2, 3, 5],
    [7, 3, 6, 2, 0, 8, 10, 4, 9, 1, 5],
    [10, 5, 0, 9, 3, 7, 1, 6, 4, 8, 2],
    [4, 7, 9, 1, 6, 0, 3, 2, 10, 5, 8],
    [2, 10, 5, 8, 4, 9, 6, 3, 0, 7, 1],
    [6, 1, 2, 4, 10, 5, 8, 9, 3, 0, 7],
    [9, 4, 7, 3, 2, 6, 5, 0, 8, 10, 1],
    [3, 6, 8, 0, 7, 1, 4, 5, 1, 2, 9]
]
    

"HastableInterest<- a hash table that store the index and the name of interests"
HastableInterest = {
    "Musique": 0,
    "Sports": 1,
    "Technologie": 2,
    "Mode": 3,
    "Voyages": 4,
    "Cuisine": 5,
    "Football": 6,
    "Basketball": 7,
    "Rugby": 8,
    "Cinéma": 9,
    "Art": 10
}
"Hastable<- a hash table that store the user position in the matrix and the name"
Hashtable={"Alice": 1, "Bob": 2, "Charlie": 3}

def cosine (ua,ub):
        sum=0
        Nua=0
        Nub=0
        for i in range (0,len(ua)):
            "avoid unnecessary calculus"
            print(ua[i],ub[i])
            if(ua[i]!=0 and ub[i]!=0):
                sum+=ua[i]*ub[i]
                print('je susi passe')
                Nua=Nua+ua[i]**2
                Nub=Nub+ub[i]**2
                print (sum,Nua,Nub)
        Nua=math.sqrt(Nua)
        Nub=math.sqrt(Nub)
        if (sum==0):
            print('sum est 0')
            return 0
        if (Nua*Nub!=0):
            return sum/(Nua*Nub)

user_empty = [0, 0, 0, 0, 0, 0]
user_active = [10, 5, 8, 0, 0, 0]
"test case for the user with 0 interests"
print(cosine(user_active, user_empty))   
    
def topsimilar(user,k):

     dic={}
     "calculating for each user in the list"
     for name,value in Hashtable.items():
         "if notInFriendlist(user,Hashtable[i]):"
         "We suppose that we have a fucntion notInFriendlist or we can usee the one in exercice 2"
         print(name)
         dic[name]=cosine(data[Hashtable[user]],data[Hashtable[name]]) 
         
     dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
     
     "selecting the top k most similar user" 
     res=[] 
     " if k is longer than the size of dictionary"
     min_limit=min(k,len(dic))
     count=0
     print(dic)
     for key, value in dic.items():
        print(key)
        if key != user:
      
            res.append(key)
            count += 1
            if count == min_limit:
              
                return res
  
     return res
print (topsimilar("Alice", 1))



def recommend (user,k):
        l=topsimilar(user,k)
        S=set()
        for el in l :
            for k in range(len(data[Hashtable[el]])): 
                
                           if (data[Hashtable[user]][k]==0 and data[Hashtable[el]][k]!=0):
                               S.add(list(HastableInterest.keys())[k]) 
        print(S)
        return S


print(recommend("Alice", 1))    
