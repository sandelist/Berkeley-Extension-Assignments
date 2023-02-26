# 1. Building a simple Rectangle class

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return (self.length + self.width)*2

    def area(self):
        return self.length*self.width

# Using the Rectangle class
rectangle_test = Rectangle(8, 10)

print('Perimeter of rectangle :', rectangle_test.perimeter())
print('Area of rectangle :', rectangle_test.area())

# 2. Building a class called Ulist

from collections import UserList

class Ulist(UserList):
    # overriding the __add__ method
    def __add__(self, other):
        new_list = Ulist(self.data)

        for item in other:
            if item not in new_list:
                new_list.append(item)

        return new_list
    
    # overriding the append method 
    def append(self, item):

        if item not in self:
            super().append(item)
    
    # overriding the extend method
    def extend(self, other):

        for item in other:

            if item not in self:
                super().append(item)

# Using the Ulist class

test_list = Ulist([4, 5])

test_list.append(5)

test_list.append(6)

# This list should only have one 5 instead of two
print('The list after appending 5 and 6: ', test_list)

# This should only have add 7 to the list, ignoring 5 and 6 because they are already in the list

test_list.extend([5,6,7])

print('The list after extending by the list made of 5, 6 and 7: ', test_list)

# This should only have add 8 and 9 to the list, ignoring 7 because it is already in the list

test_list_b = Ulist([7, 8, 9])
new_list = test_list + test_list_b

print('The list after it has added the test list 2: ', new_list)


# 3. Building a class called AnyCaseDict

from collections import UserDict

class AnyCaseDict(UserDict):
    
    def __init__(self, data=None):
        super().__init__()
        if data:
            self.update(data)

    def __setitem__(self, key, value):
        self.data[key.lower()] = value

    def __getitem__(self, key):
        return self.data[key.lower()]


# Using the AnyCaseDict class 

test_dict = AnyCaseDict()

test_dict["Car"] = "Tesla Model 3"
test_dict["CAR"] = "Tesla Model 3"
test_dict["CAr"] = "Tesla Model 3"

print(test_dict)