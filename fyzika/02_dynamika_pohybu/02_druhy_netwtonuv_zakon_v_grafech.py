import matplotlib.pyplot as plt

# Funkce pro simulaci pohybu
def simulate_motion(mass, force, mu, time_step, total_time):
    """
    Simuluje pohyb tělesa podle Newtonova 2. zákona.

    Parametry:
        mass: hmotnost tělesa (kg)
        force: velikost síly působící na těleso (N)
        mu: koeficient tření (bezrozměrný)
        time_step: časový krok simulace (s)
        total_time: celková doba simulace (s)
    """
    # Počáteční podmínky
    velocity = 0  # Rychlost (m/s)
    position = 0  # Poloha (m)
    
    # Záznam dat
    times = [0]
    positions = [position]
    velocities = [velocity]
    accelerations = []

    # Hlavní smyčka simulace
    for t in range(1, int(total_time / time_step) + 1):
        current_time = t * time_step

        # Vypočítejte třecí sílu
        friction_force = mu * mass * 9.81  # F_tření = μ * m * g
        
        # Efektivní síla působící na těleso
        net_force = max(force - friction_force, 0)  # Síla nemůže být záporná
        
        # Zrychlení podle F = ma
        acceleration = net_force / mass
        
        # Aktualizace rychlosti a polohy
        velocity += acceleration * time_step
        position += velocity * time_step

        # Uložení dat
        times.append(current_time)
        positions.append(position)
        velocities.append(velocity)
        accelerations.append(acceleration)

    return times, positions, velocities, accelerations

# Parametry simulace (můžete měnit)
mass = 5.0         # Hmotnost tělesa (kg)
force = 20.0       # Působící síla (N)
mu = 0.1           # Koeficient tření (μ)
time_step = 0.1    # Časový krok (s)
total_time = 10.0  # Celková doba simulace (s)

# Spuštění simulace
times, positions, velocities, accelerations = simulate_motion(mass, force, mu, time_step, total_time)

# Vykreslení grafů
plt.figure(figsize=(10, 8))

# Graf polohy
plt.subplot(3, 1, 1)
plt.plot(times, positions, label="Poloha (m)", color="blue")
plt.title("Poloha v čase")
plt.xlabel("Čas (s)")
plt.ylabel("Poloha (m)")
plt.grid()
plt.legend()

# Graf rychlosti
plt.subplot(3, 1, 2)
plt.plot(times, velocities, label="Rychlost (m/s)", color="green")
plt.title("Rychlost v čase")
plt.xlabel("Čas (s)")
plt.ylabel("Rychlost (m/s)")
plt.grid()
plt.legend()

# Graf zrychlení
plt.subplot(3, 1, 3)
plt.plot(times[:-1], accelerations, label="Zrychlení (m/s²)", color="red")
plt.title("Zrychlení v čase")
plt.xlabel("Čas (s)")
plt.ylabel("Zrychlení (m/s²)")
plt.grid()
plt.legend()

# Úprava rozložení a zobrazení grafů
plt.tight_layout()
plt.show()
