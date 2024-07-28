letter="hi my name {1} and i am from {0}"
country="pakistan"
name = "ayesh"

print(letter.format(name, country))
print(letter.format(country, name))

print(f"Hi my name is {name} and i am from {country}")


print("\n\n")
txt= "for only {price: .2f}$"

print(txt.format(price=49.09999))



print("\n\n")
price=49.09999
txt= f"for only {price: .2f}$"
# print(txt.format())
print(txt)


print("\n\n")
print(f"{2 * 30}")


print("\n\n")
print(f"Hi my name is {{name}} and i am from {{country}}") #now the name and country will be in curly brackets
