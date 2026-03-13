def f(*args, **kwargs): #*args means thise function will take variable number of positional arguments, some number of kew word arguments (kwargs)
    print("Positional arguments: ", args)
    print("Named arguments: ", kwargs)
    #kwargs is automatically a dictionary that contains all of named arguments passing to the function

f(a=100,b=50,c=25)