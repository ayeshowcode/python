name="Ayesh"
for i in name:
    if(i=="e"):
        print("\"e\" found")
    print(i)
    
print("end of loop\n")


colors=["red", "green", "blue"]
for color in colors:
    print(color)
    
for color in colors:
   print(color)
   for i in color:
       print(i)    
   print("\n")


for k in range(10):
    print(k+1)

print("\n")
for k in range(4, 8):
    print(k+1)

print("\n")

for k in range(1,10, 2): #start, end, step (means increment by 2)
    print(k)