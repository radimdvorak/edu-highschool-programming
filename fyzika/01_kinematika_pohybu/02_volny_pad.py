import matplotlib.pyplot as plt

# Zadání parametrů
h = float(input("Zadejte počáteční výšku (m): "))
g = 9.81  # gravitační zrychlení
t_max = (2 * h / g) ** 0.5  # doba pádu

# Výpočet polohy v čase
time = [t / 100 for t in range(int(t_max * 100) + 1)]
position = [h - 0.5 * g * t**2 for t in time]

# Vykreslení grafu
plt.plot(time, position, label='h(t) = h - 1/2 * g * t^2')
plt.title('Volný pád')
plt.xlabel('Čas (s)')
plt.ylabel('Výška (m)')
plt.legend()
plt.grid()
plt.show()
