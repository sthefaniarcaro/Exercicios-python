# predecessor and successor of a number

def number(n):
    predecessor = n - 1
    successor = n + 1
    print('the number is: ',n)
    print('the predecessor is: ',predecessor)
    print('the successor is: ',successor)

n = int(input('type a number: '))
number(n)