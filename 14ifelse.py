a=int(input("Enter your age: "))
if(a>=18):
    print("you can drive")
else:
    print("you cannot drive")
    
    
    
b=int(input("Enter the number: "))
if(b>0):
    print("number is positive")
elif(b<0):
    print("number is negative")
else:
    print("number is zero")
    
    
    
# Given numbers
a = 1
b = 2
c = 3

# Nested if-else to find the maximum number
if a >= b:
    if a >= c:
        max_num = a
    else:
        max_num = c
else:
    if b >= c:
        max_num = b
    else:
        max_num = c

print("The maximum number is:", max_num)
