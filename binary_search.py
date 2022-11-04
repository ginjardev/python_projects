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