for i in range(5):
    print(i)
else:
    print("else mai")

print("\n")

for j in []:
    print(j)
else:
    print("else mai")
    
print("\n")
    
for k in range(5):
    print(k)
    if(k==3):
        break
else:
    print("else mai") # this will not be executed because when k==3 it breaks 

print("loop k bahir") # and comes here
