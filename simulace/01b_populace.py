import matplotlib.pyplot as plt
import numpy as np

def exponential_growth(initial_population, birth_rate, death_rate, migration, years):
    """Simuluje exponenciální růst populace."""
    population = [initial_population]
    for _ in range(years):
        new_population = population[-1] * (1 + (birth_rate - death_rate) / 100) + migration
        population.append(new_population)
    return population

def logistic_growth(initial_population, birth_rate, death_rate, migration, capacity, years):
    """Simuluje logistický růst populace."""
    population = [initial_population]
    for _ in range(years):
        current_population = population[-1]
        growth_rate = (birth_rate - death_rate) / 100
        logistic_factor = 1 - (current_population / capacity)
        new_population = current_population + (current_population * growth_rate * logistic_factor) + migration
        population.append(new_population)
    return population

# Parametry simulace
initial_population = 1000
birth_rate = 5  # % za rok
death_rate = 2  # % za rok
migration = 50  # lidí za rok
capacity = 5000  # maximální kapacita prostředí
years = 100  # počet let

# Výpočty
years_list = np.arange(0, years + 1)
exp_population = exponential_growth(initial_population, birth_rate, death_rate, migration, years)
log_population = logistic_growth(initial_population, birth_rate, death_rate, migration, capacity, years)

# Vizualizace
plt.figure(figsize=(10, 6))
plt.plot(years_list, exp_population, label="Exponenciální růst", linestyle='--', color='blue')
plt.plot(years_list, log_population, label="Logistický růst", linestyle='-', color='green')
plt.axhline(capacity, color='red', linestyle=':', label="Kapacita prostředí")
plt.title("Simulace demografického růstu populace")
plt.xlabel("Roky")
plt.ylabel("Počet obyvatel")
plt.legend()
plt.grid()
plt.show()
