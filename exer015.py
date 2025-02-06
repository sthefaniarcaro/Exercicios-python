
def question1(q1):
    if q1 == 1:
       gry += 1
       rav += 1
    elif q1 == 2:
         huf += 1
         sly += 1
    else:
        print('wrong input, try again')
        return 0
    return 1



# gryffindor, ravenclaw, hufflepuff and slytherin
gry = rav = huf = sly = 0

while True:
    print('\tQ1) do you like dawn or dusk?')
    print('\t\t1) Dawn\n\t\t2) Dusk')
    q1 = int(input('\t\t'))

    op = question1(q1)
    if op == 1:
        break

print('gryffindor: ',gry)