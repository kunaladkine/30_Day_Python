"""
syntax : 

var_name={"key:value","key2:value2}

"""

#step 1 : initialize a dict 
menu={}     #empty dict

#step 2 how to add element 

menu["Gulabjamun "]=40
print(menu)

#how to remove element from dict

del menu["Gulabjamun "]

print(menu)

menu["palakpaneer"]=49
price=menu["palakpaneer"]
print(price)

# menu.clear()
# print(menu)

print(len(menu))

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct))     #to find the len of dct 

print(dct['key2'])          #to access the index value of the dct variable data 


#adding element in dict 

dct["lan"]='html'
print(dct)

#checking key is present in dct 
print('key3' in dct)

#removing an elemnt in the dict using pop(),popitem() and del 

del dct["key2"]
print(dct)
print(dct.pop('key3'))

values=dct.values()
print(values)

