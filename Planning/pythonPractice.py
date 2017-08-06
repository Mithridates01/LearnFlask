# This is a single line comment


print(10 / 2)

# division is allways a float
# True & False capitalized
# concat strings with spaces
# string interpolation "{0} pizza".format("pepperoni")


input_string_var = input("Enter Data: ")

print(input_string_var)

# accessing unassigned vars is exception

# List
listy = ["original"]
listy2 = [1,2,3,"hello", listy]
print(listy2)
print

class Oven(object):
  """docstring for Oven"""
  def __init__(self, arg):
    super(Oven, self).__init__()
    self.arg = arg
    
  def function(self):
    pass


# Practice 
# Python 3.6.2 (default, Jul 17 2017, 16:44:45) 
# [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> 3 / 3
# 1.0
# >>> 3 / 2
# 1.5
# >>> 10 // 5
# 2
# >>> 10 / 5
# 2.0
# >>> 2 ** 3
# 8
# >>> 2 ** 3.0
# 8.0
# >>> not true
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'true' is not defined
# >>> not True
# False
# >>> not False
# True
# >>> True and False
# False
# >>> False and False
# False
# >>> True and True
# True
# >>> 0 == False
# True
# >>> 1 == False
# False
# >>> a = "pizza"
# >>> a = b
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'b' is not defined
# >>> b = a
# >>> a is b
# True
# >>> a == b
# True
# >>> "This can be concat" "inated"
# 'This can be concatinated'
# >>> "This can be concat" + "inated"
# 'This can be concatinated'
# >>> "String"
# 'String'
# >>> "String"[0]
# 'S'
# >>> "String"[-1]
# 'g'
# >>> "String"[2]
# 'r'
# >>> variable = "String"
# >>> len(var
# variable  vars(     
# >>> len(variable)
# 6
# >>> variable " concat?"
#   File "<stdin>", line 1
#     variable " concat?"
#                       ^
# SyntaxError: invalid syntax
# >>> variable + " concat?"
# 'String concat?'
# >>> "{} is {} and {} is not {}".format("false","false","false","true")
# 'false is false and false is not true'
# >>> "{0} is {0} and {0} is not {1}".format("false","true")
# 'false is false and false is not true'
# >>> falseVar = false
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'false' is not defined
# >>> falseVar = False
# >>> falseStrVar = "false"
# >>> "{0} is {0} and {0} is not {1}".format(falseVar,"true")
# 'False is False and False is not true'
# >>> "{0} is {0} and {0} is not {1}".format(falseStrVar,"true")
# 'false is false and false is not true'
# >>> None
# >>> None
# >>> None is None
# True
# >>> None is Non
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'Non' is not defined
# >>> None is "none
#   File "<stdin>", line 1
#     None is "none
#                 ^
# SyntaxError: EOL while scanning string literal
# >>> "
#   File "<stdin>", line 1
#     "
#     ^
# SyntaxError: EOL while scanning string literal
# >>> None is "none"
# False
# >>> None == "none"
# False
# >>> None == None
# True
# >>> exit()
# Joshuas-MacBook-Pro:~/Desktop/Interviews/LinksProject/Planning (master) $ python3 pythonPractice.py 
# 5.0
# Joshuas-MacBook-Pro:~/Desktop/Interviews/LinksProject/Planning (master) $ 

