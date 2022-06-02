from threading import Thread
from time import sleep
import tkinter as tk

from checker_frame import CheckerFrame
from game_state import GameState

def getHeuristic(gameState, player: int):
    ret = 0
    if player == 0:       # white
        return ret
    elif player == 1:     # green player
        for p in gameState.map:
            if gameState.map(p) == player:
                mx = 0
                for y in range(4):
                    for x in range(4 - y):
                        dist = abs(p[0] - x) + abs(p[1] - (y + 9))
                        mx = max(mx, dist)
                ret+= mx
    else:               # red player
        for p in gameState.map:
            if gameState.map(p) == player:
                mx = 0
                for y in range(4):
                    for x in range(y + 1):
                        dist = abs(p[0] - (x - y + 8)) + abs(p[1] - (y - 4))
                        mx = max(mx, dist)
                ret+= mx
    return ret

def ThreadFunction(checkers: CheckerFrame):
    gameState = checkers.canvas.gameState
    moves = gameState.getAvailableMoves(2)
    for m in moves:
        sleep(1)
        global stopThread
        if stopThread:
            return
        
        checkers.canvas.gameState = m
        checkers.canvas.updateCircles()

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Chinese Checker")

    window.minsize(800, 600)

    checkers = CheckerFrame(window, background="white")
    
    stopThread = False
    
    checkers.canvas.gameState = GameState()
    backgroundThread = Thread(target= ThreadFunction, args= (checkers,))
    backgroundThread.start()
    
    checkers.pack(fill=tk.BOTH, expand=True)

    window.mainloop()
    
    stopThread = True
