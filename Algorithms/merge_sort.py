def mergesort(list1):
    # condition 1 for dividing the list 
    if len(list1) > 1 :
        mid = len(list1) // 2
        left_list = list1[:mid]
        right_list = list1[mid:]
        mergesort(left_list)
        mergesort(right_list)

        # condition 2 for merging 

        i = 0
        j = 0
        k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list1[k] = left_list[i]
                i = i + 1
                k = k + 1
            else:
                list1[k] = right_list[j]
                j = j + 1
                k = k + 1
        # condition 3 for left over numbers

        while i < len(left_list):
            list1[k] = left_list[i]
            i = i + 1
            k = k + 1

        while j < len(right_list):
            list1[k] = right_list[j]
            j = j + 1
            k = k + 1

num = int(input('Enter how many numbers you wanr in a list : '))
list1 = []
for i in range(num):
    x = int(input('Enter a number : '))
    list1.append(x)

mergesort(list1)
print(list1)

# TODO trace the code

