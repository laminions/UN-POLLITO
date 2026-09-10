from tkinter import *

# ------------------
# variables
# ------------------
BASE = 500
ALTURA = 400

x_pollito = 250
y_pollito = 350

carros = [
    [50, 140, "red", 3],
    [350, 210, "blue", -3],
    [150, 280, "orange", 2]
]

# ------------------
# funciones
# ------------------

def dibujar():
    c.delete("all")

    # pasto
    c.create_rectangle(0, 0, BASE, ALTURA, fill="green")

    # avenida
    c.create_rectangle(0, 80, BASE, 320, fill="gray")

    # meta
    c.create_rectangle(0, 50, BASE, 80, fill="lime")

    # pollito
    c.create_oval(x_pollito-15, y_pollito-15,
                  x_pollito+15, y_pollito+15,
                  fill="yellow")

    # carros
    for carro in carros:
        c.create_rectangle(carro[0], carro[1],
                           carro[0]+70, carro[1]+30,
                           fill=carro[2])


def mover_carros():
    for carro in carros:
        carro[0] = carro[0] + carro[3]

        if carro[0] > BASE:
            carro[0] = -70

        if carro[0] < -70:
            carro[0] = BASE

    dibujar()
    ventana.after(50, mover_carros)


def mover(event):
    global x_pollito, y_pollito

    if event.keysym == "Up":
        y_pollito -= 10

    if event.keysym == "Down":
        y_pollito += 10

    if event.keysym == "Left":
        x_pollito -= 10

    if event.keysym == "Right":
        x_pollito += 10

    # limites
    if x_pollito < 15:
        x_pollito = 15

    if x_pollito > BASE - 15:
        x_pollito = BASE - 15

    if y_pollito < 15:
        y_pollito = 15

    if y_pollito > ALTURA - 15:
        y_pollito = ALTURA - 15

    # ganar
    if y_pollito <= 80:
        print("¡Ganaste!")
        x_pollito = 250
        y_pollito = 350

    # perder
    for carro in carros:
        if (x_pollito > carro[0] and
            x_pollito < carro[0] + 70 and
            y_pollito > carro[1] and
            y_pollito < carro[1] + 30):

            print("¡Perdiste!")
            x_pollito = 250
            y_pollito = 350

    dibujar()


# ------------------
# ventana
# ------------------

ventana = Tk()
ventana.title("Pollito Crossing")
ventana.resizable(False, False)

c = Canvas(ventana, width=BASE, height=ALTURA)
c.pack()

ventana.bind("<KeyPress>", mover)

dibujar()
mover_carros()

ventana.mainloop()
