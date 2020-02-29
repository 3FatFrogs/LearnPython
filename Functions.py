import numpy as np


def standard_arg(arg1, arg2=5): #Positional or keyword
    print("{} - {}".format(arg1, arg2))

def pos_only_arg(arg, /): #Positional only
    print(arg)

def kwd_only_arg(*, arg): #Keyword only
    print(arg)

def concat(*args, sep="/"): #Arbitrary Argument Lists
    return sep.join(args)

def greet_me(**kwargs): #**kwargs allows you to pass keyworded variable length of arguments to a function
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))




standard_arg(4)
standard_arg(arg2=7, arg1=9)
pos_only_arg(6)
kwd_only_arg(arg=7)
x = concat("Pippo", "Ciccio", "Checco")
print(x)
greet_me(name="yasoob", age = 4, income = 25000)
greet_me()


#print Fibonacci
def Fib(n):
    Fn2 = 0 #Fn2
    Fn1 = 1 #Fn1
    for x in range(n):        
        print(Fn2, end=',')
        Fn = Fn1 + Fn2
        Fn2 = Fn1
        Fn1 = Fn
    print()
        
def Fib2(n):
     a, b = 0, 1
     while n > 0:
         print(a, end=',')                  
         a,b = b, b + a
         n=n-1
         
     print()

     
# Monte Carlo valuation of European call option
def EuropeanOption(S0,K,T,r,sigma):
    I= 1000 # number of simulations
    
    # Valuation Algorithm
    z = np.random.standard_normal(I) # pseudorandom numbers
    ST = S0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * z)
    
    # index values at maturity
    hT = np.maximum(ST - K, 0) # inner values at maturity
    C0 = np.exp(-r * T) * np.sum(hT) / I # Monte Carlo estimator

    return C0




'''
call = EuropeanOption(100,105,0.5,0.05,0.25)
print(call)
Fib(5)
Fib2(5)
'''