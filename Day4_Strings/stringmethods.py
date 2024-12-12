challenge='we are learning python'

#method 1 capitalize()

print(challenge.capitalize())   #first letter will be capitalize 
print(challenge.count('y'))     #it will count the y letter 
print(challenge.count('a'))
print(challenge.endswith('on'))
print(challenge.find('a'))      #this find() method will find the letter a 
print(challenge.replace('python', 'coding'))


web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result)