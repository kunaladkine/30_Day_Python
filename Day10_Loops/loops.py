#Life is full of routines. In programming we also do lots of repetitive tasks. In order to handle repetitive task programming languages use loops. Python programming language also provides the following types of two loops:

#while loop 
#for loop

"""
syntax : 

while condition:
    code goes here
"""
i=0
while i<5:
    print("hello")
    i=i+1
    
count = 7
while count<5:
    print(count)
    count=count+1
else:
    print(count)
    
#break and continue 

count =0
while count<5:
    print(count)
    count=count+1
    if count==3:
        break
    
count = 0
while count<5:
    print(count)
    if count ==3:
        count = count +1
        continue
    print(count)
    count=count+1
    
