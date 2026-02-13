from typing import List

def rotate(num: List[int], k: int) :
    def reverse(start: int,end: int):
        while start < end:
            num[start], num[end] = num[end], num[start]
            start += 1
            end -= 1

    n = len(num)
    k = k % n

    reverse(0, n-1)
    reverse(0, k-1)
    reverse(k, n-1)

    print(num)


test_cases = [
    #([], 3),  Does not work                  
    ([1], 0),                 
    ([1], 1),                 
    ([1,2,3], 0),             
    ([1,2,3], 3),             
    ([1,2,3], 5),             
    ([1,1,1,1], 2),           

    ([1,2,3,4,5], 2),        
    ([1,2,3,4,5,6], 3),       
    ([10,20,30,40], 1),       
]

for arr, k in test_cases:
    print(f"Original: {arr}, k={k}")
    rotate(arr.copy(), k)  
    print("-" * 30)
