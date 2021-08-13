import sys
from views.grid import GridView
from views.point import PointView
from views.result import ResultView

class Main:
    def __init__(self):
        self.point = PointView()
        self.grid = GridView()
        self.result = ResultView()
        self.start()
    
    def start(self):
        try:
            grid_size = self.grid.get_grid_size()
            me = self.point.get_my_position()
        except:
            print("Insira um valor válido para as grades e para sua posição")
            sys.exit()

        self._validate_position_on_grid(grid_size, me)

        princess = self.point.get_princess_position(grid_size)

        self.grid.draw(me, princess)
        self.result.show_results(me, princess, grid_size)
    

    def _validate_position_on_grid(self, grid_size, position):
        human_readable_position_row = position.row + 1
        human_readable_position_column = position.column + 1
        if not (
            0 < human_readable_position_row < grid_size.row and
            0 < human_readable_position_column < grid_size.column            
        ):
            print("Sua posição excede os limites da grade colocada")
            sys.exit()


if __name__ == '__main__':
    Main()