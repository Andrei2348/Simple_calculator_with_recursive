# def get_result(first_elem, elems, actions, count):
#    if count < len(actions):
#       if actions[count - 1] == '+':
#          first_elem = summa(first_elem, elems[count])

#       if actions[count - 1] == '-':
#          first_elem = minus(first_elem, elems[count])

#       if actions[count - 1] == '*':
#          first_elem = multiply(first_elem, elems[count])

#       if actions[count - 1] == '/':
#          first_elem = divide(first_elem, elems[count])

#       first_elem = get_result(first_elem, elems, actions, count + 1)
      
#    return first_elem


# first_elem = elems[0]
# print(f'{math_expression} => {get_result(first_elem, elems, actions, 1)}')




# example = re.match( r'[+-/*]', math_expression, re.M|re.X)
# print(re.findall(r'[+-/*]', math_expression))
# print(re.findall(r'\d', math_expression))

# print(re.search(r'(\d+(\.|,)?\d*)(\s?)([+-/*]?)(\s?)', math_expression))

# print(re.findall(r'(\d+(\.|,)?\d*)(\s?)([+-/*]?)(\s?)', math_expression))

math_expression = input('Введите выражение: ')


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
  
print(result_string)

  