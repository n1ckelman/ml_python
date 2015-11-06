import scipy as sp
import matplotlib.pyplot as plt

data = sp.genfromtxt("C:\Users\Rybkin\Desktop\web_traffic.tsv", delimiter="\t")
x = data[:,0]
y = data[:,1]

x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

fpl, residuals, rank, sv, rcond = sp.polyfit(x,y,1,full=True)
fl = sp.poly1d(fpl)

plt.scatter(x,y, s=10)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)], ['week %i' % w for w in range(10)])
plt.autoscale(tight=True)
plt.grid(True, linestyle='-', color='0.75')
fx = sp.linspace(0,x[-1],1000)
plt.plot(fx, fl(fx), linewidth=4)
plt.legend(["d=%i" %fl.order], loc= "upper left")
plt.show()