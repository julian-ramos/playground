from saxpy import SAX
import numpy as np
import matplotlib.pyplot as plt


t=np.linspace(0,15,num=100)
t2=np.linspace(1,16,num=100)

data=np.sin(t)
data2=np.sin(t2)



sax=SAX(wordSize=20)


rep=sax.to_letter_rep(data)
print(rep)

rep2=sax.to_letter_rep(data2)
print(rep2)


plt.plot(data,'b')
plt.plot(data2,'r')
plt.show()
