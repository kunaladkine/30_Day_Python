#Q1. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

# #program :- 
# length=int(input("Enter The Length of rectangle :"))
# width=int(input("Enter The width of rectangle :"))

# area=length*width
# print("The Area of Rectangle is :",area)

# perimeter=2*(length+width)
# print("The perimeter is ",perimeter)

#Q2. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

#program : 
# pi=3.14
# r=int(input("Enter the radius:"))
# area=pi*r*r
# print("The radius of circle is ",area)
# c=2*pi*r
# print("Circumference is :",c)


#Q3.  Find the length of 'python' and 'dragon' and make a falsy comparison statement.

# print((len("python")!=len("dragon")))

#Q4.  Use and operator to check if 'on' is found in both 'python' and 'dragon'

x="python"
y="dragon"
if "on" in x and y:
    print("The on is in x and y ")
else:
    print("the on is not in x and y")
    
#Q5.  I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

z= "I hope this course is not full of jargon"
if "jargon" in z:
    print("It is in z ")

#Q6. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

base=int(input("Enter Base : "))
height=int(input("Enter Height:"))
area=0.5*base*height
print("area of triangle is : ",area)

