l=[1,3,4,5,6,]
print(l)
l.append(7)
print(l)

print("\n")


l2=[65,32,100,8,12]
l2.sort() #ascending
print(l2)

l2.sort(reverse=True) #descending
print(l2)

l2.reverse()
print(l2)

print(l2.index(100)) #returns the first occurence of the list item


print("\n")

l3=[1,1,3,5,6,7,8]
print(l3.count(1))


# l4=l3
# l4[0]=2
# print(l4)
# print(l3)
#by doing this both l4 and l3's 0th index will be change

l4=l3.copy();
l4[0]=2
print(l4)
print(l3)

l4.insert(1,900)
print(l4)

m=[900,1000, 2000]
l4.extend(m) #m will be printed after l4 list
print(l4)
#in above example l4 is being changed


print("\n")
n=[1,3,4,5,6,7]
o=[100,300,400]
p=n+o
print(p) #here both will be joined
