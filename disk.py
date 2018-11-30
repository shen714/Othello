class Disk:
    """A disk"""
    def __init__(self, row, col, color, disks, radius):
        self.row = row
        self.col = col
        self.color = color
        self.disks = disks
        self.x = self.col * disks.SPACE + disks.SPACE/2
        self.y = self.row * disks.SPACE + disks.SPACE/2
        self.radius = radius

    def display(self):
        """Draws the disk"""
        fill(self.color)
        ellipse(self.x, self.y, self.radius, self.radius)
