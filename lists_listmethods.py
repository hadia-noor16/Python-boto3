fruits = ['apple', 'banana', 'pear', 'orange', 'mango']

print (fruits[2])    #output pear



fruits.append('strawberry')
print(fruits)    # output= ['apple', 'banana', 'pear', 'orange', 'mango', 'strawberry']



fruits.insert(1,'pineapple')
print(fruits)   # inserts pineapple at first index -> ['apple', 'pineapple', 'banana', 'pear', 'orange', 'mango', 'strawberry']


print(fruits[-1])   # prints last item of the list

#swapping banana (third item) with apple(first item)

print(fruits)  # apple is first, banana is third
temp=fruits[0]
fruits[0]= fruits[2]
fruits[2]= temp
print(fruits)  #banana is first, apple is thrid in the list 


#easier way to swap values
fruits[0],fruits[2]= fruits[2],fruits[0]
print (fruits)   #['apple', 'pineapple', 'banana', 'pear', 'orange', 'mango', 'strawberry']


ages = [25, 30, 22, 35, 28]

ages.reverse()   # reverses the order of the list. , output= [28, 35, 22, 30, 25]
print(ages)    

ages.sort()  # sorts the list in ascending order
print(ages)  # prints the sorted list

ages.reverse()   # since the list was sorted from smallest to biggest number, reversing it will give you biggest to smallest
print(ages)
