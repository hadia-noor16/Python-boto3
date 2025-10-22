# .count example
# in this example you don't want any underscore in the input string
name = input('Please type something: ')    

if name.count('_')>0:
    print ('not good, no underscore please')
else:
    print('you are good to go')

my="hello"
print (my.count('l'))    # output 2 because l appears twice
    

# .find example
# also user strip method for string, .find method counts what index it finds the string first

name2= input ('Type another string: ').strip()    ## input: ndjjandkfnkdfaaa

if name2.find('a'):
    print (name2.find('a'))      #output = 4
    
else:
    print ('doesn\'t contain a')