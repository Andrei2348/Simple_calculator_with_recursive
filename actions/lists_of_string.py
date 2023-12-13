import re
from . import logging

def get_lists(math_expression):
  # Список элементов
  elems = []
  # Список знаков действия
  actions = []
  logging.write_log(f'Получаем исходное выражение от пользователя: {math_expression}', 1)
  math_expression_list = (re.findall(r'(\d+(\.|,)?\d*)(\s?)([+-/*]?)(\s?)', math_expression))

  # Разбивка выражения на список чисел и список знаков действия
  for elem in math_expression_list:
    elems.append(float(elem[0]))
    actions.append(elem[-2])
  return elems, actions