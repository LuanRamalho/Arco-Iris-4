from turtle import *

def main():
    rainbow = ("violet" , "indigo" , "blue" , "green" , "yellow" , "orange" , "red")
    pu()
    goto(-320,-195)
    width(70)

    for i in rainbow:
        color(i)
        down()
        fd(840)
        up()
        bk(840)
        lt(90)
        fd(66)
        rt(90)

    writer = Turtle()
    writer.ht()
    writer.pencolor('white')
    writer.write("Rainbow Colour", align="center", font=("Arial" , 56 , ("bold" , "italic")))

main()
mainloop()