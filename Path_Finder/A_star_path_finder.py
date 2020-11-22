import pygame
import math
from queue import PriorityQueue

dimensions = 500
window = pygame.display.set_mode((dimensions, dimensions))
pygame.display.set_caption("A* Path Finder")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK  = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Cell:
    def __init__(self, row, column, width, total_rows):
        self.row = row
        self.column = column
        self.x = row*width      #x dimension 
        self.y = column*width   #y dimensions
        self.colour = WHITE
        self.neighbours = []
        self.width = width      #width is WIDTH/(NUMBER OF CELLS)
        self.total_rows = total_rows

    def get_pos(self): #to get the row and column number
        return self.row, self.column

    def is_closed(self): #closed set cell
        return self.colour == RED
    
    def is_open(self):
        return self.colour == GREEN
    
    def is_barrier(self):
        return self.colour == BLACK
    
    def is_start(self):
        return self.colour == ORANGE
    
    def is_end(self):
        return self.colour == TURQUOISE
    
    def reset_cell(self):
        self.colour = WHITE

    def make_closed(self):
        self.colour = RED
    
    def make_open(self):
        self.colour = GREEN

    def make_barrier(self):
        self.colour = BLACK
    
    def make_end(self):
        self.colour = TURQUOISE

    def make_start(self):
        self.colour = ORANGE

    def make_path(self):
        self.colour = PURPLE
    
    def draw(self, window):
        pygame.draw.rect(window, self.colour, (self.x, self.y, self.width, self.width))

    def update_neighbours(self, grid):
        self.neighbours = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.column].is_barrier(): #Down cell
            self.neighbours.append(grid[self.row + 1][self.column]) 
        
        if self.row > 0 and not grid[self.row - 1][self.column].is_barrier(): #Up cell
            self.neighbours.append(grid[self.row - 1][self.column])
        
        if self.column < self.total_rows - 1 and not grid[self.row][self.column + 1].is_barrier(): #Left cell
            self.neighbours.append(grid[self.row][self.column + 1])
        
        if self.column > 0 and not grid[self.row][self.column - 1].is_barrier(): #Right cell
            self.neighbours.append(grid[self.row][self.column - 1])
        
    def less_than(self, other):
        return False

def H(p1, p2): #Heuristics function calculated using Manhattan distance
     x1, y1 = p1
     x2, y2 = p2
     return abs(x1 - x2) + abs(y1 - y2)

def path_construct(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue() #efficient to get the minimum element from this queue
    open_set.put((0, count, start))
    came_from = {} #Last node dictionary
    G = {cell: float("inf") for row in grid for cell in row} #keeps track of current distances
    G[start] = 0
    F = {cell: float("inf") for row in grid for cell in row} #keeps track of predictive distances
    F[start] = H(start.get_pos(), end.get_pos())

    open_set_hash = {start} #keeps track of items in and not in PriorityQueue

    while not open_set.empty(): #runs till open set is emptied out
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            path_construct(came_from, end, draw)
            start.make_start()
            end.make_end()
            return True

        for neighbour in current.neighbours:
            temp_G = G[current] + 1

            if temp_G < G[neighbour]:
                came_from[neighbour] = current
                G[neighbour] = temp_G
                F[neighbour] = temp_G + H(neighbour.get_pos(), end.get_pos())
                if neighbour not in open_set_hash:
                    count += 1
                    open_set.put((F[neighbour], count, neighbour))
                    open_set_hash.add(neighbour)
                    neighbour.make_open()
        
        draw()
        if current != start:
            current.make_closed() 

    return False



def make_grid(rows, dimensions):
    grid = []
    gap = dimensions // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            cell = Cell(i, j, gap, rows)
            grid[i].append(cell)

    return grid

def draw_grid(window, rows, dimensions):
    gap = dimensions // rows
    for i in range(rows):
        pygame.draw.line(window, GREY, (0, i * gap), (dimensions, i * gap))
    for j in range(rows):
        pygame.draw.line(window, GREY, (j * gap, 0), (j * gap, dimensions))
     
def draw(windows, grid, rows, dimensions):
    window.fill(WHITE)

    for row in grid:
        for cell in row:
            cell.draw(window)
    draw_grid(window, rows, dimensions)
    pygame.display.update()

def get_clicked_position(pos, rows, dimensions):
    gap = dimensions // rows
    y, x = pos

    row = y // gap
    column = x // gap
    return row, column

def main(window, dimensions):
    ROWS = 50
    grid = make_grid(ROWS, dimensions)

    start = None
    end = None

    run = True
    started = False
    while run:
        draw(window, grid, ROWS, dimensions)
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                run = False
            if started:
                continue
            
            if pygame.mouse.get_pressed()[0]: #left mouse click
                pos = pygame.mouse.get_pos()
                row, column = get_clicked_position(pos, ROWS, dimensions)
                cell = grid[row][column]
                
                if not start and cell != end: #initializing start point
                    start = cell
                    start.make_start()
                elif not end and cell != start: #initializing end point
                    end = cell
                    end.make_end()
                elif cell != end and cell != start:
                    cell.make_barrier()

            elif pygame.mouse.get_pressed()[2]:  #right mouse click
                pos = pygame.mouse.get_pos()
                print(pos)
                row, column = get_clicked_position(pos, ROWS, dimensions)
                cell = grid[row][column]
                cell.reset_cell()

                if cell == start:
                    start = None
                elif cell == end:
                    end = None
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for cell in row:
                            cell.update_neighbours(grid)

                    algorithm(lambda: draw(window, grid, ROWS, dimensions), grid, start, end)   
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, dimensions)
    pygame.quit()

main(window, dimensions)
