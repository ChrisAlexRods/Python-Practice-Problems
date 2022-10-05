person = {
    "name": "Jay",
    "age": 18,
    "adress": {
        "street": "123 main",
        "city": "Some Town",
        "state": "Va"
    }
}

person["is_happy"] = True # add a properety
del person["is_happy"] # delete property

weight = 400
person[weight] = weight
person["adress"]["zip"] = 12345 # use brackets to enter dictionaries within dictionaries. This is adding to the adress dictionary
print(person)
print(person.get("adress").get("zip"))


# don't forget that  the key(first part of ditionary) is always a sting. the second input is the value
# Commaas always come after teach key:value,

# for the get function in a nested dicitonary. You have to chain the .get after the first key.

car = {
    "make": "whatever",
    "model": "yeah",
    "color": "red",
    "vin": 123124141,
    "type": "4-door",
}

print(car)