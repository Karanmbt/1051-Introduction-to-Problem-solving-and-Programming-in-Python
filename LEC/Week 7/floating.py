def isFloat(string):
    # check if string is a float
    try:
        float(string)
        return True
    except:
        return False
    
x = isFloat("hello")
print(x)


"""def isFloat(string):
    for char in string:
        if char not in "0123456789.-":
            return False
    if string.count(".") > 1:
        return True
    
"""