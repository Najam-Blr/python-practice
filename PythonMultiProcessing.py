from multiprocessing import Pool
import time

count = 50000000

def countdown(n):
    while n > 0:
       # print(n)
        n -= 1

if __name__ == "__main__":
    pool = Pool(processes=2)
    start = time.time()
    r1 = pool.apply_async(countdown, [count//2])
    r2 = pool.apply_async(countdown, [count//2])
    pool.close()
    pool.join()
    end = time.time()
    print("TIme taken is : ", end-start)


import multiprocessing

def print_square(num):
    num = num * num
    print(num)


if __name__ == "__main__":
    p1= multiprocessing.Process(target=print_square, args=(5,))
    p2 = multiprocessing.Process(target=print_square, args=(10,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()


import multiprocessing

def f(x):
    print(x)
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1,2,3,4,5]))

    p1 = multiprocessing.Process(target=f, args=(2,))
    p1.start()
    p1.join()




'''
def remove_duplicates(list1):
    list2 = []
    for item in list1:
        if item not in list2:
            list2.append(item)
    return list2

list1 = [1,2,3,4,3,4,6]
print(remove_duplicates(list1))


str = " hi how are you"
strlen = len(str)
print(str[::-1])

reversed = list(reversed(str))
print(reversed)
'''


import os
import time
import multiprocessing

def func(Val):
    print("In func: %s",Val)
    time.sleep(2)
    print("Is thread alive: ", os.getpid(), os.getppid()
          )

if __name__ == "__main__":
    p = multiprocessing.Process(target=func, name="mythread", args=("Thread1",))
    print("Is thread alive: ", p.is_alive())
    time.sleep(1)
    p.start()
    print("Is thread alive: ", p.is_alive())
    p.join()

    p.terminate()

    print("Core count", multiprocessing.cpu_count())

'''
multiprocessing module provides Array and Value objects to share data between processes.
Array: a ctypes array allocated from shared memory.
Value: a ctypes object allocated from shared memory.
'''

'''
marksheet = []
for _ in range(0, int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]

print(second_highest)
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))


import re
for test_str in ['555-1201', 'ILL-EGAL']:
    if re.match(r'^\d{3}-\d{4}$', test_str):
        print(test_str, "is valid number")
    else:
        print(test_str, "is not a valid num")

prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {
    'apple': 1,
    'banana': 6
}
grocery_bill = sum(prices[fruit]*my_purchase[fruit] for fruit in my_purchase)
print(grocery_bill)

'''