'''
Solving the exercise sheets is recommended but not mandatory to be admitted to
the final exam. There are no bonus points.
Exercise sheets will be published on Fridays and will be discussed in class one week
later. We strongly encourage you to solve the exercise sheets beforehand to benefit
from the discussions in class.
We will be using Python for the programming exercises. Python can be used both
interactively in command line or by executing scripts, e.g. from within an IDE, for
solving numerical computations. Python is freely available for Linux, Mac OS, and
Windows at https://www.python.org/downloads/. A quick guide on Python is
given in the Python cheat sheet, which is available on the website of this lecture.
Recommended for Windows:
You can find the Python modules and editors integrated in one installer at
https://winpython.github.io/. It includes all the important Python modules
and IDEs for interactive debugging. Once installed, you can open the interactive
debugger Spyder and start writing your code.
Recommended for Linux:
You can use the python package that is most probably included in your distribution.
In addition, you might need to install the python-scipy package or alike.
'''

'''
Functions in Python are usually defined inside a file. Create a file named
solution.py and implement the following function:
f(x) = cos(x) exp(x)
'''

import math
import matplotlib.pyplot as plt
import numpy as np

x_values = []
f_values = []

def func(x):
        
        ret = np.cos(x) * np.exp(x)
        return ret


x_values = np.linspace(-2 * np.pi, 2 * np.pi, 600)

f_values = func(x_values)

plt.plot(x_values, f_values, 'r')

plt.savefig('Assignment 1.png')
plt.show()

# next question
avg = 5.0
std_deviation = 2.0
random_vec = np.random.normal(avg, std_deviation, 100000)
uniform_vec = np.random.uniform(0, 10, 100000)


plt.figure()
x, diag, y = plt.hist(uniform_vec, 123)

plt.figure()
count, bins, ignored = plt.hist(random_vec, 100, normed=True)
plt.show()


