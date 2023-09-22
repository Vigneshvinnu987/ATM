import matplotlib.pyplot as plt
import numpy as np
y = np.array([10,6,3,0,0,2,2,3,1,2])
mylables = ["CSK","MI","RCB","LSG","PBKS","GT","DC","KKR","RR","SRH"]
mycolors = ["Yellow","blue","Red","Lightblue","Red","Darkblue","Blue","Blue","pink","Orange"]
myexplode = [0.2,0,0,0,0,0,0,0,0,0]
plt.pie(y,labels=mylables,explode=myexplode,shadow=True,colors=mycolors)
plt.legend()
#plt.legend(title="Most no.of times entered final in IPL")
plt.show()