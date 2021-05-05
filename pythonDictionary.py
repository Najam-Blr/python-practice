from typing import Dict, Any


class myDict(dict):

    mydict: Dict[Any, Any]

    def __init__(self):
        self.mydict = dict()

    def add(self, key, value):
        self.mydict[key] = value

    def print(self):
        for key, val in self.mydict.items():
            print(key, ":", val)


dict_obj = myDict()
dict_obj.add("Name", "Najam")
dict_obj.add("age", '32')

print(dict_obj.mydict)
print(dict_obj.print())

#using subscript notation
dict_obj.mydict["salary"] = "10000"
print(dict_obj.print())

#using update method
dict_obj.mydict.update({"address": " 200 jhonson dr, framingham, MA"})
print(dict_obj.print())


dict = { {'a': 1, 'b': 2}, {'d':4, 'e':5}}

# will create a new dictionary
new_dict = {**dict, **{'c': 3}}
print(new_dict)

#to get keys
for key in new_dict.keys():
    print(key)

#to get only values
for val in new_dict.values():
    print(val)
print(new_dict[2][0])