# Create an empty dictionary called dog
dog={}
# Add name, color, breed, legs, age to the dog dictionary
dog["name"]='panda'
dog["color"]='red'
dog['breed']='lamda'
dog['legs']=4
dog['age']=32
print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student={'first_name':'kunal','last_name':'adkine','gender':'male','age':23,'marital_status':'unmarried','skills':'frontend','country':'india'}

print(student)

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
print(type(student['skills']))
# Modify the skills values by adding one or two skills
student['skills']='html','css'
print(student)

# Get the dictionary keys as a list
print(['age','country','first_name','gender','last_name','marital_status','skills'])

# Get the dictionary values as a list
print(student.values())


# Delete one of the items in the dictionary
student.pop('skills')
print(student)

# Delete one of the dictionaries

del student