#Creating a string 

letter='p'
print(letter)       #print the string
print(len(letter))  #print the length of string

#string concatenation

first_name='abhi'
last_name='shek'    
space=' '       #it give the space between two words 
name=first_name + space + last_name
print(name)     #it will be concatinate the both name in name.
print(len(first_name))
print(len(last_name))
print(len(name))

#escape sequence charactieer 

#\n for use the new line 
# \t use for the 8 tabs
# \\ usse for the back slash
# \' use for sing single quote 
# \" use for the double quote "

a='the is first line\n this is second line '
print(a)
b="day\tdate"
print(b)
print("this is the \'line quotes\'")
print('is use for \" double quote \"')


#string formating 
x=5
y=10

print('{}+{}={}'.format(x,y,x+y))
print('{}-{}={}'.format(x,y,x-y))

#strinig interpolation /f-string

print(f'{x}+{y}={x+y}')
print(f'{x}-{y}={x-y}')


#string indexing and slicing 

lang="python"
print(len(lang))
print(lang[3])
print(lang[4])
print(lang[1:3])



