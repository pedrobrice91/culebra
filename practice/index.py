""" nombre = 'pedro'

print('hola '+ nombre)

def sumar(num1, num2):
    print('hola la suma de', num1, 'y', num2, 'es', num1 + num2)


sumar(1,2)




age = int(input('What is your age '))
age = age+10
print('Your age is', age)


a = '</title>'
b = '</html>'
c = '<head>'
d = '</body>'
e = '<html>'
f = '</head>'
g = '<title>'
h = '<body>'

# ❌ ⬆ DON'T CHANGE THE CODE ABOVE ⬆ ❌

# ✅ ↓ start coding below here ↓ ✅

html = e + c + g + a + f + h + d + b

print(html)


total = int(input('How much money do you have in your pocket\n'))

# ✅ ↓ YOUR CODE HERE ↓ ✅
if total > 100:
    print("Give me your money!")
elif total > 50:
    print("Buy me some coffee, you cheap!")
elif total <= 50:
    print("You are a poor guy, go away!")
 """

""" 
import random

def get_randomInt():
  	# ✅ ↓ CHANGE ONLY THIS ONE LINE BELOW ↓ ✅
	random_number = (random.randint(1,5))
	return random_number

print(get_randomInt()) """


""" def is_odd(my_number):
  	return (my_number % 2 != 0)

def my_main_code(num):
    # ✅ ↓ Your code here ↓ ✅
	return is_odd(num)

print(my_main_code(45345)) """
""" 
def useFor():
    for n in range(1,11):
        print(n)
    return n

useFor() """

""" 
def fizz_buzz():
    # ✅↓ Write your code here ↓✅
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif (i % 3 == 0):
            print('Fizz')
        elif(i % 5 == 0):
            print('Buzz')
        else:
            print(i)

# ❌↓ DON'T CHANGE THE CODE BELOW ↓❌
fizz_buzz()
 """


import random

def get_color(color_number=4):
    # Making sure is a number and not a string
    color_number = int(color_number)

    switcher = {
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black'
              }
    
    return switcher.get(color_number,"Invalid Color Number")

# ❌ ⬆ DON'T CHANGE THE CODE ABOVE ⬆ ❌

def get_allStudentColors():
    example_color = get_color(1)
    students_array = []
    # ✅ ↓ your loop here ↓ ✅
    for i in range(10):
        random.randint(0, 3)

print(get_allStudentColors())
