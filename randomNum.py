import random

c = 10

def rGen(c):
    nums = list(range(c))
    random.shuffle(nums)
    print(nums)

rGen(c)


