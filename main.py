# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
list_1 = ['mike', 'alan', 'john', 'cary']

list_2 = ['barry', 'chuck', 'rick ross', 'larry']

a = list_1[0]
b = list_1[2]
c = list_1[3]
d = list_2[2]
a = a.title()
b = b.title()
c = c.title()
d = d.title()
# list_1.append('roger') adds 'roger' to list_1
list_1.append('roger')
# list_2.insert(2, 'terri') will insert 'terri' in the 2 spot of list_2
list_2.insert(2, 'terri')
h = list_2[2]
h = h.title()
# list_2.remove('larry') will remove larry from list_2
list_2.remove('larry')
# e = (len(list_1)) creates a count of List_1
e = (len(list_1))
f = (len(list_2))
g = e + f


def print_hi(name):
    # name = name.title() will capitalize the first letters in each word
    name = name.title()
    # Use a breakpoint in the code line below to debug your script.
    print(f'Welcome, {name}, {a}, {d}, {h} and all {g} of your friends!')  # Press Ctrl+F8 to toggle the breakpoint.
    print(list_1)
    print(list_2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('xavier')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
