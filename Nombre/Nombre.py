import turtle
nombre = turtle.Turtle()
colors=['red', 'purple', 'blue', 'green', 'yellow', 'orange', 'pink','light blue']

#Nombre:Willington
nombre.color("blue")
nombre.pu()
nombre.setposition(-500,300)
nombre.speed(10)
nombre.pensize(5)
nombre.pd()
nombre.left(270)
nombre.forward(350)
nombre.left(135)
nombre.forward(150)
nombre.right(90)
nombre.forward(150)
nombre.left(135)
nombre.forward(350)
nombre.right(180)
nombre.forward(350)
nombre.left(90)
nombre.forward(25)
nombre.left(90)
nombre.forward(50)
nombre.right(180)
nombre.forward(50)
nombre.left(90)
nombre.forward(25)
nombre.left(90)
nombre.forward(100)
nombre.right(180)
nombre.forward(100)
nombre.left(90)
nombre.forward(25)
nombre.left(90)
nombre.forward(100)
nombre.right(180)
nombre.forward(100)
nombre.left(90)
nombre.forward(25)
nombre.left(90)
nombre.forward(50)
nombre.right(180)
nombre.forward(50)
nombre.left(90)
nombre.forward(25)
nombre.left(90)
nombre.forward(50)
nombre.left(180)
nombre.forward(10)
nombre.left(90)
nombre.forward(50)
nombre.right(90)
nombre.forward(40)
nombre.left(90)
nombre.forward(50)
nombre.left(90)
nombre.forward(40)
nombre.left(90)
nombre.forward(50)
nombre.left(90)
nombre.forward(40)
nombre.left(90)
nombre.forward(50)
nombre.right(90)
nombre.forward(50)
nombre.right(90)
nombre.forward(50)
nombre.right(180)
nombre.forward(50)
nombre.left(90)
nombre.forward(50)
nombre.right(90)
nombre.forward(25)
nombre.left(90)
nombre.forward(100)
nombre.left(180)
nombre.forward(50)
nombre.right(90)
nombre.forward(25)
nombre.right(180)
nombre.forward(50)
nombre.right(90)
nombre.forward(50)
nombre.left(90)
nombre.forward(50)
nombre.left(90)
nombre.forward(50)
nombre.left(90)
nombre.forward(50)
nombre.left(180)
nombre.forward(50)
nombre.left(90)
nombre.forward(10)
nombre.left(180)
nombre.forward(10)
nombre.left(90)
nombre.forward(50)
nombre.right(90)
nombre.forward(50)
#Nombre:Andres
nombre.pu()
nombre.setposition(-500,-50)
nombre.color("orange")
nombre.pensize(5)
nombre.pd()
nombre.left(135)
nombre.forward(150)
nombre.right(90)
nombre.forward(150)
nombre.pu()
nombre.setposition(-450,0)
nombre.pd()
nombre.left(45)
nombre.forward(110)
nombre.pu()
nombre.setposition(-500,-50)
nombre.pd()
nombre.right(90)
nombre.color("black")
nombre.forward(50)
nombre.color("orange")
nombre.forward(50)
nombre.right(180)
nombre.forward(50)
nombre.right(90)
nombre.forward(50)
nombre.right(90)
nombre.forward(50)
nombre.left(90)
nombre.forward(50)
nombre.left(90)
nombre.forward(100)
nombre.left(180)
nombre.forward(50)
nombre.right(90)
nombre.forward(50)
nombre.right(180)
nombre.forward(60)
nombre.right(90)
nombre.forward(50)
nombre.right(180)
nombre.forward(60)
nombre.right(180)
nombre.forward(10)
nombre.left(90)
nombre.forward(90)
nombre.right(90)
nombre.forward(10)
nombre.right(90)
nombre.forward(50)
nombre.right(90)
nombre.forward(10)
nombre.right(180)
nombre.forward(50)
nombre.left(90)
nombre.forward(100)
nombre.left(90)
nombre.forward(25)
nombre.left(90)
nombre.forward(50)
nombre.right(90)
nombre.forward(25)
nombre.right(90)
nombre.forward(50)
#Nombre:Niño
nombre.pu()
nombre.setposition(-500,-50)
nombre.color("green")
nombre.pensize(5)
nombre.pd()
nombre.left(45)
nombre.forward(150)
nombre.right(90)
nombre.forward(150)
nombre.left(135)
nombre.forward(350)
nombre.pu()
nombre.setposition(-288,100)
nombre.pd()
nombre.left(270)
nombre.forward(25)
nombre.left(90)
nombre.forward(50)
nombre.left(180)
nombre.forward(50)
nombre.left(90)
nombre.forward(25)
nombre.left(90)
nombre.forward(50)
nombre.right(90)
nombre.forward(100)
nombre.right(90)
nombre.forward(50)
nombre.right(90)
nombre.forward(50)
nombre.right(90)
nombre.forward(50)
nombre.right(90)
nombre.pu()
nombre.setposition(-238,160)
nombre.pd()
nombre.forward(50)
#Nombre:Perez
nombre.pu()
nombre.setposition(-288,200)
nombre.color("red")
nombre.pensize(5)
nombre.pd()
nombre.left(90)
nombre.forward(100)
nombre.right(90)
nombre.forward(50)
nombre.right(90)
nombre.forward(50)
nombre.right(90)
nombre.forward(50)
nombre.right(180)
nombre.forward(100)
nombre.right(90)
nombre.forward(10)
nombre.right(90)
nombre.forward(50)
nombre.right(90)
nombre.forward(10)
nombre.right(180)
nombre.forward(50)
nombre.left(90)
nombre.forward(50)
nombre.left(180)
nombre.forward(50)
nombre.right(90)
nombre.forward(50)
nombre.right(90)
nombre.forward(60)
nombre.left(90)
nombre.forward(10)
nombre.left(180)
nombre.forward(60)
nombre.left(180)
nombre.forward(50)
nombre.right(90)
nombre.forward(90)
nombre.right(90)
nombre.forward(10)
nombre.right(90)
nombre.forward(50)
nombre.right(90)
nombre.forward(10)
nombre.right(180)
nombre.forward(50)
nombre.left(90)
nombre.forward(100)
nombre.left(180)
nombre.forward(50)
nombre.right(135)
nombre.forward(71)
nombre.left(135)
nombre.forward(50)
nombre.right(180)
#Dos lineas de medio contorno
nombre.pu()
nombre.setposition(-520,300)
nombre.color("black")
nombre.pensize(5)
nombre.pd()
nombre.right(90)
nombre.forward(500)
nombre.left(90)
nombre.forward(1000)
#Primera figura:Triangulo en espiral
nombre.pu()
nombre.setposition(170,-10)
nombre.color("black")
nombre.speed(200)
nombre.pensize(1)
f=1
nombre.pd()
nombre.ht()
while True:
    if f<=120:
        nombre.forward(f)
        nombre.left(120)
        nombre.left(1)
        f=f+1
    else:
        break
#Segunda figura: Poligono
nombre.pu()
nombre.setposition(-300,220)
nombre.pensize(1)
nombre.pd()
for i in range(200):
  nombre.color(colors[i%8])
  nombre.forward(80)
  nombre.left(50)
  nombre.speed(100)