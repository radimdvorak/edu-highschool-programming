import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Nastavení simulace
grid_size = 200    # Velikost mřížky (počet bodů)
y_max = 1.0        # Maximální výchylka
wave_speed = 2.0   # Rychlost šíření vlny (jednotky/grid)
frequency = 0.25   # Frekvence vlnění (Hz)
time_step = 0.3    # Časový krok simulace (s)
total_time = 100.0 # Celková doba simulace (s)

# Výpočet vlnové délky
wavelength = wave_speed / frequency

# Pozice zdrojů vlnění (mřížka je 200x200)
sources = [(140, 140), (60, 60)]  # Více zdrojů

# Inicializace mřížky amplitud
x = np.linspace(0, grid_size - 1, grid_size)
y = np.linspace(0, grid_size - 1, grid_size)
X, Y = np.meshgrid(x, y)

# Funkce pro výpočet amplitudy vlny z jednoho zdroje
def wave_amplitude(source, t):
    distance = np.sqrt((X - source[0])**2 + (Y - source[1])**2)
    distThresh = wave_speed * t
    # Vyhneme se dělení nulou u zdroje
    with np.errstate(divide='ignore', invalid='ignore'):
        amplitude = y_max * np.sin(2 * np.pi * (frequency * t - (distance / wavelength)))
        amplitude[distance == 0] = 0  # V místě zdroje nastavíme amplitudu na nulu
        amplitude[distance > distThresh] = 0
    return amplitude

# Nastavení grafu
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_title("Simulace šíření vln na vodní hladině")
ax.axis("off")

# Počáteční amplitudy
amplitude = np.zeros((grid_size, grid_size))
image = ax.imshow(amplitude, cmap="Blues", interpolation="bilinear", vmin=-len(sources)*y_max, vmax=len(sources)*y_max)

# Funkce pro aktualizaci animace
def update(frame):
    global amplitude
    t = frame * time_step  # Aktuální čas
    amplitude = np.zeros((grid_size, grid_size))  # Reset mřížky
    for source in sources:
        amplitude += wave_amplitude(source, t)  # Přičítání vln od všech zdrojů
    image.set_array(amplitude)
    return image,

# Animace
frames = int(total_time / time_step)
ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

plt.show()
