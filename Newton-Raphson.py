import matplotlib.pyplot as plt
import numpy as np

# Ask the user to input the function and its derivative as strings
f_input = input("Enter the function f(x): ")     
df_input = input("Enter the derivative f'(x): ") 
x0 = float(input("Enter initial guess: "))

# Evaluate the user-defined function dynamically (use with caution)
def f(x):
    return eval(f_input)

def df(x):
    return eval(df_input)

def newton_raphson(x0, tol=1e-6, max_iter=100):
    # Newton-Raphson root-finding algorithm
    # Arguments:
    #   x0       : initial guess
    #   tol      : tolerance to determine convergence (default = 1e-6)
    #   max_iter : maximum number of iterations allowed (default = 100)
    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)

        if dfx == 0:
            print("Derivative is zero. No solution.")
            return None

        x1 = x0 - fx / dfx

        # Print the iteration progress
        print(f"Iteration {i+1}: x = {x1}, f(x) = {f(x1)}")

        # Check for convergence
        if abs(f(x1)) < tol:
            print("Converged.")
            return x1

        x0 = x1

    print("Max iterations reached.")
    return x0

# Run the method and print the root
root = newton_raphson(x0)
print(f"\nRoot found: {root}")

# Generate x values around the initial guess for plotting
x_vals = np.linspace(x0 - 5, x0 + 5, 300)
y_vals = [f(x) for x in x_vals]

plt.plot(x_vals, y_vals, label=f'f(x) = {f_input}')
plt.axhline(0, color='black', linestyle='--')  # X-axis
plt.axvline(root, color='red', linestyle=':', label=f'Root ≈ {root:.5f}')
plt.title("Newton-Raphson Visualization")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
