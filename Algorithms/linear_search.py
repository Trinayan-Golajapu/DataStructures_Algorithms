pos = -1
def linear_search(lst,n):
    i = 0
    while i < len(lst):
        if lst[i] == n:
            globals()['pos'] = i
            return True
        i = i + 1
    return False
lst = [5,7,33,6,88,53,1]
n = 1

if linear_search(lst,n):
    print('{} found at index {}'.format(n,pos))
else:
    print('not found')