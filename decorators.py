def greet(fx):
    def mfx(*args,**kwargs):
        print('Good morning')
        fx(*args,**kwargs)
        print('Thank you')
    return mfx

@greet
def hello():
    print("Hello world")

@greet
def add(a,b):
    print(a+b)

hello()
print()
add(1,4)
print()

