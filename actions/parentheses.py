def get_result_highest_priority(math_expression):
  result_string = []
  new_string = []
  count = 0

  flag = False
  while True:
    if math_expression[count] == '(':
      flag = True
      
    if flag == True and math_expression[count] != ')':
      new_string.append(math_expression[count])
      
    if math_expression[count] == ')' and flag == False:
      print('Синтаксическая ошибка!')
      break

    if flag == True and math_expression[count] == ')':
      new_string.append(math_expression[count])
      flag = False
      result_string.append(''.join(new_string))
      new_string = []

    if count == len(math_expression) - 1:
      break

    count += 1
    
  return result_string

  