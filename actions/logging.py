import logging

def write_log(message, flag):
  if flag == 0:
    logging.basicConfig(filename = './history.log',
                        encoding = 'utf-8',
                        level = logging.NOTSET)
  else:
    logging.basicConfig(filename = './history.log',
                        filemode='w',
                        encoding = 'utf-8',
                        level = logging.NOTSET)
  logger = logging.getLogger(' Калькулятор ')
  logger.info(message)