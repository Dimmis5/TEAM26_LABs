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

print(rotate([1,2,3,4,5,6,7], 10))