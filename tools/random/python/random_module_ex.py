import random

### no seed input -> different output everytime
print("="*30)
print("="*5+"  random.seed()")

random.seed()
print("no_seed_1 :", random.random())
print("no_seed_2 :", random.random())
print("no_seed_3 :", random.random())
print("no_seed_4 :", random.random())
print("no_seed_5 :", random.random())
print("no_seed_6 :", random.random())
print("\n")

### with seed input -> same output everytime
print("="*30)
print("="*5+"  random.seed(0)")

random.seed(0)
print("with_seed_1 :", random.random())
print("with_seed_2 :", random.random())
print("with_seed_3 :", random.random())
print("with_seed_4 :", random.random())
print("with_seed_5 :", random.random())
print("with_seed_6 :", random.random())
print("\n\n\n")
