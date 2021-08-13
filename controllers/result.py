class ResultController:

    def view_trace(self, me, princess):
        my_path_to_princess = princess - me
        list_of_moves = []
        if my_path_to_princess.row > 0:
            list_of_moves.extend(["DOWN"] * abs(my_path_to_princess.row))
        if my_path_to_princess.row < 0:
            list_of_moves.extend(["UP"] * abs(my_path_to_princess.row))
        if my_path_to_princess.column > 0:
            list_of_moves.extend(["RIGTH"] * abs(my_path_to_princess.column))
        if my_path_to_princess.column < 0:
            list_of_moves.extend(["LEFT"] * abs(my_path_to_princess.column))
        if not list_of_moves:
            list_of_moves.append("STAY")

        return my_path_to_princess, list_of_moves
