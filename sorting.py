
def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]  
        j = i - 1

        while j >= 0 and arr[j] > current_value:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = current_value

    return arr


def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)


    return _merge(left_sorted, right_sorted)


def _merge(left, right):

    result = []
    i = 0  # pointer into left
    j = 0  # pointer into right


    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1


    result.extend(left[i:])
    result.extend(right[j:])

    return result


if __name__ == "__main__":

    test_cases = [
        [],
        [1],
        [5, 3, 8, 1, 9, 2],
        [1, 2, 3, 4, 5],         
        [5, 4, 3, 2, 1],        
        [4, 2, 4, 1, 4, 2],       
    ]

    for case in test_cases:
        insertion_result = insertion_sort(case.copy())
        merge_result = merge_sort(case.copy())
        expected = sorted(case)  

        print("input:   ", case)
        print("insertion:", insertion_result, "OK" if insertion_result == expected else "WRONG")
        print("merge:    ", merge_result, "OK" if merge_result == expected else "WRONG")
        print("-" * 40)