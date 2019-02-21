def print_everything(*args, **kwargs):
    for arg in args:
        print(arg)

    for k, v in kwargs.items():
        print("%s: %s" % (k, v))

# we can write all the parameters individually
print_everything("cat", "dog", day="Tuesday")

t = ("cat", "dog")
d = {"day": "Tuesday"}

# we can unpack a tuple and a dictionary
print_everything(*t, **d)
# or just one of them
print_everything(*t, day="Tuesday")
print_everything("cat", "dog", **d)

# we can mix * and ** with explicit parameters
print_everything("Jane", *t, **d)
print_everything("Jane", *t, time="evening", **d)
print_everything(time="evening", *t, **d)

# none of these are allowed:
# print_everything(*t, "Jane", **d)
# ßprint_everything(*t, **d, time="evening")