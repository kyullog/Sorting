# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, (len(arr) - 1)):
        cur_index = i
        smallest_value = arr[cur_index]

        for j in range(cur_index, len(arr)):
            if smallest_value > arr[j]:
                # hold = arr[j]
                # arr[j] = smallest_value
                # smallest_value = hold
                arr[j], smallest_value = smallest_value, arr[j]
        arr[cur_index] = smallest_value

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    while True:

        swaps = 0
        for i in range(len(arr) - 1):
            current = arr[i]
            neighbor = arr[i + 1]

            if current > neighbor:
                arr[i], arr[i + 1] = neighbor, current
                swaps += 1

        if swaps == 0:
            break
        else:
            swaps = 0

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
