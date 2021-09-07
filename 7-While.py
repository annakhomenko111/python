a = int(input('Введите первое значение: '))
b = int(input('Введите второе значение: '))
c = int(input('Введите третье значение: '))

def comparison(a,b,c):
    while a <= b:
        a = a + c
        if a < b:
            print('A<B', a, 'меньше', b)
        elif a == b:
            print('A=B', a, 'равно', b)
    else:
        print('Какой-то радостный текст A>B', a, 'больше', b)



comparison(a,b,c)

# https://www.youtube.com/watch?v=Ll3AN1FXXfE