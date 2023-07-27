'''
import random
import time
# 2second

print("Dice!")
#while True:
while 1:
    value = random.randint(1, 6)
    print("dice value: %d" %value)
    time.sleep(1)
    sys.exit()
'''
#range
#start, end : input
'''
startvalue = int(input("startvalue: "))
endvalue = int(input("endvalue: "))

while startvalue <= endvalue:
    print("Count: %d" %startvalue)
    startvalue += 1
'''
'''
#use for loop
startvalue = int(input("startvalue: "))
endvalue = int(input("endvalue: "))

for start in range(startvalue, endvalue+1, 1):
    print("Count %d" % startvalue)
'''

import sys
startvalue = int(input("startvalue: "))
endvalue = int(input("endvalue: "))
SUM = 0

while startvalue <= endvalue:
    print("Count: %d" %startvalue)
    SUM += startvalue
    startvalue += 1
print(SUM)

if startvalue >= endvalue:
    print("Count: %d" %endvalue)
    SUM += endvalue
    endvalue += 1
print(SUM)
