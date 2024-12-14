# list can be create by the list() built in function and the [] square brackets 

lst=[]
print(lst)      #empty list create 

list=list()
print(list)     #we can get he output like the empty square brackets 

fruits=['banana','orange','mango','lemon']
lang=['html','css','js','java']

print("the fruits are",fruits)
print("the languages are",lang)
print("no of fruits are : ",len(fruits))        #here we use the len() built in funciton to print the length of the list 
print("no of languages : ",len(lang))

#list value can be get by the indexing 
print(fruits[1])
print(lang[2])

first_lang,second_lang,third_lang,fourth_lang=lang
print(first_lang)       #here we can giving name and indexing to the list item 
print(second_lang)
print(third_lang)
print(fourth_lang)

first_fruit,second_fruit,*rest=fruits       #we use rest to uncpack the list remainging 
print(first_fruit)
print(second_fruit)
print(*rest)            #here we can print the remaining list by *rest symbol 

#modifying and updating the original index value in the list

fruits[2]='avocado'
print(fruits)           #here we can get the updateed list new with index value 2 avocado 

#cheking the given index value  is present in the list using the 'in ' operator 

does_exist='banana' in fruits
print(does_exist)           #here we can get the value true if present and false if not present 

#we can add item in list by using the append method to update and the value will get in list at the end.

fruits.append('cherry')
fruits.append('lime')

print(fruits)           #we get the updateed list in the new fruits 

#to insert a index between two 
fruits.insert(2, 'apple')       #
print(fruits)               #we get the index 2 position apple.

#to remove list item using remove() and pop() del

fruits.remove('banana')
fruits.pop(2)
del fruits[0]
print(fruits)

combo=fruits+lang           #list concatination 
print(combo)


print(fruits.count('banana'))           #here we can count the no of item that we insert in list using count() method



