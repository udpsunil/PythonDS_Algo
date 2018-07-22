import turtle
from Command import *

class PyList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items = self.items + [item]

    # If we want to iterate over the sequence, we need to define special method called __iter__(self).
    # Without this we'll get builtin TypeError

    def __iter__(self):
        for c in self.items:
            yield c

def main():
    filename = input("Please enter drawing filename: ")

    t = turtle.Turtle()
    screen = t.getscreen()
    file = open(filename, 'r')

    # Create a pylist to hold the graphics command that are read from the file.
    graphicsCommands = PyList()

    command = file.readline().strip()

    while command != "":

        if command == "goto":
            x = float(file.readline())
            y = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            cmd = GoToCommand(x, y, width, color)
        elif command == "circle":
            radius = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            cmd = CircleCommand(radius, width, color)
        elif command == "beginfill":
            color = file.readline().strip()
            cmd = BeginFillCommand(color)
        elif command == "endfill":
            cmd = EndFillCommand()
        elif command == "penup":
            cmd = PenUpCommand()
        elif command == "pendown":
            cmd = PenDownCommand()
        else:
            raise RuntimeError("Unknown Command: " + command)
        
        graphicsCommands.append(cmd)
        command = file.readline().strip()


    for cmd in graphicsCommands:
        cmd.draw(t)

    file.close()
    t.ht()
    screen.exitonclick()
    print("Program Execution Completed.")

if __name__ == "__main__":
    main()