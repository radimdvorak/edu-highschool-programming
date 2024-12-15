import matplotlib.pyplot as plt

# Zadání vstupních parametrů
x0 = float(input("Zadejte počáteční polohu (x0, v metrech): "))
v = float(input("Zadejte rychlost (v, m/s): "))
t_max = float(input("Zadejte dobu trvání pohybu (v sekundách): "))

# Výpočet dráhy v čase
time = [t for t in range(int(t_max) + 1)]
position = [x0 + v * t for t in time]

# Vykreslení grafu
plt.plot(time, position, label='x(t) = x0 + vt')
plt.title('Rovnoměrný přímočarý pohyb')
plt.xlabel('Čas (s)')
plt.ylabel('Dráha (m)')
plt.legend()
plt.grid()
plt.show()
