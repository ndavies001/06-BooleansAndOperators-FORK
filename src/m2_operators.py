txt = "The quick brown fox jumps over the lazy dog."
t1 = "fox"
t2 = "cat"

###############################################################################
# DONE: 1. (6 pts)
#
#   Write each of the functions below (each that takes two parameters and uses
#   the appropriate operator from the reading) that simply returns the boolean
#   evaluation of those two parameters:
#
#   equal()
#   not_equal()
#   greater_than()
#   less_than()
#   greater_than_or_equal_to()
#   less_than_or_equal_to()
#
#   Now write a line of code for each one using numbers for the parameters that
#   would cause each function to return True. 
#   
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def equal(a, b):
    return a == b
def not_equal(a, b):
    return a != b
def greater_than(a, b):
    return a > b
def less_than(a, b):
    return a < b
def greater_than_or_equal_to(a, b):
    return a >= b
def less_than_or_equal_to(a, b):
    return a <= b
print(equal(5, 5))
print(not_equal(5, 3)) 
print(greater_than(6, 4))  
print(less_than(2, 4))  
print(greater_than_or_equal_to(5, 5))  
print(less_than_or_equal_to(3, 5)) 
###############################################################################
# TODO: 2. (2 pts)
#
#   Write a line of code that returns True if the string
#       t1 (defined above)
#   is contained in the string
#       txt (also defined above)
#   and prints the result.
#
#   Write another line of code that returns True if the string
#       t2
#   is contained in the string
#       txt
#   and prints the result.
#
#   Run your code. Does it return what you expect?
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
print(t1 in txt) 
print(t2 in txt)
###############################################################################
# DONE: 3. (1 pt)
#
#   Now, write a line of code that returns True if the string
#       t1
#   is *not* the same thing as
#       t2
#   and prints the result
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
print(bool(t1 != t2))