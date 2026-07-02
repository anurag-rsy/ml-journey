import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.zeros((3, 4))
c = np.ones((2, 3))
d = np.arange(0, 20, 2)
e = np.linspace(0, 1, 10)
f = np.random.uniform(0, 10, (3, 3))

# Print shape, ndim, dtype for ALL 6 arrays
print("Array a - Shape:", a.shape, "NDim:", a.ndim, "DType:", a.dtype)
print("Array b - Shape:", b.shape, "NDim:", b.ndim, "DType:", b.dtype)
print("Array c - Shape:", c.shape, "NDim:", c.ndim, "DType:", c.dtype)
print("Array d - Shape:", d.shape, "NDim:", d.ndim, "DType:", d.dtype)
print("Array e - Shape:", e.shape, "NDim:", e.ndim, "DType:", e.dtype)
print("Array f - Shape:", f.shape, "NDim:", f.ndim, "DType:", f.dtype)

arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

# prediction: 10
print(arr[0, 0])

# prediction: 80
print(arr[2, 1])

# prediction: [20 50 80]
print(arr[:, 1])

# prediction: [40 50 60]
print(arr[1, :])

# prediction: [[10 20] [40 50]]
print(arr[0:2, 0:2])

# prediction: [60 70 80 90]
print(arr[arr > 50])

import time

# Python loop — slow
a = list(range(1_000_000))
start = time.time()
result_loop = [x**2 for x in a]
print(f"Loop:  {time.time() - start:.4f} sec")

# NumPy vectorization — fast
b = np.arange(1_000_000)
start = time.time()
result_numpy = b**2
print(f"NumPy: {time.time() - start:.4f} sec")

a = np.array([[1, 2, 3],
              [4, 5, 6]])       # shape (2, 3)

b = np.array([10, 20, 30])     # shape (3,)

# prediction: shape (2,3) → [[11 22 33] [14 25 36]]
print(a + b)

c = np.array([[10],
              [20]])            # shape (2, 1)

# prediction: shape (2,3) → [[11 12 13] [24 25 26]]
print(a + c)

c = np.array([[10],
              [20]])            # shape (2, 1)

# Predict: what shape does a + c produce?
# your prediction here as a comment
print(a + c)

n = 1000
masses     = np.random.uniform(0.1, 10, n)
velocities = np.random.uniform(-50, 50, n)
charges    = np.random.choice([-1, 1], n)

# 4 lines — write these yourself:
# 1. Compute KE for all 1000 particles at once (no loop)
ke = 0.5 * masses * velocities**2
# 2. Compute momentum for all 1000 particles at once (no loop)
momentum = masses * velocities
# 3. Boolean index: find all particles where KE > 100 joules
high_ke_particles = ke[ke > 100]
# 4. Print: how many particles have KE > 100?
print(f"Number of particles with KE > 100: {len(high_ke_particles)}")