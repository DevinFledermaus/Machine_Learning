import numpy as np
x = np.arange(21)
print("\nArray:")
print(x)

a = np.mean(x)
b = np.average(x)
assert np.allclose(a, b)
print("\nMean: ", a)

a = np.std(x)
b = np.sqrt(np.mean((x - np.mean(x)) ** 2))
assert np.allclose(a, b)
print("\nstd deviation: ", a)

a = np.var(x)
b = np.mean((x - np.mean(x)) ** 2)
assert np.allclose(a, b)
print("\nvariance: ", a)
