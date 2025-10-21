f= open ('logs.txt', 'r')

for line in f:
    print(type(line))
    print (line)
    print (line.split('- -')[0])   # just the IP address
    print (line.split(']')[0])      #IP address with date time stamp
    print (line.split(']')[0].split(' [')[1])   # date and time only (no ip)
    print(line.split(']')[0].split(' [')[1].split(':')[0])   # date only (20/Oct/2025)
    print(line.split(']')[0].split(' [')[1].split('2025')[1][1:])   # time only 
    