
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    for val in arr:
        print(val)



lst = [10,5,8,22,18]
bubbleSort(lst)