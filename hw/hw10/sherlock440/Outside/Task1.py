class Ball():
    def __init__(self, ball_type: str = "regular"):
        self.ball_type = ball_type

    def __repr__(self):
        return f"Ball({self.ball_type})"

ball1 = Ball("super")
ball2 = Ball()

print(ball1)
print(ball2)
