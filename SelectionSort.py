
def selectionSort(arr):
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        temp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = temp

    for i in range(len(arr)):
        print(arr[i])



lst = [10,5,8,22,18]
selectionSort(lst)
