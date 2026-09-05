# fixed point iteration method
def fixed_point_iteration(g, x0, tol, N0):
    # Step 1
    i = 1
    x = x0

    print("\n" + "=" * 65)
    print("          FIXED POINT ITERATION METHOD")
    print("=" * 65)
    print(f"{'Iteration':<12}{'x':<15}{'g(x)':<15}{'Error':<15}")
    print("-" * 65)

    # Step 2
    while i <= N0:

        # Step 3
        x_new = g(x)
        error = abs(x_new - x)

        # Display iteration
        print(f"{i:<12}{x:<15.8f}{x_new:<15.8f}{error:<15.8f}")

        # Step 4
        if error < tol:
            print("-" * 65)
            print("Procedure completed successfully!")
            print(f"Approximate root = {x_new:.10f}")
            print(f"Number of iterations = {i}")
            print("=" * 65)
            return x_new

        # Step 5
        x = x_new
        i += 1

    # Step 6
    print("-" * 65)
    print(f"Method failed after {N0} iterations.")
    print("=" * 65)

    return None

# take input from user
g = input("Enter the function g(x): ")
x0 = float(input("Enter the initial guess x0: "))
tol = float(input("Enter the tolerance: "))
N0 = int(input("Enter the maximum number of iterations: "))

# Create the function g(x)
def g(x):
    return eval(g)

# Call the fixed point iteration method
fixed_point_iteration(g, x0, tol, N0)
