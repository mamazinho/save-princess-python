from controllers.point import PointController
from controllers.grid import GridController

class GridView:

    def __init__(self):
        self.grid_controller = GridController()
        self.point_controller = PointController()

    def get_grid_size(self):
        grid_rows = int(input("Quantas linhas a grade deve ter? "))
        grid_columns = int(input("Quantas colunas a grade deve ter? "))
        grid = self.grid_controller.create_grid(grid_rows, grid_columns)

        return grid

    def draw(self, me, princess):
        row_limit, column_limit = self.grid_controller.get_grid_size()
        grid = {}
        for row in range(0, row_limit):
            grid[row] = {}
            for column in range(0, column_limit):
                actual_place = self.point_controller.create_point(row, column)
                has_someone = self.grid_controller.has_someone_here(me, princess, actual_place)
                grid[row][column] = has_someone
        
        for lines in grid.values():
            print(" ".join(list(lines.values())))

