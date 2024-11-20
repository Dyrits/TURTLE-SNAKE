from turtle import Turtle

class Direction(float):
    UP = 90.0
    DOWN = 270.0
    RIGHT = 0.0
    LEFT = 180.0


def build(color):
    part = Turtle("square")
    part.color(color)
    part.penup()
    return part

class Snake:
    def __init__(self):
        self.body = []
        self.head = build("red")
        self.body.append(self.head)
        self.create()

    def create(self):
        for index in range(1, 3):
            part = build("black")
            part.goto(-20 * index, 0)
            self.body.append(part)

    def grow(self):
        part = Turtle("square")
        part.penup()
        tail = self.body[-1]
        part.goto(tail.position())
        self.body.append(part)

    def move(self):
        for index in range(len(self.body) - 1, 0, -1):
            self.body[index].goto(self.body[index - 1].xcor(), self.body[index - 1].ycor())
        self.body[0].forward(20)

    def up(self):
        if self.head.heading() != Direction.DOWN:
            self.head.setheading(Direction.UP)

    def down(self):
        if self.head.heading() != Direction.UP:
            self.head.setheading(Direction.DOWN)

    def right(self):
        if self.head.heading() != Direction.LEFT:
            self.head.setheading(Direction.RIGHT)

    def left(self):
        if self.head.heading() != Direction.RIGHT:
            self.head.setheading(Direction.LEFT)

    def collide(self):
        for part in self.body[1:]:
            if self.head.distance(part) < 10:
                return True
        return False