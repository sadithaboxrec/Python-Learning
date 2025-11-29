# argv- argumement vector
import sys

# try:
#     print("Hello I am" , sys.argv[1])
# except IndexError:
#     print("Too Few arguements" )


"""
if i just type python name.py i got an error
python name.py saditha it print fully
"""

# check for errors
# if len(sys.argv) < 2:
#     print("Too Few Arguments")
# elif len(sys.argv) > 2:
#     print("Too Many Arguments")
# else:
#     print("Hello I am" , sys.argv[1])


# input python name.py "sad sad"  - it will be used as one


# check for errors
if len(sys.argv) < 2:
    sys.exit("Too Few Arguments")
elif len(sys.argv) > 2:
    sys.exit("Too Many Arguments")
#print the name
print("Hello I am" , sys.argv[1])