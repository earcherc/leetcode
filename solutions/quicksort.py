array = [2,1,3,6,7,9,0]

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr.pop()
    left, right = [], []

    for num in arr:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)

    return quicksort(left) + [pivot] + quicksort(right)

sorted = quicksort(array)
print(sorted)


