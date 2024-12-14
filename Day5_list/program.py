# Declare an empty list
lst=[]
print(lst)

# Declare a list with more than 5 items
lst_1=['java','python','js','html','css']
print(lst_1)

# Find the length of your list

print(len(lst_1))

# Get the first item, the middle item and the last item of the list

print(lst_1[0:2:4])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types=['kunal',23,5.6,'unmarried','maharashtra']
print(mixed_data_types)

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies=['Facebook','Google','Microsoft','Apple','IBM','oracle','Amazon']
print(it_companies)

# Print the list using print()
print(it_companies)
# Print the number of companies in the list
print(len(it_companies))
# Print the first, middle and last company
print(it_companies[0:2:4])
# Print the list after modifying one of the companies
it_companies.append('PCE')
print(it_companies)
# Add an IT company to it_companies
it_companies.insert(0,'IT')
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)

print(it_companies)


# Check if a certain company exists in the it_companies list.
does_exist='Amazon' in it_companies
print(does_exist)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)


# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
data=front_end+back_end
print(data)
