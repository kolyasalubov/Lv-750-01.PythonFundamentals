# Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

class Ball(object):
    # your code goes here
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type