import random
import turtle as t

tim = t.Turtle()
tim.speed(20)
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for _ in range(50):
    tim.color(random_color())
    tim.right(-360 / 50)
    tim.circle(100)