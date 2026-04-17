# LAB_07 - More Recursion

## Team 26
**Team Members:**
- Kamilla VAISOVA - Exercise 2
- Diméo ZHANG - Exercise 1
- Yannick ZHANG - Exercise 3
---
## Exercise Descriptions

### Exercise 1: Divide & Conquer – Spatial Splitting
Recursive Quadtree decomposition that divides a 2D space into four equal quadrants until a minimum size is reached, effectively partitioning the area into a hierarchical grid. By integrating a point-counting function, the algorithm calculates the density of each region—the ratio of points to area—and recursively filters the space to return only those segments exceeding a specific threshold. This Divide and Conquer approach is highly efficient for identifying data clusters because it allows the program to "prune" or ignore vast empty areas while focusing computational resources on densely populated "hotspots," significantly optimizing the search process compared to a standard linear scan.

### Exercise 2: Fractals
In this exercise, we implemented three fractal-related programs using recursion and numerical analysis. The first was a Sierpinski triangle, which works by splitting a triangle into three smaller copies of itself, repeating until a set depth is reached. The second was a fractal tree, where each branch recursively grows two smaller branches at ±30 degrees, mimicking the structure of a real tree. The third was a box-counting algorithm to estimate the fractal dimension of an image: by overlaying grids of decreasing box sizes and counting how many boxes intersect the fractal, then plotting the results on a log-log scale, the slope of the resulting line gives the fractal dimension. For the Sierpinski triangle, the expected dimension is approximately 1.585, which reflects the fact that it is more complex than a line but does not fill a 2D surface. Overall, the exercises illustrated how simple recursive rules can produce complex geometric patterns, and how mathematical tools like logarithms can quantify that complexity.

### Exercise 3:  


## Complexity Analysis Summary

Exercise, Time complexity, Space complexity
- ex 1: spatial splitting, $O(N log(S/min_size))$, $O(log(S/min_size))
- ex 2: sierpinski, O(3^depth), O(depth) ; tree, O(2^depth), O(depth) ; fractal dimension, O(B × N²/s²), O(N²)








