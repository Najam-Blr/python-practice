list1 = ['orange', 'apple', 'banana', ' kiwi']

def itemExistInList(list1= list1, fruitname='unknown'):
    for item in list1:
        '''
        # 1. Using == operator 
        if item == fruitname:
        '''
        # 2. using in operator
        if fruitname in list1:
            print('item in list')
            return
    else:
        print('item not in list')



itemExistInList(list1, fruitname='strawberries')
itemExistInList(list1, fruitname='banana')

#using filter with lambda function 
elems = list(filter(lambda x: 'banana' in x, list1))
print(elems)

#by using count() func 
if list1.count('banana') > 0:
    print('item in list')

#using any on list1
if (any( element in 'banana' for element in list1 ) ):
    print('item in list')
