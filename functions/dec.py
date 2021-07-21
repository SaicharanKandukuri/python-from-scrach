def start(func):
    def inner(arg):
        print ("*" * 30)
        func(arg)
        print ("*" * 30)
    return inner

def percents(func):
    def inner(arg):
        print("%" * 30)
        func(arg)
        print("%" * 30)
    return inner

@start
@percents

def print_args(msg):
    print ("GG")

print_args()