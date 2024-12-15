import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def vector_cross_product():
    print("Vektorový součin v 3D prostoru")
    v1 = np.array(list(map(float, input("Zadejte souřadnice prvního vektoru (x1, y1, z1): ").split())))
    v2 = np.array(list(map(float, input("Zadejte souřadnice druhého vektoru (x2, y2, z2): ").split())))

    cross_product = np.cross(v1, v2)

    print(f"Vektorový součin: {cross_product}")

    x_min =  min(v1[0], v2[0], cross_product[0])
    x_max =  max(v1[0], v2[0], cross_product[0])
    y_min =  min(v1[1], v2[1], cross_product[1])
    y_max =  max(v1[1], v2[1], cross_product[1])
    z_min =  min(v1[2], v2[2], cross_product[2])
    z_max =  max(v1[2], v2[2], cross_product[2])
    # Vizualizace
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='r', label='v1')
    ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='b', label='v2')
    ax.quiver(0, 0, 0, cross_product[0], cross_product[1], cross_product[2], color='g', label='v1 × v2')

    multiplier = 1.5
    ax.set_xlim([x_min * multiplier, x_max * multiplier])
    ax.set_ylim([y_min * multiplier, y_max * multiplier])
    ax.set_zlim([z_min * multiplier, z_max * multiplier])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
    plt.title("Vektory a jejich vektorový součin v 3D prostoru")
    plt.show()

vector_cross_product()
