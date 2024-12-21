#A for keyword is used to make a for loop, similar with other programming languages, but with some syntax differences. Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

"""
syntax : 
for interator in lst:
    code goes here
"""

numbers = [0,1,2,3,4,5]
for number in numbers:
    print(number)


name="kunal"
for i in name:
    print(i)

for i in range(len(name)):
    print(name[i])
    
#range function 

lst=list(range(5))
print(lst)

lst2=list(range(0,11,2))
print(lst2)
