def polynomial_eval(coeffs, x):
    result = coeffs[-1]
    
    for i in range(len(coeffs) - 2, -1, -1):
        result = result * x + coeffs[i]

    return result

# Test cases
print(polynomial_eval([3, -2, 0, 5], 2))    # 39
print(polynomial_eval([1, 0, -2], 3))       # -17
print(polynomial_eval([2, 3], 4))           # 14