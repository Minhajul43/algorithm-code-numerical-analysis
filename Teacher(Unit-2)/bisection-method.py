def bisection_method(f, a, b, tol=1e-6, max_iter=100):

    if f(a) * f(b) >= 0:
        print("The root does not belong in this interval. Enter the correct interval.")
        print(f"f(a) = {f(a)} and f(b) = {f(b)} must have opposite signs.")
        return None

    print(f"\n{'It. no.':<6}{'   a':<12}{'   b':<12}{'Root(c)':<15}{' f(c)':<12}")
    print("-" * 55)

    for i in range(1, max_iter + 1):
        c = (a + b) / 2.0
        fc = f(c)
        print(f"{i:<6}{a:<12.6f}{b:<12.6f}{c:<15.6f}{fc:<12.6f}")
        if abs(fc) < tol or (b - a) / 2.0 < tol:
            return c
        if f(a) * fc < 0:
            b = c  
        else:
            a = c  

    print("Maximum iterations reached before full convergence.")
    return c


# --- Run the code for given example ---
if __name__ == "__main__":

    root = bisection_method(lambda x: x**3 - 3*x - 5, 2.0, 3.0, 0.0001)

    if root is not None:
        print("-" * 55)
        print(f"The approximate root is: {root:.6f}")