def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [int(input()) for _ in range(int(input("Enter the number of elements: ")))]

target = int(input("Enter the target number to search: "))

result = linear_search(arr, target)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
