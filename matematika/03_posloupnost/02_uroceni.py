import matplotlib.pyplot as plt

# Parametry
P = 1000  # Počáteční vklad (principal)
r = 0.05  # Roční úroková míra (5 %)
n = 20    # Počet let

# Výpočty
simple_interest = [P * (1 + r * t) for t in range(n+1)]  # Jednoduché úročení
compound_interest = [P * (1 + r)**t for t in range(n+1)]  # Složené úročení

# Vykreslení grafu
plt.plot(range(n+1), simple_interest, marker='o', label="Jednoduché úročení", color="blue")
plt.plot(range(n+1), compound_interest, marker='o', label="Složené úročení", color="green")
plt.title("Srovnání jednoduchého a složeného úročení")
plt.xlabel("Roky")
plt.ylabel("Hodnota (Kč)")
plt.legend()
plt.grid()
plt.show()
