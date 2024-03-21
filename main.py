stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below
mantissa = stdform[:stdform.find('x')].strip(' ')
exponent = stdform[stdform.find('^')+1 :].strip(' ')
E = mantissa+'E'+exponent+"."
print('This number in E notation is', E)