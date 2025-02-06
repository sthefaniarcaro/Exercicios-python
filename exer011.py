# magic 8 ball - use of random library
import random

def magic_ball(n):
  if n==0:
    print('Very doubtful.')
  elif n==1:
    print('Yes - definitely.')
  elif n==2:
    print('It is decidedly so.')
  elif n==3:
    print('Without a doubt.')
  elif n==4:
    print('Reply hazy, try again.')
  elif n==5:
    print('Ask again later.')
  elif n==6:
    print('Better not tell you now.')
  elif n==7:
    print('My sources say no.')
  else:
    print('Outlook not so good.')

question = str(input('Type a question: '))
n = random.randint(0,8)
magic_ball(n)