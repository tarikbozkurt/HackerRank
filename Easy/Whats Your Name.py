#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    if len(first) <=10 and len(last)<=10:
        my_str="Hello {} {}! You just delved into python.".format(first,last)
    return print(my_str)

