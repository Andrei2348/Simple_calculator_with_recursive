from .actions import multiply, divide
from . import logging

# Действия высокого приоритета
def get_result_hight_priority(elems, actions):
   if '*' in actions or '/' in actions:
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
         logging.write_log('Производим действия умножения и деления', 0)
         if actions[index] == '+' or actions[index] == '-':
            if flag == False:
               low_priority_elem.append(elems[index])
               low_priority_action.append(actions[index])
            else:
               flag = False
               low_priority_action.append(actions[index])
               
         if actions[index] == '' and flag == False:
            low_priority_elem.append(elems[index])

   else:
      low_priority_elem = elems
      low_priority_action = actions
   logging.write_log('Формируем списки данных для действий сложения и вычитания', 0)
   return low_priority_elem, low_priority_action




