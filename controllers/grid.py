from models.grid import Grid

class GridController:

    def __init__(self):
        self.grid = None

    def create_grid(self, grid_rows, grid_columns):
        self.grid = Grid(grid_rows, grid_columns)
        return self.grid
    
    def has_someone_here(self, me, princess, actual_place):
        if me.row == actual_place.row and me.column == actual_place.column:
            value = "m"
        elif princess.row == actual_place.row and princess.column == actual_place.column:
            value = "p"
        else:
            value = "-"

        return value

    def get_grid_size(self):
        return self.grid.row, self.grid.column
