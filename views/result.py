from controllers.result import ResultController

class ResultView:

    def __init__(self):
        self.result_controller = ResultController()

    def show_results(self, me, princess, grid):
        my_path_to_princess, moves = self.result_controller.view_trace(me, princess)
        print(f"PRINCESS: {princess} || ME: {me}")
        print("RESULT: ", my_path_to_princess)
        print("MOVES: ", moves)
        print("SCORE: ", (grid.row * grid.column) * len(moves) / 10)