# Used variables
x = 10  # Used in calculations
y = 20  # Used in print statement

# Unused variables
unused_var_1 = 100  # Declared but never used
unused_var_2 = "This is not used"  # Declared but never used
unused_var_3 = [1, 2, 3]  # Declared but never used

def example_function():
    # Used variable inside function
    z = x + y
    print(f"The sum of x and y is: {z}")

    # Unused variable inside function
    function_unused_var = "I am not used"  # Declared but never used

# Call the function
example_function()
