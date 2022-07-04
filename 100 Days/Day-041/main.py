# Linear Search
# Time Complexity: O(n)

def linear_search(arr, target):
    for num in range(0, len(arr)):
        if arr[num] == target:
            return num
    return -1

nums_list = [3,5,1,9,6,2] 
position = linear_search(nums_list, 9)
print(position)