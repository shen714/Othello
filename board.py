from disk import Disk


class Board:
    """Draws the board"""
    def __init__(self, WIDTH, HEIGHT, SIZE):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SIZE = SIZE
        self.SPACE = WIDTH/self.SIZE

    def display(self):
        """Displays the board"""
        # Draw the line
        for line_num in range(self.SIZE):
            line(line_num*self.SPACE, 0, line_num*self.SPACE, self.HEIGHT)
            line(0, line_num*self.SPACE, self.WIDTH, line_num*self.SPACE)
