# Section 7: List, Conditional, Loop, Input
# 17. List and itrat in details

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.

# This will use the n list created and split it up by the space
n = 'ali mitch robert rick john dan'
name = n.split()
print(name)

# This will use the n list created and split it up by the dot
n = 'ali.mitch.robert.rick.john.dan.mike.andrea.renee.ass'
name = n.split('.')
print(name)

# This will create a database
database = [
    ['ali', 'robert', 'ritchie', 'terri'],
    ['smith', 'rogers', 'bangino', 'gomez'],
    [23, 22, 21, 45]
]

print(database)

# This will create a database that can be inputted into and will return data based off of input
database2 = [
    ['ali', 'robert', 'ritchie', 'terri'],
    ['smith', 'rogers', 'bangino', 'gomez'],
    [23, 22, 21, 45]
]
first_name = database2[0]
family_name = database2[1]
ages = database2[2]

input_1 = str(input('Please enter user or pass: '))
if input_1 == 'f' or input_1 == 'firstname':
    print(first_name)
elif input_1 == 'l' or input_1 == 'lastname':
    print(family_name)
elif input_1 == 'a' or input_1 == 'ages':
    print(ages)
else:
    print('Please enter the correct info!')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
