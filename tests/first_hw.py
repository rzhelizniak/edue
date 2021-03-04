
# Task1
number_list = [1, 0, -52, 3, 5, -8, 13, 21, 34, -55, 89]

new_list =  []
for i in number_list:
    if i<=5:
        new_list.append(i)
    else:
        pass

print(new_list)

# Task 2
numbers_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
numbers_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def similar(list1, list2):
    new_list = []
    for i in list2:
        if i in list1:
            new_list.append(i)
        else:
            pass
    print(new_list)


similar(numbers_1, numbers_2)

# Task 3
my_list = [1, 2, 3, 4, 5, 6]


def first_last(list):
    first_one = list[0]
    last_one = list[-1]
    print(first_one, last_one)


first_last(my_list)

# Task 4
my_list = [1, 2, 3, 4, 5, 6]


def first_last(list):
    first_one = list[0]
    last_one = list[-1]
    print(first_one, last_one)


first_last(my_list)

# Task 5
string_1 = "Hello, it`s simple string"
symbol_1 = "s"


def count_1(random_string, symbol):
    quantity = random_string.count(symbol)
    print(quantity)


count_1(string_1, symbol_1)

# Task 6
string_1 = "Automation sometimes helps project and sometimes does not."


def special_output(random_string):
    new_list = random_string.split()
    longest = ""
    most_used = new_list[0]
    result_count = 0
    for i in new_list:
        current_most_used = new_list.count(i)
        if current_most_used > result_count:
            counter = current_most_used
            most_used = i
        if len(i) > len(longest):
            longest = i
    print(most_used)
    print(longest)


special_output(string_1)

# Task 7
string_1 = "Exception breakpoints: suspend the program when Exception or its subclasses are thrown.In PyCharm, you can set breakpoints for Python exceptions."


def change_spaces_on_smt(random_string):
    new_string = random_string.replace(" ", "_")
    print(new_string)


change_spaces_on_smt(string_1)

# Task 8
string_1 = "Hello, it`s simple string"
symbol_1 = "s"


def count_1(random_string, symbol):
    quantity = random_string.count(symbol)
    print(quantity)


count_1(string_1, symbol_1)


# Task 9
def check_palindrom(word):
    drow = word[::-1]
    if drow == word:
        print(word)
    else:
        print("Non-palindrom")


check_palindrom("rotoras")