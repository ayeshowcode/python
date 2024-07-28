a=input("enter a number: ")
print(f"Multiplication table of {a} is: ")
try:
    for i in range(1,11):
        print(f"{int(a)} X {int(i)} = {int(a)*i}")
except Exception as e:
    print(e)

print("\n\n")

try:
    num = int(input("enter a number: "))
    a=[3,4]
    print(a[num])
except ValueError:
    print("Number entered is not an integer: ")
except IndexError:
    print("index error")