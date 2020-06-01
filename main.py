from browser import document, html
import math

canvas = document["zone8"]
ctx = canvas.getContext("2d")

x = 20

def draw(event):
    global x
    ctx.beginPath()
    ctx.arc(x, 25, 15, 0, 2 * math.pi)
    x += 15
    ctx.stroke()

document["button8"].bind("click", draw)