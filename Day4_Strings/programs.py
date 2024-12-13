# Q.1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

# program : 
space=' '
print('Thirty'+space+'Days'+space+'of'+space+'Python')

code='Thirty Days of Python'
print(code)

# Q.2 Declare a variable named company and assign it to an initial value "Coding For All".

company='Coding For All'
print(company)

# Q.3 Print the length of the company string using len() method and print().
print(len(company))

# Q.4 Change all the characters to uppercase letters using upper() method.

print(company.upper())

# Q.5. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

print(company.capitalize())
print(company.title())
print(company.swapcase())

# Q.6 Check if Coding For All string contains a word Coding using the method index, find or other methods.

if 'Coding' in company:
    print("It is Available")
    print(company.find('Coding'))       #the find method is used in that 
    
# Q.7 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

data="Facebook Google Microsoft Apple IBM Oracle Amazon"
print(data.split())

# Q.8 What is the character at index 0 in the string Coding For All.

print(company[0]) 

#Q.9 . Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.

print('I am enjoying this cchallenge\nI just wonder what is next')

# Q.10 Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki

print('Name\tAge\tCountry\tCity')
print('Asabench\t250\tFinland\tHelsinki')

# Q.11 Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

a=8
b=6

print(f'{a}\t+\t{b}=\t{a+b}')
print(f'{a}\t-\t{b}=\t{a-b}')
print(f'{a}\t*\t{b}=\t{a*b}')
print(f'{a}\t/\t{b}=\t{a/b}')
print(f'{a}\t%\t{b}=\t{a%b}')
print(f'{a}\t//\t{b}=\t{a//b}')
print(f'{a}\t**\t{b}={a**b}')