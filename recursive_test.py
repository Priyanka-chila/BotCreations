def hello(str):
"""This """
    
    try:
        print(str)
        str = (str+' '+str)
        hello(str+' '+ "united kingdom")
        return str
    except Exception as e:
        return e

    #str = str+str
    #hello(str)
print(hello("welcome"))
