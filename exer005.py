# Description: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de 
# um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

def pythagorean(a, b):
  h = ((a**2) + (b**2))**0.5
  print('hypotenuse = {}' .format(h))

a = float(input('type the cateto a:'))
b = float(input('type the cateto b:'))

pythagorean(a,b)