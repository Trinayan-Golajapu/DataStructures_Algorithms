stack = []

def push():
    if n > len(stack):
        element = int(input('ENTER A NUMBER : '))
        stack.append(element)
        print(stack)
    else:
        print('stack is full')

def pop():
    if len(stack) == 0:
        print('stack is empty')
    else:

        number = stack.pop()

        print(number)

n = int(input('enter stack limit :  '))
while True:
    choice = int(input('1-->push, 2-->pop, 3-->exit : '))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print('enter correct number')
    


