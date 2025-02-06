# type of variable

def variable_type(var):
    print('the type of the variable is: ', type(var))
    print('the variale is a number: ', var.isnumeric())
    print('the variable is a space: ', var.isspace())
    print('the variable is a letter: ', var.isalpha())
    print('the variable is a alphanumeric: ', var.isalnum())
    print('the variable is a upper case: ', var.isupper())
    print('the variable is a lower case: ', var.islower())
    print('the variable is a title case: ', var.istitle())

var = input('type a variable: ')
variable_type(var)