import json

with open('steam.json') as steamdata:
    data = json.load(steamdata)


def merge_sort(array, left_index, right_index, option):
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2
    merge_sort(array, left_index, middle, option)
    merge_sort(array, middle + 1, right_index, option)
    merge(array, left_index, right_index, middle, option)

def merge(array, left_index, right_index, middle, option):
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
        if left_copy[left_copy_index][option] == right_copy[right_copy_index][option]:
            if left_copy[left_copy_index]['name'] <= right_copy[right_copy_index]['name']:
                array[sorted_index] = left_copy[left_copy_index]
                left_copy_index += 1
            else:
                array[sorted_index] = right_copy[right_copy_index]
                right_copy_index += 1
        elif left_copy[left_copy_index][option] <= right_copy[right_copy_index][option]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index += 1
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index += 1
        sorted_index += 1
    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index += 1
        sorted_index += 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index += 1
        sorted_index += 1



def sort_list(list, option, order):
    if order == 'up':
        merge_sort(list, 0, len(list) - 1, option)
        return list
    else: #down
        merge_sort(list, 0, len(list) - 1, option)
        return list[::-1]

