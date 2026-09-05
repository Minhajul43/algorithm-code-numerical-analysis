# False Position Method
def false_position(f, a, b, tol, N0):
    # Step 1
    i = 1
    FA = f(a)
    FB = f(b)

    # Check initial interval
    if FA * FB > 0:
        print("\nError: f(a) and f(b) have the same sign.")
        print("Please choose another interval.")
        return None

    print("\n" + "=" * 65)
    print("              FALSE POSITION METHOD")
    print("=" * 65)
    print(f"{'Iteration':<12}{'a':<15}{'b':<15}{'p':<15}{'f(p)':<15}")
    print("-" * 65)

    # Step 2
    while i <= N0:

        # Step 3
        p = (a * FB - b * FA) / (FB - FA)
        FP = f(p)

        # Display iteration
        print(f"{i:<12}{a:<15.8f}{b:<15.8f}"
              f"{p:<15.8f}{FP:<15.8f}")

        # Step 4
        if FP == 0 or (b - a) / 2 < tol:
            print("-" * 65)
            print("Procedure completed successfully!")
            print(f"Approximate root = {p:.10f}")
            print(f"Number of iterations = {i}")
            print("=" * 65)
            return p

        # Step 5
        i = i + 1

        # Step 6
        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p
            FB = FP

    # Step 7
    print("-" * 65)
    print(f"Method failed after {N0} iterations.")
    print("=" * 65)

    return None


# ==============================
#          MAIN PROGRAM
# ==============================

print("=" * 65)
print("             NUMERICAL ANALYSIS")
print("              FALSE POSITION METHOD")
print("=" * 65)

# Get function from user
function = input("\nEnter the function f(x): ")

# Create the function
def f(x):
    return eval(function)

# Get input values
a = float(input("Enter the lower limit (a): "))
b = float(input("Enter the upper limit (b): "))
tol = float(input("Enter the tolerance (TOL): "))
N0 = int(input("Enter maximum iterations (N0): "))

# Call False Position Method
false_position(f, a, b, tol, N0)