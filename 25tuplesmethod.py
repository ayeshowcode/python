countries=["spain", "italy", "india", "England", "Germany"]
temp= list(countries)
temp.append("Russia") #add
temp.pop(3) #remove
temp[2] = "Finland" #change
countries = tuple(temp)
print(countries)
print("\n\n")


countries1 = ("pakistan", "Afghanistan", "bangladesh", "srilanka")
countries2 = ("vietnam", "india", "Germany")
countries3 = countries1 + countries2
print(countries3)
print("\n\n")


tuple1 = (1,3,5,1,7,8,9,1)
print(tuple1.count(1))
print(tuple1)
print("\n\n")
print(tuple1.index(1)) #returns the first occurence of the element here it returns zero because 1 is appearing at 0th index

#if we want to slice first and only find the element in that portion
print(tuple1.index(1, 2, 6)) #returns 3 because ....

