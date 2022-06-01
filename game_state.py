from mimetypes import init


class GameState:
    def __init__(self) -> None:
        self.map = {}
        # Green
        for y in range(4):
            for x in range(y + 1):
                self.map[(x - y + 8), y - 4] = 1
        # Blue
        for y in range(4):
            for x in range(4 - y):
                self.map[(x, y)] = 2
        # Purple
        for y in range(4):
            for x in range(y + 1):
                self.map[(x - y - 1), y + 5] = 3
        # Red
        for y in range(4):
            for x in range(4 - y):
                self.map[(x, y + 9)] = 4
        # Orange
        for y in range(4):
            for x in range(y + 1):
                self.map[(x - y + 8), y + 5] = 5
        # Yellow
        for y in range(4):
            for x in range(4 - y):
                self.map[(x+9, y)] = 6
        # White
        for y in range(5):
            for x in range(y + 5):
                self.map[(x - y + 4, y)] = 0
        for y in range(4):
            for x in range(8 - y):
                self.map[(x, y + 5)] = 0

    def getAvailableMoves(self, player: int) -> list:
        pass
