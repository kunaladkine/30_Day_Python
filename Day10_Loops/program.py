#Iterate 0 to 10 using for loop, do the same using while loop.
count =0
while count <10:
    count=count+1
    print(count)
    
# Iterate 10 to 0 using for loop, do the same using while loop.

# data=0
# while data<10:
#     data=data+1
#     print(data)
#     if data==0:
#         print(data)
    
#Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######
  
for i in range(1,8):
    print("#"*i)
    
# Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
for i in range(5):
    print("#"*7)
    
# Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(0,100,2):
    print(i)