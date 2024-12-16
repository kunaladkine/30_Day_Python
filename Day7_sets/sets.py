#set is a collection of  same data object 

#it is write in culry brackets {}
#separate by commas  , it is unchangeable 

s={2,4,2,5}
print(s)            #here the 2 will be removed because it same data 

#creating a empty set 
st=set()
st_1={"banana","orange","mango","lemon"}
print(st)
print(st_1)

#Methods in Sets
#Getting Sets length 

print(len(st))
print(len(st_1))        #it will print the length of set itmes present in the data 

#to check item in set like present in the set 

print("mango" in st_1)          #it will check the set 

#adding item in set using add()
st_1.add("apple")
print(st_1)     #it will add apple like set 

st_1.update(["juice"])
print(st_1)     #it will add juice in the set 

#removing item from set using the remove() and pop() function 

st_1.remove("mango")
print(st_1)

st_1.pop()
print(st_1)

#clearing set 

st_1.clear()
print(st_1)

#deleting set 
# del st_1
# print(st_1)

#converting list to set 

fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits=set(fruits)
print(fruits)

#joining set using union() method

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print(st3)

#intersection item
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.intersection(dragon))      #it will shows the same value in the data type 


