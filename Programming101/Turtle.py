import turtle

def main():
    # the main code of the program
    # read file path from user
    filename = input("Please enter drawing filename: ")

    # Create a turtle graphic window to draw in
    t = turtle.Turtle()

    # Create a screen
    screen = t.getscreen()

    # Open the file in readonly mode
    file = open(filename, 'r')

    command = file.readline().strip()

    # If the command is empty, then there are no more commands left in the file.
    while command != "":
        
        # Read the rest of the record and then process it.

        if command == "goto":
            x = float(file.readline())
            y = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            t.width(width)
            t.pencolor(color)
            t.goto(x, y)
        elif command == "circle":
            radius = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            t.width(width)
            t.pencolor(color)
            t.circle(radius)
        elif command == "beginfill":
            color = file.readline().strip()
            t.fillcolor(color)
            t.begin_fill()
        elif command == "endfill":
            t.end_fill()
        elif command == "penup":
            t.penup()
        elif command == "pendown":
            t.pendown()
        else:
            print("Unknown command found in file:", command)

        command = file.readline().strip()

    # close the file handle
    file.close()

    # hide the turtle that was used to draw the picture
    t.ht()

    screen.exitonclick()
    print("Program Execution Completed.")


if __name__ == "__main__":
    main()