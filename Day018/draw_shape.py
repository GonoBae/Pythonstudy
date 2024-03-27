import random
import turtle as t

tim = t.Turtle()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
          "Wheat", "SlateGray", "SeaGreen"]

def draw_shape(num):
    angle = 360 / num
    for _ in range(num):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)
