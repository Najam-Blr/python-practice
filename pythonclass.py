class MyClass:
    ''' Simple example class '''

    #class variable are shared between all the instances of class
    i = 1234

    ''' A method is a function that “belongs to” an object.
     instance obj is passed as first argument which is self obj.f() is exactly equivalent to MyClass.f(obj)'''
    def f(self):
        return 'Hello world'

    '''
    When a class defines an __init__() method, class instantiation automatically invokes __init__() 
    for the newly-created class instance
    '''
    def __init__(self):
        print(" constructor ")
        self.data = []


obj = MyClass()
print(obj.i)
print(obj.f())
print(MyClass.__doc__) #prints all docstrings in the class
print(obj.__class__) #prints name of the class for given obj
xf = obj.f # method obj and can be used later to call func
print(xf()) #calling a func using reference obj 
print(isinstance(obj, MyClass))
print(isinstance(xf, MyClass))
print(issubclass(bool, int)) #bool is sub class of int so it returns true 
