from disk import Disk


class Disks:
    """A collection of disk"""
    def __init__(self, WIDTH, HEIGHT, SIZE, game_controller):
        self.SIZE = SIZE
        self.SPACE = WIDTH/SIZE
        self.DISKSIZE = self.SPACE - 5
        self.disks = [[None]*self.SIZE for i in range(self.SIZE)]
        self.black = 0
        self.white = 0
        self.gc = game_controller
         

    def update(self):
        """Check if any part is win"""
        if self.black + self.white == self.SIZE*self.SIZE:
            if self.black > self.white:
                self.gc.black_wins = True
            elif self.white > self.black:
                self.gc.white_wins = True
            else:
                self.gc.tie = True
            self.gc.black_num = self.black
            self.gc.white_num = self.white

    def put(self, row, col, disk):
        """Put disk on the position the player click"""
        if row < self.SIZE and col < self.SIZE:
            self.disks[row][col] = disk
            if disk.color == 255:
                self.white += 1
            else:
                self.black += 1

    def init_disk(self):
        """Put the initial four disk"""
        self.put(self.SIZE/2-1, self.SIZE/2-1,
                 Disk(self.SIZE/2-1, self.SIZE/2-1, 255, self, self.DISKSIZE))
        self.put(self.SIZE/2-1, self.SIZE/2,
                 Disk(self.SIZE/2-1, self.SIZE/2, 0, self, self.DISKSIZE))
        self.put(self.SIZE/2, self.SIZE/2-1,
                 Disk(self.SIZE/2, self.SIZE/2-1, 0, self, self.DISKSIZE))
        self.put(self.SIZE/2, self.SIZE/2,
                 Disk(self.SIZE/2, self.SIZE/2, 255, self, self.DISKSIZE))

    def display(self):
        """Display the disks"""
        self.update()

        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if self.disks[i][j] is not None:
                    self.disks[i][j].display()
