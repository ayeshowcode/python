import time
timestamp = time.strftime("%H:%M:%S")
print(timestamp)
# hour = int(time.strftime("%H"))
hour=int(input("Enter hour"))
print(hour)

if(hour>=0 and hour <=12):
    print("Morning")
elif(hour>=12 and hour <=7):
    print("Evening")
else:
    print("Night")
    
    
