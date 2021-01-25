def splitstring(str, delimeter = ' '):
    str = delimeter.join(str)
    str = str.split(delimeter)
    return str
print(splitstring(['a', 'b', 'c'], '_'))
