import turtle
window = turtle.Screen()

def fractal(angle, position, direction=None, iterations=10):
    if iterations != 0:
        jason = turtle.Turtle()
        jason.speed(0)
        jason.left(90)
        jason.setpos(position)
        if direction == "left":
            jason.left(angle)
        elif direction == "right":
            jason.right(angle)
        jason.forward(50)
        print(iterations)
        fractal(angle//1.1, jason.pos(), direction="left", iterations=iterations-1)
        fractal(angle//1.1, jason.pos(), direction="right", iterations=iterations-1)
        
    else:
        return 0


fractal(60, (0,-100))
turtle.done()
    
