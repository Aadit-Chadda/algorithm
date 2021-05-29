# importing packages and plugins
import pygame
import math
from queue import PriorityQueue

# Creating window
WIDTH = 800
window = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A-Start Search")

# Color codes for path determination
RED = (225, 0, 0)
GREEN = (0, 225, 0)
BLUE = (0, 225, 0)
YELLOW = (225, 225, 0)
WHITE = (225, 225, 225)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (225, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


# Defining Game Class
class Node:
    # Initiating  base
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = width
        self.y = width
        self.color = WHITE
        self.neighbour = []
        self.width = width
        self.total_rows = total_rows
    
    # Getting position of node
    def get_position(self):
        return self.row, self.col
    
    # Defining which nodes have been checked before
    def is_closed(self):
        return self.color == RED
    
    # Defining if a node is open
    def is_open(self):
        return self.color == GREEN
    
    # Defining the barrier(End-point) of nodes
    def is_barrier(self):
        return self.color == BLACK
    
    # Defining the START Node
    def is_start(self):
        return self.color == WHITE
    
    # Defining the END Node
    def is_end(self):
        return self.color == PURPLE
    
    # Resetting Node value
    def reset(self):
        self.color = WHITE
    
    # Making closed nodes
    def make_closed(self):
        self.color = RED
    
    # Making barrier nodes
    def make_barrier(self):
        self.color = BLACK
    
    # Making Start Node
    def make_start(self):
        self.color = ORANGE
    
    # Making the end-node
    def make_end(self):
        self.color = TURQUOISE
    
    # Defining the Path of Search
    def make_path(self):
        self.color = PURPLE
    
    # Re-presentation on screen
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
    
    # Tracking Node neighbours
    def update_neighbour(self, grid):
        pass
    
    # Defining Less Than Node
    def __lt__(self, other):
        return False


# Defining the heuristic function of AI A* Search path finding algorithm
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def make_grid(row, width):
    grid = []
    gap = width // row
    
    for i in range(row):
        grid.append([])
        for j in range(row):
            node = Node(i, j, gap, row)
            grid[i].append(node)
    return grid


def draw_grid(win, row, width):
    gap = width // row
    for i in range(row):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
    for j in range(row):
        pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


def draw_this(win, grid, row, width):
    window.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(win)
    
    draw_grid(win, row, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    
    row = y // gap
    col = x // gap
    
    return row, col


def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)
    
    start = None
    end = None
    
    run = True
    started = False
    while run:
        draw_this(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                run = False
            
            if started:
                continue
            
            if event.mouse.get_pressed()[0]: # Left Click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                if not start:
                    start = node
                    start.make_start()
                elif not end:
                    end = node
                    end.make_end()
                elif node != end and node != start:
                    node.make_barrier()
            
            elif pygame.mouse.get_pressed()[2]: # Right Click
                pass
    
    pygame.quit()


main(window, width)
