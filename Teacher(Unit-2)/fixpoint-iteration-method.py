import math

def fixed_point_iteration(g, x0, tol=1e-6, max_iter=100):

    print(f"{'It. no.':<10}{'   x_n':<15}{'  g(x_n)':<15}{'Absolute Error':<15}")
    print("-" * 55)
   
    for i in range(1, max_iter + 1):
        x1 = g(x0)
        error = abs(x1 - x0)
       
        print(f"{i:<10}{x0:<15.6f}{x1:<15.6f}{error:<15.6f}")
       
        if error < tol:
            print(f"\n The required root is: {x1:.6f} after {i} iterations.")
            return x1
           
        x0 = x1
       
    print("\n Failed to converge within the maximum number of iterations.")
    return None

# --- Run the program for the given example ---
# Solve f(x) = x^3 + x - 1 = 0
# Rewriting it as x = g(x) => x = 1 / (x^2 + 1)
"""
def g(x):
    return 1 / (x**2 + 1)

# Run the algorithm with an initial guess of 0.5
initial_guess = 0.5
tolerance = 0.0001
maximum_iterations = 20
fixed_point_iteration(g, initial_guess, tolerance, maximum_iterations)
"""

fixed_point_iteration(lambda x: 1 / (x**2 + 1), 0.5, 0.0001, 30)