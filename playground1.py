import dataStats as dS
import hmm
import numpy as np
import matplotlib.pylab as plt
import this


'''
1 = wake up
2 = breakfast
3 = shower
4 = commute
5 = lunch
6 = entertainment
7 = dinner
8 = sleep
9 = work
'''
symbols={"1":"w","2":"b","3":"s","4":"c","5":"l","6":"e","7":"d","8":"l","9":"o"}

data=[[1,2,3,4,9,5,9,4,6,7,8],
    [1,3,2,4,9,5,9,4,6,7,8],
    ]
output=""
for i in data:
    for a in i:
        output+=symbols[str(a)]
    output+=","
    
print(output)


timeData=[8,8.5,8.7,9,9.5,12,13,17,17.5,19,20,
          8.5,8.7,9,9.5,10,12,13,17,17.5,19,20
       ]
hours=[int(i) for i in timeData]
minutes=[ 10*(timeData[i]-hours[i]) for i in range(len(hours))]

# Create an HMM

model=hmm.HMM(n_states=5,V=[1,2,3,4,5,6,7,8,9])

model=hmm.baum_welch(model, data, epochs=100)

plt.imshow(model.A)
plt.show()
print(model.A)
print(model.B)
print(model.F)

# TODO
# Before moving forward with all thisfirst define some standard format to read all this data
# maybe also think about the idea of having an HMM with discrete and continuous data mixed, maybe
# it is not such a crazy idea after all and it maybe not even hard to implement.


