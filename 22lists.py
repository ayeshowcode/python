marks=[3,4,5, "ayesh", True]
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

if "ayesh" in marks:
    print("yes")
else:
    print("No")



print("\n\n")


if "aye" in "ayesh":
    print("aye is present in ayesh")
else:
    print("aye is not present in ayesh")
    
print("\n\n")

    
print(marks[:])
print(marks[0:-3])
print(marks[0::2])


lst=[i*i for i in range(4)]
print(lst)

lst=[i*i for i in range(10) if (i%2==0)]
print(lst)

lst=[i*i for i in range(10) if (i%2)]
print(lst)