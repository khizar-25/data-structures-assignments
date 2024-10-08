def bubblesort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(1, n - i):  # Modification to the inner loop
            if arr[j - 1] > arr[j]:  # Adjusted index comparison
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                swapped = True
        
        if not swapped:
            break

arr = []
n = int(input("Enter number of elements: "))
print("Enter the elements:")

for i in range(n):
    arr.append(int(input()))

bubblesort(arr)
print("Sorted array:", arr)
