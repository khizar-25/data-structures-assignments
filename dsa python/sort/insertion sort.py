def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i

        while j > 0 and arr[j - 1] > key:
            arr[j] = arr[j - 1]
            j -= 1

        arr[j] = key

arr = []
n = int(input("Enter number of elements: "))
print("Enter the elements:")

for i in range(n):
    arr.append(int(input()))

insertion_sort(arr)
print("Sorted array:", arr)
