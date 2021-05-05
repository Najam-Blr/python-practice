import array

arr = array.array('i', [10, 22, 15, 8, 5])

# Sum of the array
sum = 0
for elem in range(len(arr)):
    sum += arr[elem]

print("Sum of the array :", sum)

# largest element in the array

max = arr[0]
for i in range(1, len(arr)):
    if arr[i] > max:
        max = arr[i]

print("Max elem: ", max)

# array rotation
print("Before rotation", arr)
rotElem = 2
for j in range(rotElem):
    temp = arr[0]
    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]
    print(temp)
    arr[len(arr) - 1] = temp

print("After rotation", arr)

# Find remainder of array

mul = 1
for i in range(len(arr)):
    print(arr[i], mul)
    mul = mul * arr[i]

rem = mul % len(arr)
print(rem)

# find monotonic array: if the array either in increasing order or decreasing order

arr = array.array('i', [1, 23, 156, 85, 98])

monotonic = False
for i in range(len(arr) - 1):
    if arr[i] < arr[i + 1]:
        monotonic = True
    else:
        monotonic = False

print("Monotonic array ", monotonic)


def isMonotonic(myArr):
    return (all(myArr[i] <= myArr[i + 1] for i in range(len(myArr) - 1)) or
            all(myArr[i] >= myArr[i + 1] for i in range(len(myArr) - 1)))


arr = array.array('i', [1, 23, 56, 85, 98])
print("is Monotonic : ", isMonotonic(arr))


# fibonacci of number
def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    return fib(n - 1) + fib(n - 2)


n = int(input("Enter a number : "))
print(fib(n))
print("Fibonacci of %d is %d ", n, fib(n))
