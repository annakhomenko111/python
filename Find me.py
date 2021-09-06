import random

c = 10
nums = list(range(c))
random.shuffle(nums)
print(nums)

a = int(input('Какое число найти?: '))

def find (a):
    for i in nums:
        if i == a:
            print('число ',i, 'находится в списке под номером' ,nums.index(i))
        else:
            print('число ',i, 'не равно ' ,a,)

find(a)




