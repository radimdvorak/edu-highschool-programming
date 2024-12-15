import cellpylib as cpl
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Vytvoření počátečního stavu (les)
forest_size = 75
forest = cpl.init_simple2d(forest_size, forest_size, 0)
# forest = np.zeros((forest_size, forest_size), dtype=int)

# Pravidla šíření ohně
def fire_rule(cells, c, t):
    """Definice pravidel pro šíření ohně."""
    current_cell = cells[1][1]  # Středová buňka (aktuální buňka)
    neighbors = cells

    neighbors[1][1] = 0

    # 4 okoli
    neighbors[0][0] = 0
    neighbors[0][2] = 0
    neighbors[2][0] = 0
    neighbors[2][2] = 0

    # osetrime okraje mrizky
    row = c[0]
    col = c[1]

    # [0,0][0,1][0,2]
    # [1,0][1,1][1,2]
    # [2,0][2,1][2,2]

    if row == 0:
        for i in range(3):
            neighbors[0][i] = 0
    if row == forest_size - 1:
        for i in range(3):
            neighbors[2][i] = 0
    if col == 0:
        for i in range(3):
            neighbors[i][0] = 0
    if col == forest_size - 1:
        for i in range(3):
            neighbors[i][2] = 0

    # Strom začne hořet, pokud hoří některý soused
    if current_cell == 2 and 1 in neighbors:
        return 1  # Začne hořet
    # Hořící strom shoří
    elif current_cell == 1:
        return 0  # Shoří na prázdnou buňku
    # Stromy, které nehoří, zůstanou stromy
    elif current_cell == 2:
        return 2  # Zůstane stromem
    # Prázdné buňky zůstávají prázdné
    return 0

# Callback funkce pro detekci stabilního stavu
def cont(states, t):
    """Zastaví simulaci, pokud aktuální stav je stejný jako předchozí."""
    if len(states) > 1 and np.array_equal(states[-1], states[-2]):
        print("Simulace se zastavila: Automat dosáhl stabilního stavu: ", t)
        return False
    return True


# Inicializace lesa (všechny stromové buňky jsou ve stavu 2 - strom)
#forest[forest == 0] = 2

percentage = 60
# forest = np.random.random_integers(0, 100, (1, forest_size, forest_size))
forest = np.random.randint(0, 100, (1, forest_size, forest_size))
forest[forest < (100 - percentage)] = 0
forest[forest >= (100 - percentage)] = 2

# forest[0][0][int(forest_size/5)] = 1

for i in range(forest_size):
    forest[0][i, 0] = 1 if forest[0][i, 0] == 2 else 0 # Inicializace ohně zleva
    # forest[0][i, forest_size-1] = 1 if forest[0][i, forest_size-1] == 2 else 0 # Inicializace ohně zprava
    # forest[0][0, i] = 1 if forest[0][0, i] == 2 else 0 # Inicializace ohně z vrchu
    # forest[0][forest_size-1, i] = 1 if forest[0][forest_size-1, i] == 2 else 0 # Inicializace ohně ze spodu

# Spuštění simulace
forest = cpl.evolve2d(cellular_automaton=forest, timesteps=cont, apply_rule=fire_rule, neighbourhood="von Neumann", memoize=False)

cpl.plot2d_animate(forest, interval=100, colormap=ListedColormap(["black", "red", "green"]))

# Vizualizace výsledků
# cpl.plot2d(forest)
# plt.show()
