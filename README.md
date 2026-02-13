
Dimeo ZHANG:Exercice 3 and 5 
Kamilla VAISOVA :Exercice 2 and 4
Yannick ZHANG:Exercice 1 and 6

Exercice 1
o reverse a number without converting it into a string, we have to isolate each digit by using modulo, then add it back mathematically. In this exercise, we observed that the time complexity depends mainly on the length (number of digits) of the integer.

Exercice6

To find the first unique character, we compared two methods.
In both cases, we use a dictionary to store the letter and its index (or nullify the value if it's a duplicate).
Method 1 (Standard Dictionary): We have to iterate through the string a second time to find the first unique index, because a standard dictionary loses the order.
Method 2 (Ordered Dictionary): This is the most effective way. Since the order is preserved, we only iterate through the dictionary (maximum 26 items) instead of the whole string
The time is constant for the ordered dictionary while for the standard dictionary it depends on the string's number of letter 
