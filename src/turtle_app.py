from turtle import Turtle, Vec2D


class TurtleApp:
    def __init__(self) -> None:
        self._turtle = Turtle()
        self.pinceau_actif = True
        self._turtle.pendown()

    def set_up(self):
        # Initial position: pointing upward
        self._turtle.setheading(90)

        # Bind screen events
        self.bind_screen_events()

        # Set up callbacks in the screen object
        self._turtle.screen.listen()

    def run_app(self):
        # Set up the app
        self.set_up()

        # Infinite main loop
        self._turtle.screen.mainloop()

    def bind_screen_events(self):
        self._turtle.screen.onkey(self.on_up_key_event, "Up")
        self._turtle.screen.onkey(self.on_down_key_event, "Down")
        self._turtle.screen.onkey(self.on_left_key_event, "Left")
        self._turtle.screen.onkey(self.on_right_key_event, "Right")
        self._turtle.screen.onkey(self.reset_turtle, "space")
        self._turtle.screen.onkey(self.active, "p")
        self._turtle.screen.onscreenclick(self.rosace)
        self._turtle.screen.onkey(self.rosace2, "r")


    def on_up_key_event(self):
        self._turtle.forward(10)

    def on_down_key_event(self):
        self._turtle.back(10)

    def on_left_key_event(self):
        self._turtle.left(20)

    def on_right_key_event(self):
        self._turtle.right(20)

    def reset_turtle(self):
        self._turtle.clear()
        self._turtle.teleport(0, 0)
        self._turtle.setheading(90)
        self._turtle.color("black")
        self._turtle.fillcolor("black")
    
    def active(self):
        if self.pinceau_actif:
            self._turtle.penup()
            self._turtle.color("red")
            self.pinceau_actif = False
        else :
            self._turtle.pendown()
            self._turtle.color("black")
            self.pinceau_actif=True
    
    def rosace (self, x, y):
        self._turtle.penup()
        self._turtle.teleport(x, y)
        self._turtle.pendown()
        # Drawing sequence
        self._turtle.begin_fill()
        while True:
            self._turtle.forward(150)
            self._turtle.left(140)
            if abs(self._turtle.pos() - Vec2D(x, y)) < 1:
                break
        self._turtle.end_fill()
    
    def faire_carre(self):
        for i in range( 4 ):
            self._turtle.forward(100)
            self._turtle.right(90)

    def rosace2 (self):
        self._turtle.clear()
        self._turtle.penup()
        self._turtle.teleport(0, 0)
        self._turtle.pendown()
        # Drawing sequence
        angle = 5 # en degrés
        for i in range( 360 // angle ):
            self.faire_carre()
            self._turtle.left(angle)
