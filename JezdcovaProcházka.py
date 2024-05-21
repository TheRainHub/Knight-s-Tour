import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
import sys
import keyboard

# Načíst obrázek jezdce
knightImg = mpimg.imread('bN.png')

def isValidMove(x, y, board):
    """Zkontrolovat, zda je tah platný v rámci desky a není již navštívený."""
    return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == -1

def getDegree(x, y, board):
    """Získat počet platných tahů z pozice."""
    count = 0
    for i in range(8):
        nextX = x + moveX[i]
        nextY = y + moveY[i]
        if isValidMove(nextX, nextY, board):
            count += 1
    return count

def solveKnightsTour(x, y, moveI, path, deadEnds):
    """Vyřešit problém jezdcovy procházky pomocí Warnsdorfova pravidla."""
    global solutionCount, wrongMovesCount
    if keyboard.is_pressed('space'):
        print("Program přerušen uživatelem.")
        sys.exit(0)
    
    if moveI == N * M:
        solutionCount += 1
        visualizeBoard(board, path, (x, y))
        print(f"Řešení #{solutionCount}")
        print("Gratulujeme! Řešení bylo nalezeno.")
        return True
    
    state = tuple(tuple(row) for row in board)
    if state in deadEnds:
        return False

    moves = []
    for i in range(8):
        nextX = x + moveX[i]
        nextY = y + moveY[i]
        if isValidMove(nextX, nextY, board):
            degree = getDegree(nextX, nextY, board)
            moves.append((degree, nextX, nextY))
    moves.sort()

    hasValidMoves = False
    for degree, nextX, nextY in moves:
        hasValidMoves = True
        board[nextX][nextY] = moveI
        path.append((nextX, nextY))
        visualizeBoard(board, path, (nextX, nextY))
        
        if solveKnightsTour(nextX, nextY, moveI + 1, path, deadEnds):
            return True
        else:
            board[nextX][nextY] = -1
            path.pop()
    
    if not hasValidMoves:
        wrongMovesCount += 1
        deadEnds.add(state)
    
    return False

def visualizeBoard(board, path, knightPosition):
    """Vizualizovat desku, cestu jezdce a počítadla."""
    ax.clear()
    ax.set_xticks(np.arange(M+1))
    ax.set_yticks(np.arange(N+1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(True, which='both', color='black', linestyle='-', linewidth=2)
    plt.gca().invert_yaxis()
    
    colors = ['#D18B47', '#FFCE9E']
    for i in range(N):
        for j in range(M):
            color = colors[(i + j) % 2]
            rect = patches.Rectangle((j, i), 1, 1, linewidth=0, edgecolor='none', facecolor=color)
            ax.add_patch(rect)
            if board[i][j] != -1:
                colorVal = plt.cm.plasma(board[i][j] / (N * M))
                ax.add_patch(patches.Rectangle((j, i), 1, 1, linewidth=0, edgecolor='none', facecolor=colorVal))
                ax.text(j + 0.5, i + 0.5, str(board[i][j]), color='black', ha='center', va='center')
    
    knight = OffsetImage(knightImg, zoom=0.15)
    knightBox = AnnotationBbox(knight, (knightPosition[1] + 0.5, knightPosition[0] + 0.5), frameon=False)
    ax.add_artist(knightBox)
    
    for (x, y) in path:
        circ = patches.Circle((y + 0.5, x + 0.5), 0.3, linewidth=2, edgecolor='black', facecolor='none')
        ax.add_patch(circ)
    
    ax.text(-0.5, N + 0.5, f'Řešení: {solutionCount}', fontsize=12, color='black')
    ax.text(M / 2 - 0.5, N + 0.5, f'Špatné tahy: {wrongMovesCount}', fontsize=12, color='black')
    
    plt.draw()
    plt.pause(0.5)

def main():
    """Hlavní funkce pro spuštění programu Jezdcovy procházky."""
    global N, M, moveX, moveY, board, solutionCount, wrongMovesCount, ax
    
    N = int(input("Zadejte počet řad na šachovnici (např. 8): "))
    M = int(input("Zadejte počet sloupců na šachovnici (např. 8): "))
    
    board = [[-1 for _ in range(M)] for _ in range(N)]
    solutionCount = 0
    wrongMovesCount = 0
    
    moveX = [2, 1, -1, -2, -2, -1, 1, 2]
    moveY = [1, 2, 2, 1, -1, -2, -2, -1]
    
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xticks(np.arange(M+1))
    ax.set_yticks(np.arange(N+1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(True, which='both', color='black', linestyle='-', linewidth=2)
    plt.gca().invert_yaxis()
    
    startPositions = [(N // 2, M // 2), (0, 0), (0, M - 1), (N - 1, 0), (N - 1, M - 1)]
    
    deadEnds = set()
    
    foundSolution = False
    
    for startX, startY in startPositions:
        board = [[-1 for _ in range(M)] for _ in range(N)]
        board[startX][startY] = 0
        visualizeBoard(board, [(startX, startY)], (startX, startY))
        
        if solveKnightsTour(startX, startY, 1, [(startX, startY)], deadEnds):
            foundSolution = True
            break
    
    if not foundSolution:
        print("Řešení nebylo nalezeno.")
    
    plt.show()
    
    print(f"Celkový počet nalezených řešení: {solutionCount}")
    print(f"Celkový počet špatných tahů: {wrongMovesCount}")

if __name__ == "__main__":
    main()
