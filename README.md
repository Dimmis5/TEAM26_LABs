# LAB_01 - Revision

## Team 26
**Team Members:**
- Kamilla VAISOVA - Exercises 2, 4
- Diméo ZHANG - Exercises 3, 5
- Yannick ZHANG - Exercises 1, 6

---
## Exercise Descriptions

### Exercise 1: Integer Mirror (Digit Reversal)
To reverse a number without converting it into a string, we have to isolate each digit by using modulo, then add it back mathematically. In this exercise, we observed that the time complexity depends mainly on the length (number of digits) of the integer.

### Exercise 2: Balanced Symbol Checker
To validate whether parentheses, brackets, and braces are properly balanced and nested, we use a stack data structure. We push opening symbols onto a stack. When encountering a closing symbol, 
we check if it matches the top of the stack. If the stack is empty, it means there is a pairless closing symbol, or if the closing does not match the opening, it returns False. The string is balanced if stack is empty at the end, meaning that with each closing symbol, an opening symbol was popped out of the stack.

### Exercise 3: Merge Overlapping Intervals
To merge overlapping intervals, we first sort all intervals by their start value. This allows us to process them in order from left to right. We then keep track of the current merged interval as we scan through the sorted list. For each new interval, we check if it overlaps with our current interval (by comparing if the new start is less than or equal to the current end). If they overlap, we extend the current interval's end to cover both. If they don't overlap, we save the current interval and start a new one. This approach ensures we only need one pass through the data after sorting.

### Exercise 4: Polynomial Evaluation
To evaluate a polynomial efficiently, we use Horner's method instead of the naive approach. The key insight is that we can rewrite the polynomial by factoring out x repeatedly, which eliminates the need to compute powers of x separately. We start with the coefficient of the highest degree term and work backwards through the array. At each step, we multiply our current result by x and add the next coefficient. This way, we only perform one multiplication per coefficient, resulting in exactly n multiplications for a degree-n polynomial. In contrast, the naive approach would compute each power of x separately (x², x³, etc.), requiring approximately n²/2 multiplications total. Horner's method reduces this from O(n²) to O(n), making it significantly more efficient for high-degree polynomials.

### Exercise 5: Array Rotation Optimization
To rotate an array to the right by k positions in-place, we use the reverse segments method. The key insight is that three reversals achieve the rotation without needing extra space. First, we reverse the entire array. Then we reverse the first k elements. Finally, we reverse the remaining elements. This method is optimal because it runs in O(n) time with O(1) extra space. We also handle the case where k is larger than the array length by using k mod n, since rotating by the array length brings us back to the original position.

### Exercise 6: First Unique Character Finder
To find the first unique character, we compared two methods. In both cases, we use a dictionary to store the letter and its index (or nullify the value if it's a duplicate). Method 1 (Standard Dictionary): We have to iterate through the string a second time to find the first unique index, because a standard dictionary loses the order. Method 2 (Ordered Dictionary): This is the most effective way. Since the order is preserved, we only iterate through the dictionary (maximum 26 items) instead of the whole string The time is constant for the ordered dictionary while for the standard dictionary it depends on the string's number of letter

---

## Complexity Analysis Summary

Exercise, Time complexity, Space complexity
Ex 1: Integer Mirror | O(log n) | O(1) | Loop runs once per digit; d digits = log₁₀(n)
---
Ex 2: Balanced Symbols | O(n) | O(n) | Single pass; stack stores up to n/2 elements
---
Ex 3: Merge Intervals | O(n log n) | O(n) | Dominated by sorting; linear merge afterward
---
Ex 4: Polynomial Eval | O(n) | O(1) | Horner's: n multiplications vs naive O(n²)
---
Ex 5: Array Rotation (optimal) | O(n) | O(1) | Reverse method; temp array is O(n) space
---
Ex 6: First Unique Char | O(n) | O(1) | Two passes; dictionary size bounded by alphabet

