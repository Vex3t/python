"""""1
name = "Tom" #переменная для хранения данных, может называться как угодно, но должна быть написао словом, так же желательно давать перменным понятные названия
print (name) # напечатав имя переменной в скобочках с принтом, она выведиться
name = "Bob"
print (name)
 #bool - логический оператор который принимает значения true и false, часто юзаеться с if and else

1"""""





"""""2
isill = False
print (isill) #False

isclear = True
print (isclear) #True
2"""""



"""""3
age = 18
if age >= 18:
    print("Вы совершеннолетний")

else:
    print(" Вы педик")
   3 """""



"""""4
age = 21.3
print ("Age", age)

count = 21
print ("Count", count)
4"""""




"""""5
a = 0b11
b = 0b1011
c = 0b100001
print(a)    # 3 в десятичной системе
print(b)    # 11 в десятичной системе
print(c)    # 33 в десятичной системе
5"""""



"""""6
height = 3.12
pi = 3.14
weight = 3.16
print (height * weight)
6"""""





"""""7
you_say = "Hello World!"
print (you_say)

name = "Tom"
print (name)
7"""""


"""""8
myName = "Alex"
myAge = 14
user = f"name:  {myName}, age:   {myAge}"
print (user)
8"""""



"""""9
nubmer = 2
nubmer += 5
print (nubmer)

a = 3.6
round = round(a)
print (round)
9"""""




"""""10
number_a = 2.12123123
number_b = 3

z = number_a + number_b
print(round(z)) #round функция которая округляет число
10"""""







"""""11
massive = [1,2,3,4,5,6]
#number = list2() = number = [] просто создает пустой список
print (massive)

a = [2,2,41,1,]
b = list(a)
print (b)

letters = list("hello")
print (letters)

boys = ("Tom", "Lisa", "Michel")

#print(boys[0])
#print(boys[1])
#print(boys[2])

Tom, Lisa, Michel, = boys

print (Tom)
print (Lisa)
print (Michel)
11"""""
"""""12
def true_false():
        a = 17
        b = 12
        if a<b:
                print("FR")
        else:
                print ("Crap")



true_false()
12"""""
"""""13
def print_messages():
    # определение локальных функций
    def say_hello(): 
        print("Hello")
    def say_goodbye(): 
        print("Good Bye")
    # вызов локальных функций
    say_hello()
    say_goodbye()
 
# Вызов функции print_messages
print_messages()
 
#say_hello() # вне функции print_messages функция say_hello не доступна
13"""""

"""""14
def add_numbers(a, b):
    sum = a + b
    

result = add_numbers(3, 5)
print(result)  # Выводит 8
14"""""
 
"""""14
a = 5
b = 6
result = 5 == 6  # сохраняем результат операции в переменную
print(result)  # False - 5 не равно 6
print(a != b)  # True
print(a > b)  # False - 5 меньше 6
print(a < b)  # True
 
bool1 = True
bool2 = False
print(bool1 == bool2)  # False - bool1 не равно bool2
14"""""
"""""15
a = input ('s')
b = input ('s')

print (int(a)+int(b))
15"""""

"""""16
#My tipical calculator

f1 = float(input("Введите ваше первое число:  "))
f2 = float(input("Введите ваше второе число:  "))

print(" Выберите опцию:  ")
print("1: умножение  ")
print("2: деление   ")
print("3: вычетание  ")
print("4: сложение  ")
print("5: отнимание  ")

chose = float(input("1/2/3/4/5:    "))

if chose == 1:
    result = f1*f2
    print (result, "Это и есть ваш результат")

elif chose == 2:
    result = f1/f2
    print (result, "Это и есть ваш результат")

elif chose == 3:
    result = f1%f2
    print (result, "Это и есть ваш результат")

elif chose == 4:
    result = f1+f2
    print (result, "Это и есть ваш результат")

elif chose == 5:
    result = f1-f2
    print (result, "Это и есть ваш результат")
    16"""""


"""""17
def multiply(a, b=2):
    return a * b


result1 = multiply(3)
result2 = multiply(3,4)

print (result1, result2)
17"""""

"""""18
a = int(input("Введите ваш возраст:   "))

if a <=12:
    print("Это ребенок")
elif a<=22:
    print("Это взрослый")
else:
    print('Это дед')
18"""""
"""""19
word = ""
while word != "стоп":
    word = input("Введите слово: ")
    print("Вы ввели: " + word)
19"""""

numbers = []
while True:
    n = input("Введите число (или 'стоп', чтобы закончить ввод): ")
    if n == "стоп":
        break
    numbers.append(int(n))
if len(numbers) > 0:
    print("Наибольшее число: ", max(numbers))
    print("Наименьшее число: ", min(numbers))
else:
    print("Список пуст")
