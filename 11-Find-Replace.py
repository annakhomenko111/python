import random

def rGen():
    nums = list(range(10))
    random.shuffle(nums)
    print(nums)


    n = int(input('какое число чтобы заменить от 0 до 10 : '))
    nums.pop(n)
    nums.insert(n, n)
    print(nums)

rGen()

# https://www.youtube.com/watch?v=v8Q6nR7itsU