from . import logging

def summa(a, b):
   return a + b

def minus(a, b):
   return a - b

def multiply(a, b):
   return a * b

def divide(a, b):
   try:
      return a / b
   except:
      print('Ошибка: деление на 0!')
      logging.write_log('Ошибка: деление на 0!', 0)