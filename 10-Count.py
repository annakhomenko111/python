

def count():
    n = int(input('Введите значение: '))
    s = str(n)
    sum = 0

    for i in range(len(s)):
        sum += int(s[i])
    print (sum)

count()


# https://www.youtube.com/watch?v=gb_vQw8-OEY