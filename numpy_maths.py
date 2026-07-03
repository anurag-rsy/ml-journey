import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Write these yourself — predict output before running each
print(np.sum(arr))           
print(np.sum(arr, axis=0))   
print(np.sum(arr, axis=1))   
print(np.mean(arr))          
print(np.std(arr))           
print(np.min(arr))           
print(np.max(arr))           
print(np.cumsum(arr))        
print(np.argmax(arr))        
a = np.arange(12)   # [0, 1, 2, ... 11]

# Predict shape before running each line
b = a.reshape(3, 4)       
c = a.reshape(2, 6)       
d = a.reshape(2, 2, 3)    
e = b.flatten()           
f = b.T                  

print(b.shape)
print(c.shape)
print(d.shape)
print(e.shape)
print(f.shape)

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

# Predict shape AND values before running
print(np.vstack([a, b]))        
print(np.hstack([a, b]))        
print(np.concatenate([a, b], axis=0)) 
print(np.concatenate([a, b], axis=1))

# Reproducibility — always set seed in ML experiments
np.random.seed(42)

a = np.random.normal(loc=0, scale=1, size=(3, 3))   # Gaussian
b = np.random.uniform(0, 10, (3, 3))                 # Uniform
c = np.random.randint(0, 100, (3, 3))                # Integers
d = np.random.choice([1, 2, 3, 4, 5], size=10, replace=True)

print(a)
print(b)
print(c)
print(d)

np.random.seed(42)

n = 1000
masses     = np.random.normal(loc=5, scale=2, size=n)
velocities = np.random.normal(loc=0, scale=30, size=n)
charges    = np.random.choice([-1, 1], size=n)

# 1. Reshape masses into a (10, 100) matrix — why might this be useful?
ke = 0.5 * masses * velocities**2

mean_ke = np.mean(ke)
std_ke = np.std(ke)
min_ke = np.min(ke)
max_ke = np.max(ke)

masses_matrix = masses.reshape(10, 100)
print(f"masses_matrix shape: {masses_matrix.shape}")

# 3. Stack masses and velocities into a (1000, 2) matrix called features
# your code here — hint: use np.column_stack or np.vstack
features = np.column_stack((masses.flatten(), velocities.flatten()))
ke = 0.5 * masses * velocities**2
# 4. Print shape of features — should be (1000, 2)
# your code here
print(features.shape)
    