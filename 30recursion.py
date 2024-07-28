def fact(n):
    if(n>=2):
        return n * fact((n-1))
    else:
        return n    
print(fact(5))