s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2))
s1.union(s2)
print(s1) #this will print s1 but not union  because the above line is only used with print it doesnt updates

s1.update(s2) #does same thing as
print(s1, s2)

cities= {"tokyo", "madrid", "berlin", "delhi"}
cities2={"tokyo", "seoul", "kabul", "madrid"}
cities3=cities.union(cities2)
print(cities3)
cities4=cities.intersection(cities2)
print(cities4)

cities5=cities.symmetric_difference(cities2)
print(cities5)

cities6=cities.difference(cities2)
print(cities6)

cities7=cities.isdisjoint(cities2)
print(cities7)

cities8=cities.issuperset(cities2)
print(cities8) 