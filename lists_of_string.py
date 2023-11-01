import re

def get_lists(math_expression):
  # Список элементов
  elems = []
  # Список знаков действия
  actions = []
  math_expression_list = (re.findall(r'(\d+(\.|,)?\d*)(\s?)([+-/*]?)(\s?)', math_expression))
   
  # Разбивка выражения на список чисел и список знаков действия
  for elem in math_expression_list:
    elems.append(float(elem[0]))
    actions.append(elem[-2])
  return elems, actions