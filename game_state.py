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
                self.map[(x, y)] = 0
        # Purple
        for y in range(4):
            for x in range(y + 1):
                self.map[(x - y - 1), y + 5] = 0
        # Red
        for y in range(4):
            for x in range(4 - y):
                self.map[(x, y + 9)] = 2
        # Orange
        for y in range(4):
            for x in range(y + 1):
                self.map[(x - y + 8), y + 5] = 0
        # Yellow
        for y in range(4):
            for x in range(4 - y):
                self.map[(x+9, y)] = 0
        # White
        for y in range(5):
            for x in range(y + 5):
                self.map[(x - y + 4, y)] = 0
        for y in range(4):
            for x in range(8 - y):
                self.map[(x, y + 5)] = 0

    def getAvailableMoves(self, currentPlayer: int) -> list[tuple['GameState', tuple[int, int], tuple[int, int]]]:
        result: list[GameState] = []
        map = self.map

        myMarbles = []
        # Get marbles
        for cord, player in map.items():
            if player == currentPlayer:
                myMarbles.append(cord)

        for cords in myMarbles:
            moveCords = self.getMarbleMoves(cords)
            result.extend([(self.moveMarble(cords, x), cords, x) for x in moveCords])

        return result

    def getMarbleMoves(self, cords) -> list[tuple[int, int]]:
        result = []

        x, y = cords
        map = self.map
        # Normal moves
        if map.get((x, y - 1)) == 0:
            result.append((x, y - 1))
        if map.get((x + 1, y - 1)) == 0:
            result.append((x + 1, y - 1))
        if map.get((x - 1, y)) == 0:
            result.append((x - 1, y))
        if map.get((x + 1, y)) == 0:
            result.append((x + 1, y))
        if map.get((x - 1, y + 1)) == 0:
            result.append((x - 1, y + 1))
        if map.get((x, y + 1)) == 0:
            result.append((x, y + 1))

        # Hop moves
        visited = {(x, y)}
        toVisit = set()

        if map.get((x, y - 1), 0) != 0 and map.get((x, y - 2)) == 0:
            toVisit.add((x, y - 2))
        if map.get((x + 1, y - 1), 0) != 0 and map.get((x + 2, y - 2)) == 0:
            toVisit.add((x + 2, y - 2))
        if map.get((x - 1, y), 0) != 0 and map.get((x - 2, y)) == 0:
            toVisit.add((x - 2, y))
        if map.get((x + 1, y), 0) != 0 and map.get((x + 2, y)) == 0:
            toVisit.add((x + 2, y))
        if map.get((x - 1, y + 1), 0) != 0 and map.get((x - 2, y + 2)) == 0:
            toVisit.add((x - 2, y + 2))
        if map.get((x, y + 1), 0) != 0 and map.get((x, y + 2)) == 0:
            toVisit.add((x, y + 2))

        while len(toVisit) != 0:
            m = toVisit.pop()
            if m in visited:
                continue

            result.append(m)
            visited.add(m)
            x1, y1 = m

            if map.get((x1, y1 - 1), 0) != 0 and map.get((x1, y1 - 2)) == 0:
                toVisit.add((x1, y1 - 2))
            if map.get((x1 + 1, y1 - 1), 0) != 0 and map.get((x1 + 2, y1 - 2)) == 0:
                toVisit.add((x1 + 2, y1 - 2))
            if map.get((x1 - 1, y1), 0) != 0 and map.get((x1 - 2, y1)) == 0:
                toVisit.add((x1 - 2, y1))
            if map.get((x1 + 1, y1), 0) != 0 and map.get((x1 + 2, y1)) == 0:
                toVisit.add((x1 + 2, y1))
            if map.get((x1 - 1, y1 + 1), 0) != 0 and map.get((x1 - 2, y1 + 2)) == 0:
                toVisit.add((x1 - 2, y1 + 2))
            if map.get((x1, y1 + 1), 0) != 0 and map.get((x1, y1 + 2)) == 0:
                toVisit.add((x1, y1 + 2))

        return result

    def moveMarble(self, initial, next) -> 'GameState':
        result = GameState()
        result.map = self.map.copy()
        temp = result.map[initial]
        result.map[initial] = result.map[next]
        result.map[next] = temp

        return result

    def getHeuristic(self) -> int:
        xr = 0
        yr = 12
        xg = 8
        yg = -4
        HR = 0
        HG = 0
        for cords, p in self.map.items():
            if p == 1:
                HG += abs(cords[0] - xr) + abs(cords[1] - yr)
            elif p == 2:
                HR += abs(cords[0] - xg) + abs(cords[1] - yg)
        return HR - HG

    def winCondition(self) -> int:
        #topside
        topSideFull=True
        botSideFull=True
        redWin=False
        greenWin=False
        for y in range(4):
            for x in range(y + 1):
                # self.map[(x - y + 8), y - 4] = 1
                if(topSideFull):
                    if(self.map[(x - y + 8), y - 4] ==0):
                        topSideFull=False
                    elif(self.map[(x - y + 8), y - 4]==2):
                        redWin=True
        if(topSideFull and redWin):
            return 2
        
        #botside
        for y in range(4):
            for x in range(4 - y):
                # self.map[(x, y + 9)] = 2
                if(botSideFull):
                    if(self.map[(x, y + 9)]==0):
                        botSideFull=False
                    elif(self.map[(x, y + 9)]==1):
                        greenWin=True
        if(botSideFull and greenWin):
            return 1
        
        return 0

    def alphaBetaSearch(self, depth: int) -> tuple[tuple[int, int], tuple[int, int]]:
        def minValue(state: GameState, alpha: int, beta: int, depth: int) -> tuple[int, tuple[int, int], tuple[int, int]]:
            if state.winCondition() == 1:
                return float('inf'), None, None
            elif state.winCondition() == 2:
                return float('-inf'), None, None
            elif depth == 0:
                return state.getHeuristic(), None, None
            
            v = float('inf')
            for s, initial, next in state.getAvailableMoves(1):
                v = min(v, maxValue(s, alpha, beta, depth - 1)[0])
                
                if v <= alpha:
                    return v, initial, next
                beta = min(v, alpha)

            return v, initial, next

        def maxValue(state: GameState, alpha: int, beta: int, depth: int) -> tuple[int, tuple[int, int], tuple[int, int]]:
            if state.winCondition() == 1:
                return float('inf'), None, None
            elif state.winCondition() == 2:
                return float('-inf'), None, None
            elif depth == 0:
                return state.getHeuristic(), None, None
            
            v = float('-inf')
            for s, initial, next in state.getAvailableMoves(1):
                v = max(v, minValue(s, alpha, beta, depth - 1)[0])
                
                if v >= beta:
                    return v, initial, next
                alpha = max(v, alpha)

            return v, initial, next
        
        h, initial, next = maxValue(self, float('-inf'), float('inf'), depth)
        print(h)

        return initial, next
