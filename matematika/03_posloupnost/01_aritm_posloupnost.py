import matplotlib.pyplot as plt

# Aritmetická posloupnost
a1 = 5  # první člen
d = 3   # diference
n = 20  # počet členů

# Vytvoření posloupnosti
arit_seq = [a1 + d * i for i in range(n)]

# Vykreslení grafu
plt.plot(range(1, n+1), arit_seq, marker='o', label="Aritmetická posloupnost")
plt.title("Aritmetická posloupnost")
plt.xlabel("Pořadí členu (n)")
plt.ylabel("Hodnota členu (a_n)")
plt.legend()
plt.grid()
plt.show()

