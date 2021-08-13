from models.point import Point


class PointController:

    def create_point(self, row, column):
        return Point(row, column)