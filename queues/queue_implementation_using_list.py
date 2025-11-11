queue = []

def enqueue():
    element = int(input('enter number : '))
    queue.append(element)
    print(queue)

def dequeue():
    removed_element = queue.pop(0)
    print(f'removed_element is {removed_element}')
    print(f'updated queue is {queue}')

def display():
    print(queue)


while True:
    n = int(input("Enter 1 for add, 2 for remove, 3 for display, 4 for exit : "))
    if n == 1:
        enqueue()
    elif n == 2:
        dequeue()
    elif n == 3:
        display()
    elif n == 4:
        break
    else:
        print('Enter Correct Number')