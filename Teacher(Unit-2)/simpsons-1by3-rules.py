# Simpson's 1/3 Rule for numerical integration
from symtable import Function


def f(x):
    return x**3  # Example function: f(x) = x^3

def simpson_one_third(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's 1/3 rule")
    
    h = (b - a) / n  # step size
    s = f(a) + f(b)  # first and last term
    
    for i in range(1, n):
        if i % 2 == 0:
            s += 2 * f(a + i * h)  # even index term
        else:
            s += 4 * f(a + i * h)  # odd index term
            
    result = (h / 3) * s
    return result

# Input values
a = float(input("Enter the lower limit a: "))
b = float(input("Enter the upper limit b: "))
n = int(input("Enter the number of subintervals (even): "))

# Compute and display result
result = simpson_one_third(f, a, b, n)
print(f"\nApproximate value of the integral = {result:.6f}")
