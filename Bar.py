import matplotlib.pyplot as plt
import numpy as np
a = np.array(["CSK"])
b = np.array([10])
c = np.array(["MI"])
d = np.array([6])
e = np.array(["RCB"])
f = np.array([3])
g = np.array(["RR"])
h = np.array([2])
i = np.array(["DC"])
j = np.array([2])
k = np.array(["PBKS"])
l = np.array([0])
m = np.array(["KKR"])
n = np.array([3])
o = np.array(["LSG"])
p = np.array([0])
q = np.array(["GT"])
r = np.array([2])
s = np.array(["SRH"])
t = np.array([2])
plt.legend(title = "No.of Times Entered Final")
plt.bar(a,b,width=0.5,color="yellow")
plt.bar(c,d ,color ="blue",width=0.5 )
plt.bar(e,f ,color ="red",width=0.5 )
plt.bar(g,h ,color ="pink",width=0.5 )
plt.bar(i,j ,color ="lightblue",width=0.5 )
plt.bar(k,l,color ="red",width=0.5 )
plt.bar(m,n,color ="blue",width=0.5 )
plt.bar(o,p,color ="darkblue",width=0.5 )
plt.bar(q,r,color ="darkblue",width=0.5 )
plt.bar(s,t,color ="orange",width=0.5 )
plt.show()