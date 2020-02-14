
import datetime

def a(func):
    def b(*args,**kwargs):
        print(datetime.datetime.now())
        func()
        print(datetime.datetime.now())
        return func(*args,**kwargs)
    return b



@a
def main_func():
    print("main_func")

    return None

main_func()