a="ayesh!!!!!!!"
print("length" , len(a))
print(a.upper())
print(a.lower())
print(a.strip(("!"))) #removes the specified character from the beginning and end of the string
print(a.strip(("a"))) 
print(a.replace("ay", "qu")) #replaces the specified string with another string here "ay" with "qu"

b="ayesh qureshi charya"
print(b.split(" ")) #splits the string into substrings (lists) if it finds instances of the separator


c="ayesh qUreshi is Good huMan"
print(c.capitalize()) #converts the first character of the string to uppercase and the rest to lowercase
print(c.center(50)) #returns a centered string 50 spaces long

d="ayesh ayesh ayesh"
print(d.count("ayesh")) #returns the number of times a specified value occurs in a string


e="Welcome to the console!!"
print(e.endswith("!!")) #returns true if the string ends with the specified value
print(e.endswith("to", 4, 10)) #returns true if the string ends with the specified value
print(e.find("to")) #searches the string for a specified value and returns the position of where it was 
print(e.index("to")) #searches the string for a specified value and returns the position of where it was

f="Welcometotheconsole"
print(f.isalnum()) #returns true if all characters in the string are alphanumeric
print(f.isalpha()) #returns true if all characters in the string are in the alphabet
print(f.islower())