# Задача 1 необязательная. Напишите рекурсивную программу вычисления 
# арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:* 

# 2+2 => 4; 

# 1+2*3 => 7; 

# 1-2*3 => -5;

# - Добавьте возможность использования скобок, меняющих приоритет операций.

#     *Пример:* 


#     1+2*3 => 7; 

#     (1+2)*3 => 9;
# Тут может помочь библиотека re


# example = re.match( r'[+-/*]', math_expression, re.M|re.X)
# print(re.findall(r'[+-/*]', math_expression))
# print(re.findall(r'\d', math_expression))

# print(re.search(r'(\d+(\.|,)?\d*)(\s?)([+-/*]?)(\s?)', math_expression))

# print(re.findall(r'(\d+(\.|,)?\d*)(\s?)([+-/*]?)(\s?)', math_expression))




import re

math_expression = input('Введите выражение: ')
math_expression_list = (re.findall(r'(\d+(\.|,)?\d*)(\s?)([+-/*]?)(\s?)', math_expression))

# Список элементов
elems = []
# Список знаков действия
actions = []

for elem in math_expression_list:
   elems.append(float(elem[0]))
   actions.append(elem[-2])

print(elems)
print(actions)

def summa(a, b):
   return a + b

def minus(a, b):
   return a - b

def multiply(a, b):
   return a * b

def divide(a, b):
   return a / b

# def get_result(first_elem, elems, actions, count):
#    if count < len(actions):
#       if actions[count - 1] == '+':
#          first_elem = summa(first_elem, elems[count])

#       if actions[count - 1] == '-':
#          first_elem = minus(first_elem, elems[count])

#       if actions[count - 1] == '*':
#          first_elem = multiply(first_elem, elems[count])

#       if actions[count - 1] == '*':
#          first_elem = divide(first_elem, elems[count])

#       first_elem = get_result(first_elem, elems, actions, count + 1)
      
#    return first_elem


# first_elem = elems[0]
# print(f'{math_expression} => {get_result(first_elem, elems, actions, 1)}')



def get_result(first_elem, elems, actions, count):
   if count < len(actions):

      match actions[count - 1]:
         case '+':
            first_elem = summa(first_elem, elems[count])

         case '-':
            first_elem = minus(first_elem, elems[count])

         case '*':
            first_elem = multiply(first_elem, elems[count])

         case '*':
            first_elem = divide(first_elem, elems[count])

      first_elem = get_result(first_elem, elems, actions, count + 1)
      
   return first_elem


first_elem = elems[0]
print(f'{math_expression} => {get_result(first_elem, elems, actions, 1)}')