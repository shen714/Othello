from board import Board
from disks import Disks
from disk import Disk
from game_controller import GameController

WIDTH = 600
HEIGHT = 600
SIZE = 8
SPACE = WIDTH/SIZE

game_controller = GameController(WIDTH, HEIGHT, 0, 0)
board = Board(WIDTH, HEIGHT, SIZE)
disks = Disks(WIDTH, HEIGHT, SIZE, game_controller)
color = "white"

def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB, 255, 255, 255)
    background(0, 100, 0)
    board.display()
    disks.init_disk()

def draw():
    disks.display()
    game_controller.update()

def mousePressed():
    global color
    row = mouseY/SPACE
    col = mouseX/SPACE
    if disks.disks[row][col] is None:
        if color == "white":
            color = "black"
            disks.put(row, col, Disk(row, col, 0, disks, disks.DISKSIZE))
        else: 
            color = "white"
            disks.put(row, col, Disk(row, col, 255, disks, disks.DISKSIZE))
