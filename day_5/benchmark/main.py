import numpy as np 
import time

A = np.random.rand(1000, 1000)
B = np.random.rand(1000, 1000)

start_time = time.time()
C = np.dot(A, B)
end_time = time.time()

print("thời gian nhân ma trận ", end_time - start_time)