# function and numeric input

def function_bmi(mass, height):
  bmi = mass/(height ** 2)
  print('the bmi is {}' .format(bmi))

mass = float(input('type your mass:'))
height = float(input('type your height: '))

function_bmi(mass, height)