def quicksort(arr):
    # base case, return the input arr
    if len(arr) <= 1:
        return arr

    pivot = arr.pop()
    less_than = []
    greater_than = []
    # inductive step / sub problem
    for num in arr:
        if num <= pivot:
            less_than.append(num)
        else:
            greater_than.append(num)
    
    return quicksort(less_than) + [pivot] + quicksort(greater_than)

sorted_arr = quicksort(nums)
print('nums', nums)
print('sorted_arr', sorted_arr)
