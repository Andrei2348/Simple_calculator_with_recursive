from .actions import summa, minus

def get_result_low_priority(first_elem, elems, actions, count):
   if count < (len(actions) + 1):

      match actions[count - 1]:
         case '+':
            first_elem = summa(first_elem, elems[count])

         case '-':
            first_elem = minus(first_elem, elems[count])

      first_elem = get_result_low_priority(first_elem, elems, actions, count + 1)
      
   return first_elem
