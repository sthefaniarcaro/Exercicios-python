# ph level - if/else/elif statement

def ph_levels(ph):
  if ph > 7:
    print('Basic')
  elif ph < 7:
    print('Acidic')
  else:
    print('Neutral')

ph = float(input('type a ph value between 0 and 14: '))
ph_levels(ph)