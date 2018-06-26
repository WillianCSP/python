#Desenha quadrados na tela.
import turtle

def draw_square(some_turtle):
        for i in range(1,5):
                some_turtle.forward(200)
                some_turtle.right(90)

def draw_square_esq(some_turtle):
        for i in range(1,4):
                some_turtle.forward(200)
                some_turtle.left(90)                

def draw_art():
        window = turtle.Screen()
        window.bgcolor("red")
        brad  =turtle.Turtle()
        brad.shape("turtle")
        brad.color("yellow")
        brad.speed(12)#altera velocidade
        #angie = turtle.Turtle()
        #angie.shape("arrow")
        #angie.color("blue")
        #angie.speed(8)
        #angie.circle(100)
        #angie.forward(100)
        #angie.left(100)
        for i in range(1,148):
                draw_square(brad)
                brad.right(2.5)
                if(i%2==0):
                        brad.color("yellow")
                elif(i%2!=0):
                        brad.color("blue")
                #draw_square_esq(angie)
                #angie.left(5)

        window.exitonclick()

draw_art()
