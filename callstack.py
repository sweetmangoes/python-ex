def greet(name):
    print ("Hello, " + name + "!")
    greet2(name)
    print ("getting ready to say bye...")
    bye()

def greet2(name):
    print ("how are you, d" + name + "?")

def bye():
    print ("ok bye!")

greet("maggie")
