#Bài tập 1
import numpy as np

# Problem 1: Hệ phương trình trong R^2
A1 = np.array([[1, -1], [2, 3]])
b1 = np.array([-2, 6])
x1 = np.linalg.solve(A1, b1)
print("Problem 1:", x1)

# Problem 2: Hệ phương trình trong R^3
A2 = np.array([[1, -1, 0], [2, 0, -1], [0, 1, 2]])
b2 = np.array([2, 3, 6])
x2 = np.linalg.solve(A2, b2)
print("Problem 2:", x2)

# Problem 3: Tìm hệ số đa thức bậc 2
A3 = np.array([[1, 1, 1], [4, 2, 1], [9, 3, 1]])
b3 = np.array([4, 3, 4])
x3 = np.linalg.solve(A3, b3)
print("Problem 3 (a, b, c):", x3)

# Problem 4: Phân tích phân thức để tích phân
A4 = np.array([[1, 0, 1], [1, -2, -3], [-2, 2, 0]])
b4 = np.array([1, -3, 0])
x4 = np.linalg.solve(A4, b4)
print("Problem 4 (a, b, c):", x4)

#Bài tập 2
from sympy import symbols, Eq, solve

# Problem 1
x, y = symbols('x y')
eq1 = Eq(x - y, -2)
eq2 = Eq(2*x + 3*y, 6)
sol1 = solve((eq1, eq2), (x, y))
print("Sympy - Problem 1:", sol1)

# Problem 2
x, y, z = symbols('x y z')
eq1 = Eq(x - y, 2)
eq2 = Eq(2*x - z, 3)
eq3 = Eq(x + y + 2*z, 6)
sol2 = solve((eq1, eq2, eq3), (x, y, z))
print("Sympy - Problem 2:", sol2)

# Problem 3
a, b, c = symbols('a b c')
eq1 = Eq(a + b + c, 4)
eq2 = Eq(4*a + 2*b + c, 3)
eq3 = Eq(9*a + 3*b + c, 4)
sol3 = solve((eq1, eq2, eq3), (a, b, c))
print("Sympy - Problem 3:", sol3)

# Problem 4
a, b, c = symbols('a b c')
eq1 = Eq(a + c, 1)
eq2 = Eq(a + b - 2*c, -3)
eq3 = Eq(-2*a + 2*b + c, 0)
sol4 = solve((eq1, eq2, eq3), (a, b, c))
print("Sympy - Problem 4:", sol4)

#Bài tập 3
import numpy as np

def fib_matrix(k):
    F = np.array([[1, 1],
                  [1, 0]], dtype=object)
    return np.linalg.matrix_power(F, k)

# Ví dụ kiểm tra:
k = 7
Fk = fib_matrix(k)
print(f"F^{k} = \n{Fk}")
print("Fibo_{k+1} =", Fk[0, 0])
print("Fibo_k     =", Fk[0, 1])
print("Fibo_{k-1} =", Fk[1, 1])
