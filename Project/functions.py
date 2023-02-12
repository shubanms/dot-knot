import numpy as np
from pandas import *
import random

class gridFunc:
    def __init__(self , rows : int , columns : int , dots : int) -> None:
        self.rows = rows
        self.columns = columns
        self.dots = dots
        
    def print_grid_spacing(self , grid : list) -> None:
        grid = np.array(grid)
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in grid]))
        
    def print_grid_dataframe(self , grid : list) -> None :
        print(DataFrame(grid))
        
    def generate_random_blank_grid(self , place_holder : int) -> list:
        rows = random.randint(3,10)
        columns = random.randint(3,10)
        
        grid = [[place_holder]*columns]*rows
        
        return np.array(grid)
    
    def generate_blank_gird(self , rows : int , columns : int , place_holder : int) -> list:
        grid = [[place_holder]*columns]*rows
        
        return np.array(grid)
    
    def generate_dots_location(self) -> list:
        dot_x = random.randint(0,self.rows-1)
        dot_y = random.randint(0,self.columns-1)
        
        return [dot_x , dot_y]
    
    def generate_dots_positions(self) -> list:
        dots_positions = []
        for _ in range(self.dots * 2):
            
            x , y = map(int , self.generate_dots_location())

            while([x,y] in dots_positions):
                x , y = map(int , self.generate_dots_location())

            temp = [x,y]

            dots_positions.append(temp)
                    
        return dots_positions
    
    def group_dots(self , dots_positions : list) -> list:
        dot_positions = []
        
        for i in range(0 , len(dots_positions) , 2):
            dots_positions[i].extend(dots_positions[i+1])
            dot_positions.append(dots_positions[i])
        
        return dot_positions
    
    def place_dot(self , grid : list , dot_x : int , dot_y : int , place_holder : int) -> list:
        if(grid[dot_x][dot_y] == place_holder):
            grid[dot_y][dot_x] = place_holder
        else:
            grid[dot_x][dot_y] = place_holder

        return np.array(grid)
    
    def find_path(self , grid : list , start_dot_x : int , start_dot_y : int , end_dot_x : int , end_dot_y : int , place_holder : int) -> list:
        if(start_dot_x == end_dot_x and start_dot_y == end_dot_y):
            return 1
        
        if(grid[start_dot_x][start_dot_y] == place_holder):
            grid[start_dot_x][start_dot_y] = place_holder
            
            if(self.find_path(grid , start_dot_x-1 , start_dot_y , end_dot_x , end_dot_y , place_holder) == 1): return 1
            if(self.find_path(grid , start_dot_x , start_dot_y-1 , end_dot_x , end_dot_y , place_holder) == 1): return 1
            if(self.find_path(grid , start_dot_x+1 , start_dot_y , end_dot_x , end_dot_y , place_holder) == 1): return 1
            if(self.find_path(grid , start_dot_x , start_dot_y+1 , end_dot_x , end_dot_y , place_holder) == 1): return 1
            
            grid[start_dot_x][start_dot_y] = 0
            
        return np.array(grid)
    
    def find_path_shortest(self , grid : list , start_dot_x : int , start_dot_y : int , end_dot_x : int , end_dot_y : int , place_holder : int) -> list:
        if(start_dot_x == end_dot_x and start_dot_y == end_dot_y):
            return 1
        
        '''
        There will be eight possible places for the end dot's co-ordinates to be located at.
        They are (Clock-wise order):
        
        1. North
        2. North - East
        3. East
        4. South - East
        5. South
        6. South - West
        7. West
        8. North - West
        
        Their priority of movement will be first in the exact direction 
        for diagonal dots will take sides which are shorter first ie length
        or breadth then the reaming side 
        '''
    
if __name__ == "__main__":
    print("PASS")
