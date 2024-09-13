array = [1,2,3,4,5,6,7,8,9]

def binary_search(arr, target, l=0, r=None):
    # initialise the right pointer
    if r is None:
        r = len(arr) - 1

    # base case if target is never found
    if l > r:
        return -1

    midpoint = (l + r) // 2

    if arr[midpoint] == target:
        return midpoint
    
    if arr[midpoint] > target: 
        return binary_search(arr, target, l, midpoint - 1)

    if arr[midpoint] < target:
        return binary_search(arr, target, midpoint + 1, r)

result = binary_search(array, 8)
print(result)

