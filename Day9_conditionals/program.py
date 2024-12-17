# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.

# age=int(input("Enter Your Age:"))
# if age>=18:
#     print("You are old enough to drive")
# else:
#     print("You Need to wait for the year ")
    


#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.

# a=int(input("Enter a number one:"))
# b=int(input("Entre a number two:"))
# if a>b:
#     print(a,"is greater than",b)
# else:
#     print(b,"is greater than",a)
    
#Write a code which gives grade to students according to theirs scores:

# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

score=int(input("Enter Your Score:"))
if score>=80 and score<=100:
    print("A")
elif score>=70 and score<=89:
    print("B")
elif score>=60 and score<=69:
    print("C")
elif score>=50 and score<=59:
    print("D")
else:
    print("F")