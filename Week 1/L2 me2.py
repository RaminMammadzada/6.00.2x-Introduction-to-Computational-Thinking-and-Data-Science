import random
random.randint(1,5)
random.choice(['apple','banana','cat',])

def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    # Your code here
    while 1:            
        a=random.randint(0,99)
        if a%2==0:
            return a

    
# Possible solutions:

def deterministicNumber():
    return 10 # or 12 or 14 or 16 or 18 or 20

# or

def deterministicNumber2():
    random.seed(0) # This will be discussed in the video "Drunken Simulations"
    return 2 * random.randint(5, 10)

# Possible solutions:
def stochasticNumber():
    return 2 * random.randint(5, 10)

# or 

def stochasticNumber2():
    return random.randrange(10, 22, 2)

# or, again, something like that.


