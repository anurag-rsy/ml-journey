import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# NumPy test
arr = np.array([1, 2, 3, 4, 5])
print("NumPy mean:", arr.mean())

# Pandas test
df = pd.DataFrame({'x': [1,2,3], 'y': [4,5,6]})
print(df.head())

# Plot test
plt.plot([1,2,3], [4,5,6])
plt.title("Setup verified")
plt.savefig("verify.png")
print("Plot saved. Setup complete.")