import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as Image
from sklearn.cluster import KMeans

# ucitaj sliku
img = Image.imread("imgs\\test_1.jpg")

# prikazi originalnu sliku
plt.figure()
plt.title("Originalna slika")
plt.imshow(img)
plt.tight_layout()
plt.show()

# pretvori vrijednosti elemenata slike u raspon 0 do 1
img = img.astype(np.float64) / 255

# transfromiraj sliku u 2D numpy polje (jedan red su RGB komponente elementa slike)
w,h,d = img.shape
img_array = np.reshape(img, (w*h, d))

# rezultatna slika
img_array_aprox = img_array.copy()


#zad2
clusters=4

#zad-2-1
# broj razlicitih boja u slici
print(len(np.unique(img_array_aprox,axis=0)))

#zad-2-2
# primjena K-means algoritma
km = KMeans ( n_clusters =clusters ) 
labels = km.fit_predict(img_array_aprox)

#zad-2-3
# promjena vrijednosti u K-means centre
rgb_cols = km.cluster_centers_.astype(np.float64)
print(rgb_cols)
img_quant = np.reshape(rgb_cols[labels],(w,h,d))

plt.imshow(img_quant)
plt.show()

#zad2-6
distortions = []
K = range(1,10)
for k in K:
    kmeanModel = KMeans ( n_clusters =k , init ='random',n_init =10 , random_state =0 )
    kmeanModel.fit(img_array)
    distortions.append(kmeanModel.inertia_) #inertia mjeri koliko je dobro dataset grupiran K-means metodom

plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show()

#zad2-7
# binarna slika s obzirom na klasu 
for i in range(clusters): 
    bit_values = labels==[i]
    binary_img = np.reshape(bit_values, (img.shape[0:2]))
    binary_img = binary_img*1
    x=int(i/2)
    y=i%2
    plt.imshow(binary_img)
    plt.show()

