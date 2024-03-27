import random
import turtle as t

tim = t.Turtle()
t.colormode(255)
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
          "Wheat", "SlateGray", "SeaGreen"]

directions = [0, 90, 180, 270]
tim.pensize(15)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for _ in range(100):
    tim.color(random_color())
    tim.forward(30)
    tim.right(random.choice(directions))
