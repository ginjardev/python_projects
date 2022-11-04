#recursive approach

def binary_search(start, end, int_list, target):
    if start <= end:
        mid = (start + end) // 2

        if int_list[mid] == target:
            return mid +1
        elif target < int_list[mid]:
            return binary_search(start, mid -1, int_list, target)
        elif target > int_list[mid]:
            return binary_search(mid + 1, end, int_list, target)
        else:
            return -1



# collect user input

length = int(input("Enter length of list: "))
int_list = []

for i in range(length):
    element = int(input('Enter a number: '))
    int_list.append(element)

int_list = sorted(int_list)
print(int_list)

target = int(input("Enter target element: "))

position = binary_search(0, length-1, int_list, target)
if position == -1:
    print("Element not in list")
else: 
    print("Element is at position: " + str(position))