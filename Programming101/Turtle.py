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

    # for instructions in the file, loop through them and perform them
    for line in file:
        # strip the newline characters at the end of line
        text = line.strip()

        # get the command and parameters from a command line.
        commandList = text.split(',')

        # get the drawing command
        command = commandList[0]

        if command == "goto":
            x = float(commandList[1])
            y = float(commandList[2])
            width = float(commandList[3])
            color = commandList[4].strip()
            t.width(width)
            t.pencolor(color)
            t.goto(x, y)
        elif command == "circle":
            radius = float(commandList[1])
            width = float(commandList[2])
            color = commandList[3].strip()
            t.width(width)
            t.pencolor(color)
            t.circle(radius)
        elif command == "beginfill":
            color = commandList[1].strip()
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

    # close the file handle
    file.close()

    # hide the turtle that was used to draw the picture
    t.ht()

    screen.exitonclick()
    print("Program Execution Completed.")


if __name__ == "__main__":
    main()