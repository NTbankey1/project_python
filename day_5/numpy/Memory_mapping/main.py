import numpy as np

filename = "large_date.npy"
np.save(filename, np.random.rand(10_000_000))
large_date = np.load(filename, mmap_mode='r')
print(large_date[:100])