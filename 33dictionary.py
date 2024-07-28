dic={
    "ayesh" : "Human",
    "dog":"kutta"
}
print(dic["ayesh"])

dic2={
    1:"ayesh",
    2:"kutta",
    3: "helo"
}

print(dic2[1])

print(dic) #puri ki puri

info={'name': 'ash', 'age' : 19, 'eligible': True}
print(info)
#if not available:
# print(info['name1']) throws an error
print(info.get('name1')) #print none

print(info.keys())

for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")