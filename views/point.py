from random import randint
from controllers.point import PointController


class PointView:

    def __init__(self):
        self.point_controller = PointController()

    def get_princess_position(self, grid_size):
        princess_row, princess_column = self._get_random_position(grid_size.row, grid_size.column)
        princess = self.point_controller.create_point(princess_row, princess_column)
        return princess

    def get_my_position(self):
        my_row = int(input("Em que linha você quer estar quando iniciar? ")) - 1
        my_column = int(input("Em que coluna você quer estar quando iniciar? ")) - 1

        me = self.point_controller.create_point(my_row, my_column)
        return me

    def _get_random_position(self, row_limit, column_limit):
        return randint(0, row_limit), randint(0, column_limit)