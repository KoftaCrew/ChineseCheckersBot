from threading import Thread
from time import sleep
import tkinter as tk

from checker_frame import CheckerFrame
from game_state import GameState

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
