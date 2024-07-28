def average(a=9, b=10):
    print("Average of ", a, " and ", b, " is ", (a+b)/2)
    
average(5,3)
average()
average(b=9) #b value is 9



def name(fname, mname="Ayesh", lname="Qureshi"):
    print("hello", fname, mname, lname)
    
name("muhmmad")

print("\n\n")


def average(*numbers):
    print(type(numbers)) #tuple
    sum=0
    for i in numbers:
        sum+=i
    print("Average is: " , sum/len(numbers))
        
average(5,4,3,2,1)

print("\n\n")

def name(**names):
    print(type(names)) #dictionary
    print("hello", names["fname"], names["mname"], names["lname"])

name(fname="muhammad", mname="ayesh", lname="qureshi")
     
print("\n\n")

def name(**names):
    print(type(names)) #dictionary
    for i in names:
        print(names[i])
name(fname="muhammad", mname="ayesh", lname="qureshi")




print("\n\n")

def average(*numbers):
    print(type(numbers)) #tuple
    sum=0
    for i in numbers:
        sum+=i
    return sum/len(numbers)        
print(average(5,4,3,2,1))


#functions returniing more than  one value
print("\n\n")

def convert_seconds(seconds):
    hours=seconds//3600
    minutes=(seconds-hours*3600)//60
    remaining_seconds=seconds-hours*3600 - minutes * 60
    return hours,minutes,remaining_seconds
hours, minutes, seconds=convert_seconds(5000)
print(hours,minutes, seconds)