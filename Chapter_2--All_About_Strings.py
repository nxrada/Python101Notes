# Creating strings in the 3 types of ways: single parentheses, double parentheses, & multi-line strings
my_string = "Welcome to Python!"
another_string = 'Python is cool!'
a_long_string = '''I bonked
your
mum hahah ''' 
print(my_string + "\n" + another_string + "\n" + a_long_string + "\n")

# Casting int vars into string datatype
my_number = 123
my_casted_num = str(my_number)
print (my_casted_num+ "\n")

# Concatenation of strings
string_one = "My dog ate"
string_two = " my homework!"
string_three = string_one + string_two
print (string_one + "\n" + string_two + "\n" + string_three + "\n")

# String method example: uppercase. Use dir() method to determine all possible methods of a given datatype
print(my_string.upper() + "\n")
dir(my_string)


# String slicing
print(my_string[0])
print(my_string[0:1])
print(my_string[0:2])
print(my_string[0:3])
print(my_string[0:4])
print(my_string[0:5])
print(my_string[0:6])
print(my_string[0:7])
print(my_string[0:6])
print(my_string[0:5])
print(my_string[0:4])
print(my_string[0:2])
print(my_string[0:1])
print(my_string[0] + "\n")

# String formatting (ye olde way)
my_string = "I like %s" % "Python"
print(my_string + "\n")
var = "cookies"
newString = "I like %s" % var
print(newString + "\n")
another_string = "I like %s and %s" % ("Python", var)
print(another_string + "\n")
my_string ="%i + %i = %i" % (1, 2, 3)
print(my_string + "\n")
float_string = "%f" % (1.23)
print(float_string + "\n")
float_string2 = "%.2f" % (1.23)
print(float_string2 + "\n")
float_string3 = "%.2f" % (1.237)
print(float_string3 + "\n")

# String formatting (new methodolgy)
# Based on {"key":"value"} protocol
print("%(lang)s is fun!" % {"lang":"Python"} + "\n")
print("%(value)s %(value)s %(value)s !" % {"value":"SPAM"} + "\n")
print("%(x)i + %(y)i = %(z)i" % {"x":1, "y":2, "z":3} + "\n")
print("Python is as simple as {0}, {1}, {2}".format("a", "b", "c") + "\n")
xy = {"x":0, "y":10}
print("Graph a point at where x={x} and y={y}".format(**xy))

