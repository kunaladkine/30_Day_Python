# empty tupple

empty_tuple=()
print(empty_tuple)

# empty tuple using type constructor 

tup=tuple()
print(tup)

# tuple with the intial values 
tup_1=("banana","orange,","mango")
print(tup_1)

# to print the tuple length using len() function 
print(len(tup_1))

# accessing tuple element using the indexed values 
print(tup_1[0])         #it wwill print the indexed value 0 item.


# slicing in tuple 

print(tup_1[0:1])
print(tup_1[0:2])

# changing tuple to list because we cannot change the tuple it is immutable 

lst=list(tup_1)
print(lst)      #it will current tuple to list it will shown in square brackets 

# checking item in tuple 
print('banana' in tup_1)

# joining in tuple 

tup1=('banana', 'orange', 'mango', 'lemon')
tup2=('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits=tup1+tup2
print(fruits)

# deleting a tuple  by using del() but it remove all item because it not possbile to remove 1 single item in tuple 

del tup1

