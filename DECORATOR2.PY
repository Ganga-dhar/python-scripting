
def pretty_comments(fun):
    def wrapper(a,b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print(" not divisable")
            return 
        return fun(a,b)
    return wrapper



@pretty_comments
def division(a,b):
    return a/b


if __name__ == '__main__':
    division(10,3)
    division(10,0)