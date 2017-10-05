import numpy as np

def threahold(val):
    "Return 0 if val<0"
    if val < 0.0:
        return 0.0
    else:
        return val

sample = np.random.randn(10,10)
print(sample)
vec = np.vectorize(threahold)
print(vec(sample))
