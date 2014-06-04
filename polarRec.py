import numpy as np
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt

x = np.linspace(-10,10,1000)
number = raw_input("How many polynomials do you want to plot?")
#-------------First Plot---------------
plt.subplot(1,2,1)

ylin = x
yqua = x ** 2
ycub = x ** 3

plt.xlim([-10,10])
plt.ylim([-10,10])

plt.plot(x,ylin,'r', label = "linear")
plt.plot(x,yqua,'g', label = "quadratic")
plt.plot(x,ycub,'b', label = "cubic")

plt.xlabel("x")
plt.ylabel("y")

plt.legend(loc = "lower right")
plt.title("rectangular coordinates")

#------------------ Second Plot-----------------

plt.subplot(1,2,2, polar = True)

ylin = x
yqua = x ** 2
ycub = x ** 3

plt.plot(x,ylin,'r', label = "linear")
plt.plot(x,yqua,'g', label = "quadratic")
plt.plot(x,ycub,'b', label = "cubic")

plt.xlabel("r")
#plt.ylabel(r"$\theta$")

plt.legend(loc = "lower left", bbox_to_anchor = (2,1))
plt.title("polar coordinates")
#----------------Final Setup---------------------

plt.savefig("Math.pdf")


