from .actions import summa, minus
from . import logging

def get_result_low_priority(first_elem, elems, actions, count):
   if count < (len(actions) + 1):

      match actions[count - 1]:
         case '+':
            first_elem = summa(first_elem, elems[count])

         case '-':
            first_elem = minus(first_elem, elems[count])

      first_elem = get_result_low_priority(first_elem, elems, actions, count + 1)
   logging.write_log('Производим действия вычитания и сложения', 0)
   return first_elem
