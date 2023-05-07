import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import rotate

img = plt.imread("road.jpg")

#a
add_brightness = 100
light_img = np.where((255 - img) < add_brightness, 255, img+add_brightness)

plt.figure()
plt.imshow(img, cmap="gray")
plt.show()
plt.title("a) Posvjetljena slika")
plt.imshow(light_img, cmap="gray")
plt.show()

#b
quarters = np.hsplit(img, 4)
second_quarter = quarters[1]
plt.title("b) Druga četvrtina")
plt.imshow(second_quarter, cmap="gray")
plt.show()

#c
rotated = np.rot90(img)
rotated = np.rot90(rotated)
rotated = np.rot90(rotated)
plt.title("c) Rotirano za 90°")
plt.imshow(rotated, cmap="gray")
plt.show()

#d
mirror = np.flip(img, axis=0)
plt.title("d) Zrcaljena slika")
plt.imshow(mirror, cmap="gray")
plt.show()

