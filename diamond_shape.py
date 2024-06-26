# Turgay ERDEM

# Written on June 27  01.43


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Şekil ve 3D alt grafik oluşturma
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Şeklin köşelerini tanımlama
vertices = [[0, 0, 0], # köse 0
            [1, 0, 0], # köse 1
            [0, 0, 1], # köse 2
            [1, 0, 1], # köse 3
            [0.5, -1, 0.5], # köse 4/ burada eksiyi eksen altına insin diye koyduk. Eğer şekli grafik içinde tutmak istersek 0 ile 1 değer aralığında işlem yapmalıyız.
            [0.25, 0.5, 0.25], # köse 5
            [0.25, 0.5, 0.75], # köse 6
            [0.75, 0.5, 0.75], # köse 7
            [0.75, 0.5, 0.25]] # köse 8

# Şeklin yüzlerini tanımlayın
faces = [[vertices[j] for j in [0, 4, 1]],   #Buradaki sayılar yukarıda tanımladığımız köşe isimleri. O değerlere göre yüz tanımlıyoruz.
         [vertices[j] for j in [0, 2, 4]],
         [vertices[j] for j in [2, 3, 4]],
         [vertices[j] for j in [1, 3, 4]],
         [vertices[j] for j in [0, 1, 8, 5]],
         [vertices[j] for j in [0, 2, 6, 5]],
         [vertices[j] for j in [2, 6, 7, 3]],
         [vertices[j] for j in [3, 7, 8, 1]],
         [vertices[j] for j in [5, 6, 7, 8]]]



# Şekil çizmek için Poly3DCollection kullanma
poly3d = Poly3DCollection(faces, 
                          facecolors='red', linewidths=1, edgecolors='b', alpha=.35)
ax.add_collection3d(poly3d)

# Eksen sınırlarını ayarlama
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Eksen sınırlarını belirleme
ax.set_xlim([0, 1]) 
ax.set_ylim([0, 1])   # Burada eksen değerlerini değiştirebilirsiniz.
ax.set_zlim([0, 1])

plt.show()
