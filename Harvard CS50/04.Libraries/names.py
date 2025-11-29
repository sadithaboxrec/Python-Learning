import sys

"""
from nbformat.v4 import output_from_msg

if len(sys.argv) <2:
    sys.exit("Too Few Arguments")

for arg in sys.argv:
    print(arg)
    
    
#### output
names.py
james
John
boxing  

// 
"""
# let's try to remove unnecessary file name
# slices
if len(sys.argv) <2:
    sys.exit("Too Few Arguments")

for arg in sys.argv[1:]:
    print("Hello",arg)