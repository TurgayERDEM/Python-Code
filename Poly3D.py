import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Bir figür oluşturalım ve 3D eksenleri ekleyelim
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# 3D koordinatlarını tanımlayalım
verts = [
    [1, 1, 1],
    [-1, 1, 1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, -1],
    [1, -1, -1]
]

# Köşe dizisini bir Poly3DCollection nesnesi ile oluşturalım
faces = [
    [verts[0], verts[1], verts[2], verts[3]],
    [verts[4], verts[5], verts[6], verts[7]],
    [verts[0], verts[1], verts[5], verts[4]],
    [verts[2], verts[3], verts[7], verts[6]],
    [verts[1], verts[2], verts[6], verts[5]],
    [verts[4], verts[7], verts[3], verts[0]]
]

# Poly3DCollection nesnesini oluşturalım
poly3d = Poly3DCollection(faces, alpha=0.8, linewidths=1, edgecolors='k')

# Yüzeyleri ekle ve grafiği göster
ax.add_collection3d(poly3d)

# Eksen etiketlerini ayarlayalım
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Eksen sınırlarını ayarlayalım
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])

# Arka plan rengini ayarlayalım
ax.set_facecolor('white')

# Fare tekeri ile zoom kontrolü ekleme
def on_scroll(event):
    axtemp = event.inaxes
    x_min, x_max = axtemp.get_xlim()
    y_min, y_max = axtemp.get_ylim()
    z_min, z_max = axtemp.get_zlim()

    scale = 1.1
    if event.button == 'up':
        # zoom in
        axtemp.set_xlim(x_min * scale, x_max * scale)
        axtemp.set_ylim(y_min * scale, y_max * scale)
        axtemp.set_zlim(z_min * scale, z_max * scale)
    elif event.button == 'down':
        # zoom out
        axtemp.set_xlim(x_min / scale, x_max / scale)
        axtemp.set_ylim(y_min / scale, y_max / scale)
        axtemp.set_zlim(z_min / scale, z_max / scale)
    plt.draw()

fig.canvas.mpl_connect('scroll_event', on_scroll)

# Görüntüyü gösterelim
plt.show()
