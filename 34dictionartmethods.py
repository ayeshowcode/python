ep1={122:45, 123: 89, 567: 69, 670: 69}
ep2={222: 67, 566: 90}
ep1.update(ep2) #same as set but ordered
print(ep1) 

# ep1.clear() empty krdega
# print(ep1)

print("\n")
ep1.pop(123) 
print(ep1)

ep1.popitem() #pops the element from last
print(ep1)

# del ep1
# print(ep1)  error

del ep1[122]
print(ep1)