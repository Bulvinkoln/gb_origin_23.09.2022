import turtle
import random
import time

# экран
wn = turtle.Screen()
wn.title('Star Fleet')
wn.setup(600, 600)
wn.bgcolor('black')
wn.tracer(0)

# фон
dec = turtle.Turtle()
dec.speed(0)
dec.color('white')
dec.hideturtle()
dec.penup()
dec.goto(1920, 1080)
dec.pendown()
dec.goto(-1920, 1080)
dec.goto(-1920, -1080)
dec.goto(1920, -1080)
dec.goto(1920, 1080)


for i in range(1000):
    dec.penup()
    dec.goto(random.randint(-1920, 1080), random.randint(-1920, 1080))
    dec.pendown()
    dec.circle(random.randint(1, 3))
dec.penup()
dec.goto(600, 600)

# Главный герой внешка
mc = turtle.Turtle()
mc.speed(0)
mc.color('white')
mc.shape('arrow')
mc.shapesize(1, 2, 0)
mc.penup()
mc.direction = 'stop'

# Пират внешка
klr = turtle.Turtle()
klr.speed(0)
klr.color('red')
klr.shape('arrow')
klr.shapesize(3)
klr.penup()
klr.goto(2000, 2000)

#золото внешка 
coin = turtle.Turtle()
coin.speed(0)
coin.color('gold')
coin.shape('circle')
coin.penup()
coin.goto(random.randint(-1920, 1080), random.randint(-1920, 1080))

health = 10
score = 0
hidh_score = 0
delay = 0.1
x = 0
y = 0

# результат
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.goto(0, 260)
pen.write(f'Cчёт: {score} Рекорд: {hidh_score} Здоровье: {health}', align = 'center', font = ('Courier', 24, 'normal'))

#управление с клавиатуры

def move_up():
    mc.direction = 'Up'
    mc.setheading(90)

def move_down():
    mc.direction = 'Down'
    mc.setheading(270)

def move_right():
    mc.direction = 'Right'
    mc.setheading(0)

def move_left():
    mc.direction = 'Left'
    mc.setheading(180)

def check():
    if mc.direction == 'Up':
        y = mc.ycor()
        mc.sety(y + 20)
    if mc.direction == 'Down':
        y = mc.ycor()
        mc.sety(y - 20)
    if mc.direction == 'Right':
        x = mc.xcor()
        mc.setx(x + 20)
    if mc.direction == 'Left':
        x = mc.xcor()
        mc.setx(x - 20)

wn.listen()
wn.onkeypress(move_up, 'w')
wn.onkeypress(move_down, 's')
wn.onkeypress(move_right, 'd')
wn.onkeypress(move_left, 'a')

while True:
    wn.update()
    
    pen.write(f'Cчёт: {score} Рекорд: {hidh_score} Здоровье: {health}', align = 'center', font = ('Courier', 24, 'normal'))

    if mc.xcor() > 960 or mc.xcor() < -960 or mc.ycor() > 540 or mc.ycor() < -540:
        time.sleep(1)
        mc.direction = 'stop'
        mc.goto(0, 0)
        klr.goto(2000, 1000)
        health += 5
        
        score = 0
        pen.clear()
        pen.write(f'Cчёт: {score} Рекорд: {hidh_score} Здоровье: {health}', align = 'center', font = ('Courier', 24, 'normal'))   
        
        check()

    if mc.distance(coin) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        coin.goto(x, y)

        score += 10
        if score > hidh_score:
            hidh_score = score
        pen.clear()

    if score >= 50:
        klr.showturtle()
        klr.setheading(klr.towards(mc.xcor(), mc.ycor()))
        if score <= 100:
            klr.fd(5)
        elif score >= 100:
            klr.fd(10)
        elif score >= 150:
            klr.fd(15)
        elif score >= 200:
            klr.fd(20)
        
        if klr.distance(mc) < 25:
            #time.sleep(1)
            #mc.direction = 'stop'
            #mc.goto(0, 0)
            #klr.goto(400, 400)
        
            #score = 0
            #pen.clear()
            #pen.write(f'Cчёт: {score} Рекорд: {hidh_score} Здоровье: {health}', align = 'center', font = ('Courier', 24, 'normal'))
            mc_xcor = mc.xcor()
            mc_ycor = mc.ycor()
            klr.goto(mc_xcor - 100, mc_ycor - 100)
            health -= 1
            pen.clear()
    
    if health <= 0:
        time.sleep(1)
        mc.direction = 'stop'
        mc.goto(0, 0)
        klr.goto(2000, 1000)
        health += 5
        
        score = 0
        pen.clear()
        pen.write(f'Cчёт: {score} Рекорд: {hidh_score} Здоровье: {health}', align = 'center', font = ('Courier', 24, 'normal'))   
        
        check()

    pen.write(f'Cчёт: {score} Рекорд: {hidh_score} Здоровье: {health}', align = 'center', font = ('Courier', 24, 'normal'))

    time.sleep(delay)

wn.mainloop()