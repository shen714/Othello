TEXT_SIZE1 = 30
TEXT_SIZE2 = 50
TEXT_COLOR = color(47, 79, 79)
RECT_COLOR = color(220, 220, 220)


class GameController:
    """Maintains the state of the game."""
    def __init__(self, WIDTH, HEIGHT, black_num, white_num):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.black_wins = False
        self.white_wins = False
        self.tie = False
        self.black_num = black_num
        self.white_num = white_num

    def update(self):
        """Carries out necessary actions if black or white wins"""
        if self.black_wins or self.white_wins or self.tie:
            textSize(TEXT_SIZE1)
            text1 = ("Black: " + str(self.black_num) + "  " + "White: " +
                     str(self.white_num))
            text_width1 = textWidth(text1)
            fill(RECT_COLOR)
            rect((self.WIDTH-text_width1)/2, self.HEIGHT/2-TEXT_SIZE2,
                 text_width1, TEXT_SIZE1+TEXT_SIZE2+20)
            fill(TEXT_COLOR)
            text(text1, (self.WIDTH-text_width1)/2, self.HEIGHT/2+TEXT_SIZE1)
            text2 = ""
            text_width2 = 0
            if self.black_wins:
                text2 = "YOU WINS!"
                text_width2 = textWidth(text2)
            if self.white_wins:
                text2 = "YOU LOSE!"
                text_width2 = textWidth(text2)
            if self.tie:
                text2 = "TIE!"
                text_width2 = textWidth(text2)
            fill(TEXT_COLOR)
            textSize(TEXT_SIZE2)
            text(text2, (self.WIDTH - text_width2)/2, self.HEIGHT/2)
