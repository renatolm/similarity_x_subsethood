import numpy as np
import pylab as pl
import synthetic

mg = synthetic.mackey_glass(sample_len=1000, tau=17)

#print len(mg[0])

pl.plot(mg[0])
pl.show()

