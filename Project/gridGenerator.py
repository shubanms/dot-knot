import numpy as np
import random
from pandas import *
import time

class gridTester:
    def __init__(self , rows : int , columns : int , dots : int , grid : list) -> None:
        self.rows = rows
        self.columns = columns
        self.dots = dots * 2
        self.grid = grid
    
    @classmethod
    def function_timer(self , func):
        def wrapper():
            start = time.time()
            func()
            end = time.time()
            
            print(f'{func.__name__} took {end - start} seconds')
        
        return wrapper
        
    def grid_print(self , grid : list) -> None:
        grid = np.array(grid)
        print(DataFrame(grid))
        
    def place_dots(self , dots_positions : list) -> None:
        for items in dots_positions:
            self.grid[items[0]][items[1]] = 'x'
                
    def generate_dots_location(self) -> list:
        dot_x = random.randint(3,10)
        dot_y = random.randint(3,10)
        
        return [dot_x , dot_y]
   
    def generate_dots_positions(self) -> list:
        dots_positions = []
        for _ in range(self.dots):
            
            x , y = map(int , self.generate_dots_location())

            while([x,y] in dots_positions):
                x , y = map(int , self.generate_dots_location())

            temp = [x,y]

            dots_positions.append(temp)
                    
        return dots_positions
            
def check_valid_number_dots(dots : int , rows : int , columns : int) -> int:
    if(dots > max(rows , columns)+1):
        dots = dots % ((max(rows , columns)//2)+1)
    else:
        pass
    
    return dots

def make_empty_grid(rows : int , columns : int) -> list:
    
    grid = [[0]*rows]*columns
    
    return np.array(grid)

if __name__ == "__main__":
    rows = random.randint(3,10)
    columns = random.randint(3,10)
    
    number_of_dots = check_valid_number_dots(int(input("Enter the number of dots: ")) , rows , columns)
    
    grid = make_empty_grid(rows , columns)
    
    board = gridTester(rows , columns , number_of_dots , grid)
    
    dots_positions = board.generate_dots_positions()
    
    print(dots_positions)
    
    board.function_timer(board.generate_dots_positions)
    print(board.function_timer(board.generate_dots_positions))
    
    
    # board.place_dots(dots_positions)
    
    # board.grid_print(grid)
    
