# Description: Create a program that checks if a person can ride a roller coaster. 
# The person must be at least 137 cm tall and have 10 credits. 
# The program must ask the user for their height and the number of credits. 

def cyclone(height, credit):
  if height >= 137 and credit >= 10:
    print('enjoy the ride!')
  elif height < 137 and credit >=10:
    print('you are not tall enough to ride!')
  elif height >= 137 and credit < 10:
    print('you dont have enough credits!')
  else:
    print('you dont have met either requirement!')


print('to ride a cyclone you must be at least 137 cm tall and have 10 credits\n\n')
height = float(input('type your height in cm: '))
credit = int(input('type your credit: '))

cyclone(height, credit)