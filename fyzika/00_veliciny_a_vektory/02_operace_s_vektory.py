import numpy as np
import matplotlib.pyplot as plt

def vector_operations():
    print("Operace s vektory v 2D prostoru")
    x1, y1 = map(float, input("Zadejte souřadnice prvního vektoru (x1, y1): ").split())
    x2, y2 = map(float, input("Zadejte souřadnice druhého vektoru (x2, y2): ").split())

    # definice vektorů
    v1 = np.array([x1, y1])
    v2 = np.array([x2, y2])

    # Výpočty
    v_sum = v1 + v2
    v_diff = v1 - v2
    dot_product = np.dot(v1, v2)
    v1_magnitude = np.linalg.norm(v1)
    v2_magnitude = np.linalg.norm(v2)

    print(f"Součet vektorů: {v_sum}")
    print(f"Rozdíl vektorů: {v_diff}")
    print(f"Skalární součin: {dot_product}")
    print(f"Velikost vektoru 1: {v1_magnitude:.2f}")
    print(f"Velikost vektoru 2: {v2_magnitude:.2f}")

    # Vizualizace
    plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r', label='v1')
    plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='b', label='v2')
    plt.quiver(0, 0, v_sum[0], v_sum[1], angles='xy', scale_units='xy', scale=1, color='g', label='v1 + v2')

    plt.xlim(0, 6)
    plt.ylim(0, 6)
    plt.grid()
    plt.legend()
    plt.title("Vektory v 2D prostoru")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.show()

vector_operations()
