def forward_difference_table(y_values):
    """
    Constructs the forward difference table for the values of y = tan x as
    (x,y) = (0.10, 0.1003), (0.15, 0.1511), (0.20, 0.2027), (0.25, 0.2553), (0.30. 0.3093)
    and hence find the value tan(0.12).

    """
    n = len(y_values)
    # Create a 2D list filled with zeros
    table = [[0.0] * n for _ in range(n)]
   
    # The first column is always the original y-values
    for i in range(n):
        table[i][0] = y_values[i]
       
    # Calculate the remaining columns of the table
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = table[i + 1][j - 1] - table[i][j - 1]
           
    return table

def newton_forward_interpolation(x_values, y_values, x):
    """
    Performs Newton's Forward Interpolation to find the value of y at a given x.
    """
    n = len(x_values)
   
    # Calculate step size (h) and the fractional spacing parameter (u)
    h = x_values[1] - x_values[0]
    u = (x - x_values[0]) / h
   
    # Generate the forward difference table
    table = forward_difference_table(y_values)
   
    # Initialize the interpolation result with the first y-value
    result = table[0][0]
   
    # Term runner variables
    u_term = 1.0
    factorial = 1.0
   
    # Calculate each term of the formula iteratively
    for i in range(1, n):
        u_term *= (u - (i - 1))
        factorial *= i
        result += (u_term * table[0][i]) / factorial
       
    return result, table

# --- Example Usage ---
if __name__ == "__main__":
    # Given data points (x must be equally spaced)
    x_data = [0.10, 0.15, 0.20, 0.25, 0.30]
    y_data = [0.1003, 0.1511, 0.2027, 0.2553, 0.3093]
   
    # Target value to interpolate
    target_x = 0.12
   
    # Run the interpolation
    predicted_y, diff_table = newton_forward_interpolation(x_data, y_data, target_x)

    # Display the forward difference table nicely
    print("\n--- Forward Difference Table ---")
    for i in range(len(x_data)):
        print(f"{x_data[i]:.2f}\t", end="")
        for j in range(len(x_data) - i):
            print(f"{diff_table[i][j]:.4f}\t", end="")
        print()

    print("\n--- Interpolation Result ---")
    print(f"The estimated value of y at x = {target_x} is: {predicted_y:.5f}")