import numpy as np

### no seed input -> different output everytime
print("="*30)
print("="*5+"  np.random.seed()")

np.random.seed()
print("no_seed_1 :", np.random.random())
print("no_seed_2 :", np.random.random())
print("no_seed_3 :", np.random.random())
print("no_seed_4 :", np.random.random())
print("no_seed_5 :", np.random.random())
print("no_seed_6 :", np.random.random())
print("\n")

### with seed input -> same output everytime
print("="*30)
print("="*5+"  np.random.seed(0)")

np.random.seed(0)
print("with_seed_1 :", np.random.random())
print("with_seed_2 :", np.random.random())
print("with_seed_3 :", np.random.random())
print("with_seed_4 :", np.random.random())
print("with_seed_5 :", np.random.random())
print("with_seed_6 :", np.random.random())
print("\n\n")
