def lagrange_interpolation(x_points, y_points, xp):
    """
    Certain corresponding values of x and ln (x) are the set of data points (2.0, 0.69315),
    (2.5, 0.91629), (3.0, 1.09861). Interpolates value of y = ln(x) at x = 2.3 using
    Lagrange's Interpolation Formula.
   
    Parameters:
    x_points (list or array): X-coordinates of the data points.
    y_points (list or array): Y-coordinates of the data points.
    xp (float): The target X-value to find the corresponding Y-value for.
   
    Returns:
    float: The interpolated Y-value at xp.
    """
    n = len(x_points)
    yp = 0.0  # Initialize the interpolated result

    # Loop through each data point to calculate its Lagrange basis polynomial
    for i in range(n):
        p = 1.0
        for j in range(n):
            if i != j:
                # Multiply terms: (xp - x_j) / (x_i - x_j)
                p *= (xp - x_points[j]) / (x_points[i] - x_points[j])
       
        # Add the term (L_i * y_i) to the final summation
        yp += p * y_points[i]
       
    return yp

# --- Example Usage ---
if __name__ == "__main__":
    # Define known data points (e.g., coordinates matching y = x^2)
    x = [2.0, 2.5, 3.0]
    y = [0.69315, 0.91629, 1.09861]
   
    # Target value to interpolate
    target_x = 2.3
   
    # Calculate the result
    interpolated_y = lagrange_interpolation(x, y, target_x)
   
    print(f"Given X data points: {x}")
    print(f"Given Y data points: {y}")
    print(f"The interpolated value at X = {target_x} is Y = {interpolated_y}")