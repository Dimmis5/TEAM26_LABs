def balanced_symbols(s):
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}
    openers = set(['(', '[', '{'])

    for char in s:
        if char in openers:
            stack.append(char)          
        elif char in matching:
            if len(stack) == 0:         
                return False
            if stack[-1] != matching[char]:  
                return False
            stack.pop()                 

    return len(stack) == 0  

# Test cases
print(balanced_symbols("([{}])"))   # True 
print(balanced_symbols("([)]"))     # False 
print(balanced_symbols(""))         # True
print(balanced_symbols("((())"))    # False
