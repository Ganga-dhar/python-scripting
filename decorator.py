def logger(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@logger
def greet():
    print("Hello!")

greet()

