# Simpson's 3/8 Rule for numerical integration
def f(x):
    return x**3  # Example function: f(x) = x^3

def simpson_three_eighth(f, a, b, n):
    if n % 3 != 0:
        raise ValueError("n must be a multiple of 3 for Simpson's 3/8 rule")
    h = (b - a) / n
    s = f(a) + f(b)  # first and last term
    for i in range(1, n):
        if i % 3 == 0:
            s += 2 * f(a + i*h)  # coefficient 2 (for i = 3,6,9,...)
        else:
            s += 3 * f(a + i*h)  # coefficient 3 (for other interior terms)
    result = (3*h/8) * s
    return result

# Input values
a = float(input("Enter the lower limit a: "))
b = float(input("Enter the upper limit b: "))
n = int(input("Enter the number of subintervals (multiple of 3): "))

# Compute and display result
result = simpson_three_eighth(f, a, b, n)
print(f"\nApproximate value of the integral = {result:.6f}")