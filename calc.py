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

from actions import parentheses
from actions import lists_of_string
from actions import hight_priority
from actions import low_priority



def get_result():
   math_expression = original_expression = input('Введите выражение: ')

   # Проверка наличия скобок в выражении
   if '(' in math_expression:
      parentheses_expression = parentheses.get_result_highest_priority(math_expression)

      # Получение результатов в скобках и замена скобок результатами вычисления
      for elem in parentheses_expression:
         elems, actions = lists_of_string.get_lists(elem)
         elems, actions = hight_priority.get_result_hight_priority(elems, actions)
         first_elem = elems[0]
         result = str(low_priority.get_result_low_priority(first_elem, elems, actions, 1))
         math_expression = math_expression.replace(elem, result, 1)

   elems, actions = lists_of_string.get_lists(math_expression) 
   elems, actions = hight_priority.get_result_hight_priority(elems, actions)
   first_elem = elems[0]
   return f'Результат выражения: {original_expression} равен {low_priority.get_result_low_priority(first_elem, elems, actions, 1)}'


if __name__ == '__main__':
  print(get_result())