#it is use for to write the condtion in one line 

a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')
    
#this code will write in shorthand like this 
b=-5
print("A is greater") if b>0 else print("A is less than ")