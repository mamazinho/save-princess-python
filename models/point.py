class Point:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __sub__(self, other):
        new_row = self.row - other.row
        new_column = self.column - other.column
        return Point(new_row, new_column)

    def __getitem__(self, position):
        return (self.row, self.column)[position]

    def __str__(self):
        return f"{self.row}, {self.column}"