a = int(input('Перше число: '))
b = int(input('Друге число: '))
d = int(input('Оберіть арифметичну операцію: \n 1 додавання \n 2 віднімання \n 3 множення \n 4 ділення \n ' ))
if d==1:
    r=a+b
    p='додовання'
    o=p
if d==2:
    r=a-b
    i='віднімання'
    o=i
if d==3:
    r=a*b
    y='множення'
    o=y
if d==4:
    r=float(a/b)
    z='ділення'
    o=z
print ('Результат ',o,' чисел ' ,a,' та ',b,'= ',r)