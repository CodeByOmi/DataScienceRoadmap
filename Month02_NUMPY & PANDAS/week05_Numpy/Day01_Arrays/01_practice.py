import numpy as np

steps = np.array([[8500,9000,7500,8000,8400,9500,8300,10000],
                 [8000,8500,9000,7500,8000,8400,9500,8300],
                 [8100,10000,8000,8500,9000,7500,8000,8400]])
print(steps)

print("shape;", steps.shape)
print("size;", steps.size)
print("dtype;", steps.dtype)
print("ndim;", steps.ndim)


print(steps[0,0])
print(steps[1,7])
print(steps[2,-8])

