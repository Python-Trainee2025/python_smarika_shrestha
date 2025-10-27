#list
a=[1,2,3,3]
#ordered, mutable, allows duplicates

print(a[::-1]) # reverse the list but does not affect the actual list
print(a)
a.reverse()    #reverse the actual list
print(a)
#add elements
a.append(10)   #add at the end
print(a)
a.insert(0,20)  #insert at ceratain position
print(a)
a[1]='Hello' # replace at certain index
print(a)

#sorting
#sort and sorted
#sort changes the original list
#sorted doesnot chnage the original list


#concatnation
#repetation
#memebership check
#remove , removes the first instance of that particular thing
#pop
#del is used to remove item at that index
