import matplotlib.pyplot as plt

# Parametry
initial_deposit = 1000   # Počáteční vklad (Kč)
regular_deposit = 100    # Pravidelný vklad (měsíční/čtvrtletní/roční) v Kč
annual_rate = 0.05       # Roční úroková míra (5 %)
years = 20               # Počet let
frequency = 12           # Počet období za rok (12 = měsíčně, 4 = čtvrtletně, 1 = ročně)

# Výpočet
total_periods = years * frequency
rate_per_period = annual_rate / frequency

# Vypočítáme zůstatek po každém období
balances = []
balance = initial_deposit
deposits = []
interests = []

for t in range(1, total_periods + 1):
    # Přidáme úroky na současný zůstatek
    balance *= (1 + rate_per_period)
    # Přidáme pravidelný vklad
    balance += regular_deposit
    # Uložíme zůstatek do seznamu
    balances.append(balance)
    deposits.append(initial_deposit + regular_deposit * t)
    interests.append(balances[-1] - deposits[-1])

# Vykreslení grafu
#plt.plot(range(1, total_periods + 1), balances, marker='o', color="purple")
plt.plot(range(1, total_periods + 1), balances, color="purple", label="Celková hodnota investice")
plt.plot(range(1, total_periods + 1), deposits, color="black", label="Hodnota samotných vkladů")
plt.plot(range(1, total_periods + 1), interests, color="black", label="Hodnota úroků")
plt.title(f"Růst úspor při {int(12 / frequency)}-měsíčních vkladech")
plt.xlabel("Období (měsíce/čtvrtletí/roky)")
plt.ylabel("Zůstatek (Kč)")
plt.grid()
plt.legend()

plt.show()
