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

from parentheses import get_result_highest_priority
from lists_of_string import get_lists
from hight_priority import get_result_hight_priority
from low_priority import get_result_low_priority


math_expression = input('Введите выражение: ')

# Проверка наличия скобок в выражении
if '(' in math_expression:
   parentheses_expression = get_result_highest_priority(math_expression)

   # Получение результатов в скобках и замена скобок результатами вычисления
   for elem in parentheses_expression:
      elems, actions = get_lists(elem)
      elems, actions = get_result_hight_priority(elems, actions)
      first_elem = elems[0]
      result = str(get_result_low_priority(first_elem, elems, actions, 1))
      math_expression = math_expression.replace(elem, result, 1)

elems, actions = get_lists(math_expression) 
elems, actions = get_result_hight_priority(elems, actions)
first_elem = elems[0]
print(f'{math_expression} => {get_result_low_priority(first_elem, elems, actions, 1)}')
