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

import re

def summa(a, b):
   return a + b

def minus(a, b):
   return a - b

def multiply(a, b):
   return a * b

def divide(a, b):
   return a / b


def get_result(first_elem, elems, actions, count):
   if count < (len(actions) + 1):

      match actions[count - 1]:
         case '+':
            first_elem = summa(first_elem, elems[count])

         case '-':
            first_elem = minus(first_elem, elems[count])

         case '*':
            first_elem = multiply(first_elem, elems[count])

         case '/':
            first_elem = divide(first_elem, elems[count])

      first_elem = get_result(first_elem, elems, actions, count + 1)
      
   return first_elem



math_expression = input('Введите выражение: ')
math_expression_list = (re.findall(r'(\d+(\.|,)?\d*)(\s?)([+-/*]?)(\s?)', math_expression))

# Список элементов
elems = []
# Список знаков действия
actions = []

for elem in math_expression_list:
   elems.append(float(elem[0]))
   actions.append(elem[-2])

# print(elems)
# print(actions)


low_priority_action = []
low_priority_elem = []


flag = False
for index in range(0, len(actions)):
   if actions[index] == '*':
      if flag:
         low_priority_elem[-1] = multiply(low_priority_elem[-1], elems[index + 1])
      else:
         elem = multiply(elems[index], elems[index + 1])
         flag = True
         low_priority_elem.append(elem)
      
   if actions[index] == '/':
      if flag:
         low_priority_elem[-1] = divide(low_priority_elem[-1], elems[index + 1])
      else:
         elem = divide(elems[index], elems[index + 1])
         flag = True
         low_priority_elem.append(elem)
   
   if actions[index] == '+' or actions[index] == '-':
      if flag == False:
         low_priority_elem.append(elems[index])
         low_priority_action.append(actions[index])
      else:
         flag = False
         low_priority_action.append(actions[index])
         
   if actions[index] == '' and flag == False:
      low_priority_elem.append(elems[index])
   
print(low_priority_elem)
print(low_priority_action)
   

first_elem = low_priority_elem[0]
print(f'{math_expression} => {get_result(first_elem, low_priority_elem, low_priority_action, 1)}')