def sort(arr):
    # applying a selection sort algorithm
    for i in range(len(arr)):
        curr_lowest = arr[i]

        for j in range(i, len(arr)):
            if arr[j] < curr_lowest:
                curr_lowest = arr[j]
                arr[i], arr[j] = arr[j], arr[i]

    return arr

