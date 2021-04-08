strings = ['a','b','c','d']
# 4*4 = 16 bytes of storage is used

print(strings[2])

#push
strings.append('e')      # O(1)
#pop
strings.pop()
strings.pop()            # O(1)

#addfirstelement
strings.insert(0,'x')    #O(n) #because it has to reasssign the index to each element

#splice
strings.insert(2,'alien')   #O(n) #because it has to reasssign the index to each element

print(strings)

#lists/array may not be the best data structure for adding new elements
#dynamic array is like python or JS - C++ or Java are more memory efficient because
#they allocate certain quantity of memory based on the size of the array
#however,python is dynamic and the size of the array/list and their memory usage is self determine 
