import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data.csv", delimiter=",", dtype=float, skiprows=1)

#a
print("a) Mjerenja su izvršena na", data.shape[0], "ljudi.")

#b
# x sadrzi visine (stupac 1) a y tezine (stupac 2)
x = data[:, 1]
y = data[:, 2]

plt.title("b) Omjer visine i težine")
plt.xlabel("Visina")
plt.ylabel("Težina")
plt.scatter(x, y, color="b", s=0.8)
plt.show()

#c
x_50 = data[:,1][::50]
y_50 = data[:,2][::50]

plt.title("c) Omjer visine i težine za svaku 50u osobu")
plt.xlabel("Visina")
plt.ylabel("Težina")
plt.scatter(x_50, y_50, color="b",s=5)
plt.show()

#d
print("d) Najmanja visina u skupu je:", min(x), "cm")
print("Najveća visina u skupu je:",  max(x), "cm")
print("Prosječna visina u skupu iznosi", round(x.mean(), 2), "cm.")

#e
m = data[np.where(data[:,0] == 1)]
f = data[np.where(data[:,0] == 0)]
m = m[:,1]
f = f[:,1]

print("e) Najmanja visina u muškom skupu:", min(m),"cm")
print("Najveća visina u muškom skupu:",max(m), "cm")
print("Prosječna visina u muškom skupu iznosi", round(m.mean(), 2), "cm.")
print("Najmanja visina u ženskom skupu:", min(f), "cm")
print("Najveća visina u ženskom skupu:",max(f), "cm")
print("Prosječna visina u ženskom skupu iznosi", round(f.mean(), 2), "cm.")
