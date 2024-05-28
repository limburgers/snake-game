from tkinter import *
import random

snake_color = "#50C878"
apple_color = "#FF0000"
background_color = "#000000"

window_width = 700
window_height = 700

speed = 50
size = 50
snake_size = 2

class Snake:
    def __init__(self):
        self.coordinates = []
        self.body_size = snake_size
        self.squares = []

        for i in range(0, snake_size):
            self.coordinates.append([0, 0])

        for x,y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + size, y + size, fill=snake_color)
            self.squares.append(square)


class Apple:
    def __init__(self):
        y = random.randint(0, (window_height / size) - 1) * size
        x = random.randint(0, (window_width/size)-1) * size

        self.coordinates = [x, y]

        canvas.create_rectangle(x, y, x + size, y + size, fill=apple_color, tag="food")


def direction_(event):

    global direction
    nDirection = event.keysym

    if nDirection == 'Right':
        if direction != 'Left':
            direction = nDirection
    elif nDirection == 'Left':
        if direction != 'Right':
            direction = nDirection
    elif nDirection == 'Up':
        if direction != 'Down':
            direction = nDirection
    elif nDirection == 'Down':
        if direction != 'Up':
            direction = nDirection

def turn(snake, food):

    x, y = snake.coordinates[0]

    if direction == 'Right':
        x+= size

    elif direction == 'Left':
        x -= size

    elif direction == 'Up':
        y-= size

    elif direction == 'Down':
        y += size


    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + size, y + size, fill=snake_color)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global scoreApple
        scoreApple += 1
        label.config(text="{}".format(scoreApple))

        canvas.delete("food")
        food = Apple()


    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if crash(snake):
        end_game()

    window.after(speed, turn, snake, food)

def crash(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >+ window_width:
        return True
    elif y < 0 or y >+ window_height:
        return True

    for body in snake.coordinates[1:]:
        if x == body[0] and y == body[1]:
            print("a")
            return True

def end_game():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('arial', 35), text="You Lose!", fill="orange")



window = Tk()
window.title("Python Snake Game!")

scoreApple = 0
direction = 'Down'

label = Label(window, text="{}".format(scoreApple), font=('arial', 35))
label.pack()

canvas = Canvas(window, background=background_color, width=window_width, height=window_height)
canvas.pack()


window.bind('<Up>', direction_)
window.bind('<Down>', direction_)
window.bind('<Left>', direction_)
window.bind('<Right>', direction_)

snake = Snake()
food = Apple()

turn(snake, food)

window.mainloop()
