def sort(width, height, length, mass):
    error, isValid = validateArgs(width, height, length, mass)
    if not isValid:
        return error
    return "REJECTED" if isBulky(width, height, length) and isHeavy(mass) else "SPECIAL" if isBulky(width, height, length) or isHeavy(mass) else "STANDARD"
    
def isBulky(width, height, length):
    return width * height * length >= 1000000 or width >= 150 or height >= 150 or length >= 150

def isHeavy(mass):
    return mass >= 20

def validateArgs(width, height, length, mass):
    if not isinstance(width, int) or not isinstance(height, int) or not isinstance(length, int) or not isinstance(mass, int):
        return "Invalid argument type", False
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        return "Invalid argument value", False
    return None, True

#test cases
print(sort(100, 100, 100, 20)) #REJECTED
print(sort(1000000, 100, 100, 20)) #REJECTED
print(sort(99, 99, 99, 200)) #SPECIAL
print(sort(99, 99, 99, 10)) #STANDARD
print(sort(150, 20, 20, 5)) #SPECIAL
print(sort(20, 150, 20, 5)) #SPECIAL
print(sort(20, 20, 150, 5)) #SPECIAL
print(sort(150, 150, 150, 5)) #SPECIAL
print(sort("10", 20, 20, 5)) #Invalid argument type
print(sort(-10, 20, 20, -5)) #Invalid argument value
print(sort("",20, 20, 5)) #Invalid argument type
