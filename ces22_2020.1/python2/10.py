import numpy as np

# This decorator plot numpy friendly math functions
def plot_math_function(func):
    import matplotlib.pyplot as plt

    def plotting(*args, **kwargs):
        fname = func.__name__
        x = args[0]
        y = func(x)
        plt.plot(x, y)
        plt.grid()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(fname)
        plt.show()
    
    return plotting


@plot_math_function
def sigmoid(x):
    from math import e
    return 1 / (1 + e ** (-x))

@plot_math_function
def arctan(x):
    from numpy import arctan as atan
    return atan(x)

@plot_math_function
def square_root_abs(x):
    from numpy import sqrt
    return sqrt(abs(x))


arr = np.linspace(-10, 10, 100)

sigmoid(arr)
arctan(arr)
square_root_abs(arr)