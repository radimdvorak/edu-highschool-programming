import turtle

# Nastavení plátna
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Kreslení geometrických tvarů")
screen.screensize(640, 480)

# Vytvoření želvy (kreslicího nástroje)
pen = turtle.Turtle()
pen.speed(3)  # Rychlost kreslení

# Funkce pro kreslení pravidelného mnohoúhelníku
def draw_polygon(sides, length):
    angle = 360 / sides  # Výpočet úhlu mezi stranami
    for _ in range(sides):
        pen.forward(length)  # Pohyb vpřed o délku strany
        pen.left(angle)      # Otočení o vypočítaný úhel

# Kreslení tvarů
# Trojúhelník
pen.color("blue")
draw_polygon(3, 100)

# Přesun želvy na jinou pozici
pen.penup()
pen.goto(-150, -50)
pen.pendown()

# Čtverec
pen.color("green")
draw_polygon(4, 100)

# Přesun želvy na jinou pozici
pen.penup()
pen.goto(150, -50)
pen.pendown()

# Šestiúhelník
pen.color("red")
draw_polygon(6, 100)

# Ukončení programu
pen.hideturtle()
screen.mainloop()
