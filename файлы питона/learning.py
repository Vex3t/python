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

def add_numbers(a, b):
    sum = a + b
    

result = add_numbers(3, 5)
print(result)  # Выводит 8

