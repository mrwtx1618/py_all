

def mydecorator(function_be_decorated):
    def wrapper(*args):
        print('Inside of the decorator before calling the function')
        function_be_decorated(*args)
        print('Inside of the decorator before calling the function')
    return wrapper

@mydecorator
def printName(name):
    print(name)



printName('111222')



