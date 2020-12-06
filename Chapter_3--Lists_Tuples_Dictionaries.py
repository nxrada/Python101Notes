# Lists:
# Basically an array.
# Two ways to write them:
my_list = []
other_list = list()

# Adding elements to a list:
my_list = [1, 2, 3]
my_list2 = ["a", "b", "c"]
my_list3 = ["a", 1, "Python", 5]
my_list3

# Creating nested list:
my_nested_list = [my_list, my_list2]

# Combining lists via the extend method:
combo_list = []
one_list = [4, 5]
combo_list.extend(one_list)
combo_list

# Combining lists via addition:
my_list = [1, 2, 3]
my_list2 = ["a", "b", "c"]
combo_list = my_list + my_list2
combo_list

# Sorting lists:
alpha_list = [8, 4, 42, 16, 23, 15]
alpha_list.sort()
alpha_list

# Another sorting example:
# Demonstrates that the sort() method sorts the list in-place. Returns 'None,' which is equivalent to 'Null.'
# To reiterate, you cannot assign the value of a sort()-method'd list.
alpha_list = [8, 4, 42, 16, 23, 15]
sorted_list =  alpha_list.sort()
print(sorted_list)

# Slicing lists:
alpha_list[0:3]

# Tuples:
# Similar to list, but made with parentheses.
# Difference is: tuples are immutable.
# Tuples cannot be sorted.
my_tuple = (1, 2, 3, 4, 5)
another_tuple = tuple()
my_tuple[0:3]
abc = tuple([1, 2, 3])  # Ex. of casting a list to tuple.

# Dictionaries:
# Basically a hash table or hash mapping.
# An unordered set of key:value paris.
# Indexed with keys, which can be any immutable type (e.g. a string or number). Keys must be unique.
# A few ways to write them:
my_dict = {}
another_dict = dict()
a_third_dict = {"one":1, "two":2, "three":3}
a_third_dict

# How to access a  value:
a_third_dict["one"]
my_dict = {"name":"Mike", "address":"123 Coomer St."}
my_dict["name"]

# How to tell if a key is in a dictionary.
# Use 'in' keyword to check a dictionary for a specific key. Returns boolean value.
"name" in my_dict
"state" in my_dict

# How to get a list of all keys in a dict
# Use keys() method to get a list of keys in a dictionary. 
my_dict.keys()
