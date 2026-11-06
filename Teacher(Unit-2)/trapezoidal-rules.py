# Trapezoidal Rule for numerical integration
def f(x):
    return x**2  # Example function: f(x) = x^2

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))  # first and last term
    for i in range(1, n):
        s += f(a + i*h)
    return h * s

# Input values
a = float(input("Enter the lower limit a: "))
b = float(input("Enter the upper limit b: "))
n = int(input("Enter the number of subintervals n: "))

# Compute and display result
result = trapezoidal_rule(a, b, n)
print(f"\nApproximate value of the integral = {result:.6f}")