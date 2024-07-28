def func1():
    try:
        l = [1,2,4,5,6]
        i=int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0

    print("always executed")

x=func1()
print(x)

print("\n\n")
#if
def func1():
    try:
        l = [1,2,4,5,6]
        i=int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0
    finally:
        print("always executed")

x=func1()
print(x)