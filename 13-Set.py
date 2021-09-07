import random



def rGen():
    a = {random.randint(-10,10) for i in range (10)}
    print(a)

    b = {random.randint(-10, 10) for i in range(10)}
    print(b)

    с = a & b
    print('Intersection', с)


rGen()

# https://www.youtube.com/watch?v=_zBTBr6XdZo&t=71s
# https://www.youtube.com/watch?v=KMGRXDxUw18&t=263s