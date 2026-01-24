class Empty:
    counter=123
    def __init__(self):
        print(self)
print(Empty.counter)
x=Empty()
print(x.counter)