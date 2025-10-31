fruits = ['apple', 'strwaberry','pears','orange']

print(fruits[1:-1]) #output= ['strwaberry', 'pears'], starting from index 1, enging before last element of list i.e -1
fruits[3:3]='b'   #insert b in list at position 3, output=['apple', 'strwaberry', 'pears', 'b', 'orange']
fruits[3:]='b'   #insert at position 3 but stops there and doesn't copy further elements, outpu=['apple', 'strwaberry', 'pears', 'b']
print (fruits)

for fruit in fruits:
    if fruit=='pears':
        print ('we have pears in list')
        break
else:
   print ('sorry no pears')
    
