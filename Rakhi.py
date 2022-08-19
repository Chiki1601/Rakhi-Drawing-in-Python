#Rakhi drawing in Python

import turtle
happy=turtle.Screen()
happy.bgcolor("black")
turtle=turtle.Turtle()
turtle.shape("turtle")
turtle.color("yellow")
turtle.width()
colors=["peru","ivory","dark orange","coral","cyan","hot pink","gold","ivory","yellow","red","pink","green","blue","light blue","light green",]



def move(x,y):
   turtle.up()
   turtle.setposition(0,0)
   turtle.setheading(90)
   turtle.rt(90)
   turtle.fd(x)
   turtle.lt(90)
   turtle.fd(y)
   turtle.pendown()
   
   
def mov(x,y):
   turtle.up()
   turtle.setposition(0,0)
   turtle.setheading(90)
   turtle.lt(90)
   turtle.fd(x)
   turtle.rt(90)
   turtle.fd(y)
   turtle.pendown()

def draw_happy(i,x,y):
    turtle.pencolor("linen")
    turtle.color(colors[i%7])
    turtle.begin_fill()
    turtle.lt(70)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(33)
    turtle.end_fill()

def f1():
   
  for i in range(7):
    turtle.pensize(5)
    turtle.pencolor('light blue')
    turtle.color(colors[i%19])
    turtle.begin_fill()
    turtle.left(330)
    turtle.forward(55)
    turtle.begin_fill()
    turtle.rt(110)
    turtle.circle(33)
    turtle.end_fill()
    turtle.rt(11)
    turtle.backward(33)
    turtle.end_fill()
   
   
def A(size):
  turtle.rt(16)
  turtle.forward(size)
  turtle.rt(150)
  turtle.fd(size)
  turtle.backward(size/2)
  turtle.rt(90)
  turtle.fd(size/3)   
  
  
def B():
   turtle.forward(70)
   turtle.rt(90)
   for i in range(18):
      turtle.rt(9)
      turtle.fd(3)
   for i in range(18):
      turtle.rt(13)
      turtle.backward(4)  
   
def H():
   turtle.fd(60)
   turtle.backward(30)
   turtle.rt(90)
   turtle.fd(30)
   turtle.lt(90)
   turtle.fd(30)
   turtle.backward(60)
   
   
def P():
   turtle.fd(60)
   turtle.rt(90)
   turtle.fd(7)
   for i in range(8):
       turtle.rt(20)
       turtle.fd(5)
       
       
def Y():
   turtle.fd(40)
   turtle.left(60)
   turtle.fd(20)
   turtle.backward(20)
   turtle.rt(90)
   turtle.fd(45)
   
   
   
def R():
   turtle.fd(60)
   turtle.rt(90)
   turtle.fd(7)
   for i in range(15):
      turtle.rt(12)
      turtle.fd(3)
   turtle.lt(120)
   turtle.fd(42)
   
   
   
def D():
   turtle.fd(60)
   turtle.rt(90)
   turtle.fd(9)
   for i in range(13):
      turtle.rt(13)
      turtle.fd(7)  
      
def K():
	turtle.fd(60)
	turtle.backward(50)
	turtle.rt(45)
	turtle.fd(50)
	turtle.backward(30)
	turtle.rt(97)
	turtle.fd(35)
	
	
def S(size):
    turtle.rt(90)
    turtle.fd(size)
    turtle.lt(90)
    turtle.fd(size)
    turtle.lt(90)
    turtle.fd(size)
    turtle.rt(90)
    turtle.fd(size)
    turtle.rt(90)
    turtle.fd(size)
      	
def N():
	turtle.fd(66)
	turtle.lt(35)
	turtle.backward(84)  
	turtle.rt(35)  
	turtle.fd(66)  
   
def i(size):
   turtle.fd(size)
      
      
#main function
turtle.speed(8)
turtle.width(9)
mov(120,200)
H()
mov(80,200)
turtle.width(5)
A(60)
mov(40,200)
P()
mov(0,200)
P()
mov(-40,200)
Y()


#Raksha Bandhan
turtle.color("cyan")
mov(325,100)
turtle.width(9)
R()
turtle.width(5)
mov(285,100)
A(60)
mov(230,100)
K()
mov(175,100)
S(30)
mov(125,100)
H()
mov(87,100)
A(60)

turtle.color("ivory")
mov(36,100)
turtle.width(9)
B()
move(4,100)
turtle.width(5)
A(60)
move(54,100)
N()
move(124,100)
D()
move(174,100)
H()
move(225,100)
A(60)
move(270,100)
N()
mov(0,0)
turtle.width(9)
turtle.rt(90)
turtle.fd(300)
turtle.backward(300)
turtle.color("cyan")
turtle.backward(300)

#rakhi
mov(20,0)
def draw_square(square):
	for i in range(0,2):
		square.forward(50)
		square.right(40)
		square.forward(40)
		square.right(140)

turtle.width(9)

def draw_flower():
	colors=['orange','yellow','hotpink','cyan','snow','baige'] 
	for i in range(0,18):
		turtle.color(colors[i%5])
		turtle.begin_fill()
		draw_square(turtle)
		turtle.end_fill()
		turtle.right(20)
draw_flower()

#bhaiya
turtle.color("yellow")
mov(110,-260)
turtle.width(9)
B()
turtle.width(5)
mov(70,-260)
H()
mov(30,-260)
A(60)
move(20,-260)
i(60)
move(50,-260)
Y()
move(70,-260)
A(60)
turtle.width(33)
move(100,500)
f1()
happy.exitonclick()
