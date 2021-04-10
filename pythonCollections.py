

from collections import Counter, defaultdict, OrderedDict, deque, namedtuple, ChainMap
list = [1,2,3,4,1,2,6,7,3,8,1]
cnt = Counter(list)
print(cnt)
print(cnt[1])
print(cnt.elements())

''' 
Output
Counter({1: 3, 2: 2, 3: 2, 4: 1, 6: 1, 7: 1, 8: 1})
3
<itertools.chain object at 0x00000217F1643B88>
'''

for i in cnt.elements():
    print(i)
'''
Output:
loops through all the elements  1
1
1
2
2
3
3
4
6
7
8
'''

print(cnt.most_common())
#[(1, 3), (2, 2), (3, 2), (4, 1), (6, 1), (7, 1), (8, 1)]

for i,j in cnt.most_common():
    print(i, j)
    
"""
Ouputs: 
1 3
2 2
3 2
4 1
6 1
7 1
8 1
"""

cnt = Counter({1:3, 2:4})
deduct = {1:1, 2:2}
cnt.subtract(deduct)
print(cnt)
# Op: Counter({1: 2, 2: 2})

nums = defaultdict(int)
nums['one'] = 1
nums['two'] = 2
print(nums['three']) #it prints 0 instead of throwing key error

nums = defaultdict(int)
names_list = "Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Smith".split()
for names in names_list:
    nums[names] = nums[names]+1

for key, val in nums.items():
    print(key, val)
'''
Output:
Mike 5
John 3
Anna 2
Britney 1
Smith 2
'''


nums = OrderedDict()
nums['one'] = 1
nums['two'] = 2
nums['three'] = 3
nums['four'] = 4

for key, val in nums.items():
    print(key, val)

'''
Output:
one 1
two 2
three 3
four 4
'''

list1 = ["a", "b", "c"]
deq = deque(list1)
print(deq)

deq.append(["e", "f"])
deq.appendleft('g')
deq.append('h')
print(deq)

deq.pop()
print(deq)

deq.popleft()
print(deq)
print(deq.count("a"))


'''
Output:
deque(['a', 'b', 'c'])
deque(['g', 'a', 'b', 'c', ['e', 'f'], 'h'])
deque(['g', 'a', 'b', 'c', ['e', 'f']])
deque(['a', 'b', 'c', ['e', 'f']])
1
'''

dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'c' : 3, 'b' : 4 }
chain_map = ChainMap(dict1, dict2)

print(chain_map.maps)
for keys in (chain_map.keys()):
    print(keys)

#[{'a': 1, 'b': 2}, {'c': 3, 'b': 4}]
'''
Output:
c
b
a

'''
for val in (chain_map.values()):
    print(val)
'''
Output:
3
2
1
'''
dict3 = {'e' : 5, 'f' : 6}
new_chain_map = chain_map.new_child(dict3)
print(new_chain_map)

#ChainMap({'e': 5, 'f': 6}, {'a': 1, 'b': 2}, {'c': 3, 'b': 4})
