from enum import Enum, IntEnum

class Weekdays(IntEnum):
    Saturday = 6
    Monday = 1
    Tuesday = 2
    Friday = 5
    Wednesday = 3
    Thursday = 4
    Weekend = 5 #duplicate values are not considered 

print("The week day is = {} and it's numerical value = {}".format(Weekdays.Monday.name, Weekdays.Monday.value))

for weekday in Weekdays:
    print(weekday.name, weekday.value)

print("Sorted the ENum")
for c in sorted(Weekdays):
    print(c.name, c.value)

#using map func to iterate the enum class
weekday_list = list(map(int, Weekdays))
print(weekday_list)


