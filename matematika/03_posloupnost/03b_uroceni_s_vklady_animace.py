import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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
deposits = []
interests = []
balance = initial_deposit

for t in range(1, total_periods + 1):
    # Přidáme úroky na současný zůstatek
    balance *= (1 + rate_per_period)
    # Přidáme pravidelný vklad
    balance += regular_deposit
    # Uložíme hodnoty
    balances.append(balance)
    deposits.append(initial_deposit + regular_deposit * t)
    interests.append(balances[-1] - deposits[-1])

# Příprava grafu
fig, ax = plt.subplots()
x_data, y_balances, y_deposits, y_interests = [], [], [], []

balance_line, = ax.plot([], [], color="purple", label="Celková hodnota investice")
deposit_line, = ax.plot([], [], color="black", label="Hodnota samotných vkladů")
interest_line, = ax.plot([], [], color="blue", label="Hodnota úroků")

ax.set_xlim(0, total_periods)
ax.set_ylim(0, max(balances) * 1.1)
ax.set_title(f"Růst úspor při {int(12 / frequency)}-měsíčních vkladech")
ax.set_xlabel("Období (měsíce)")
ax.set_ylabel("Zůstatek (Kč)")
ax.legend()
ax.grid()

# Aktualizační funkce pro animaci
def update(frame):
    x_data.append(frame + 1)
    y_balances.append(balances[frame])
    y_deposits.append(deposits[frame])
    y_interests.append(interests[frame])
    
    balance_line.set_data(x_data, y_balances)
    deposit_line.set_data(x_data, y_deposits)
    interest_line.set_data(x_data, y_interests)
    
    return balance_line, deposit_line, interest_line

# Spuštění animace
ani = FuncAnimation(fig, update, frames=range(total_periods), interval=50, blit=True, repeat=False)

plt.show()
