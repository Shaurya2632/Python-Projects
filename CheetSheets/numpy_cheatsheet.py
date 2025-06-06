import numpy as np

# -------- Array Creation --------
a = np.array([1, 2, 3])
# Creates a 1D numpy array from a Python list

b = np.array([[1, 2], [3, 4]])
# Creates a 2D numpy array from nested lists

c = np.full((2, 2), 7)
# Creates a 2x2 array filled with the value 7

d = np.arange(0, 10, 2)
# Creates array starting at 0, up to but not including 10, step 2: [0,2,4,6,8]

e = np.linspace(0, 1, 5)
# Creates 5 evenly spaced numbers between 0 and 1 inclusive

# -------- Special Arrays --------
zeros = np.zeros((2, 3))
# 2x3 array filled with zeros

ones = np.ones((2, 3))
# 2x3 array filled with ones

empty = np.empty((2, 2))
# 2x2 array with uninitialized (random) values — faster to create but contains garbage

eye = np.eye(3)
# 3x3 Identity matrix with 1s on the diagonal and 0 elsewhere

identity = np.identity(3)
# Another way to create a 3x3 identity matrix

diag = np.diag([1, 2, 3])
# Creates a diagonal matrix with diagonal values 1, 2, 3

# -------- Reshaping and Flattening --------
reshaped = a.reshape((3, 1))
# Changes shape of array 'a' to 3 rows and 1 column

flattened = b.flatten()
# Converts 2D array 'b' into 1D array (copy)

raveled = b.ravel()
# Converts 2D array 'b' into 1D array (view, no copy)

transposed = b.T
# Transposes rows and columns of array 'b'

# -------- Indexing and Slicing --------
element = a[1]
# Gets element at index 1 (second element)

slice_a = a[1:3]
# Gets elements from index 1 up to (but not including) index 3

reversed_a = a[::-1]
# Reverses array 'a'

# -------- Arithmetic Operations --------
add = a + a
# Element-wise addition of arrays

sub = a - a
# Element-wise subtraction

mul = a * a
# Element-wise multiplication

div = a / (a + 1)
# Element-wise division

power = a ** 2
# Element-wise power

# -------- Aggregation Functions --------
sum_val = np.sum(a)
# Sum of all elements

mean_val = np.mean(a)
# Mean (average) value

std_val = np.std(a)
# Standard deviation

min_val = np.min(a)
# Minimum value in array

max_val = np.max(a)
# Maximum value in array

argmax = np.argmax(a)
# Index of the maximum value

argmin = np.argmin(a)
# Index of the minimum value

# -------- Boolean Masking --------
mask = a > 1
# Boolean array where elements greater than 1 are True

filtered = a[mask]
# Select elements from 'a' where mask is True

# -------- Broadcasting --------
x = np.array([[1], [2], [3]])
y = np.array([10, 20, 30])
broadcast_result = x + y
# Broadcasting adds x (3x1) and y (1x3) to form a 3x3 array by automatic expansion

# -------- Random Numbers --------
np.random.seed(0)
# Set seed for reproducibility

rand = np.random.rand(3)
# Generate 3 random floats in [0, 1)

randn = np.random.randn(3)
# Generate 3 samples from standard normal distribution

randint = np.random.randint(0, 10, (2, 2))
# Generate 2x2 array of random integers from 0 to 9

# -------- File I/O --------
np.save('data.npy', a)
# Save array 'a' to a binary file 'data.npy'

loaded = np.load('data.npy')
# Load array from file 'data.npy'

# -------- Linear Algebra --------
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[2, 0], [1, 2]])

dot_product = np.dot(mat1, mat2)
# Matrix multiplication of mat1 and mat2

inv = np.linalg.inv(mat1)
# Inverse of matrix mat1

eigvals, eigvecs = np.linalg.eig(mat1)
# Eigenvalues and eigenvectors of mat1

det = np.linalg.det(mat1)
# Determinant of matrix mat1
