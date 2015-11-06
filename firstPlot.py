# -*- coding: utf-8 -*-

import pylab

principal = 10000
interest = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal*interest
pylab.plot(range(years + 1), values, 'g')
pylab.title('Growth')
pylab.xlabel('Years')
pylab.ylabel('Value')
pylab.show()    