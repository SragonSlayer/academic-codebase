# MinimaxTicTacToeAgent
# A game-playing tic tac toe agent that uses the minimax algorithm to produce
# a rational action.
# Lucas Swanson



# Local enum definitions
ai = 'ai'
human = 'human'

class MinimaxTicTacToeAgent:

    def __init__(self, game, symbol):
        self.game = game
        self.symbol = symbol

        try:
            if self.symbol == self.game.P1_SYMBOL:
                self.opponent_symbol = self.game.P2_SYMBOL
            else:
                self.opponent_symbol = self.game.P1_SYMBOL
        except:
            self.opponent_symbol = None

    def action(self, state):
        """
        takes in a game state and executes minimax for all possible actions, returning the next action with the best minimax value
        """
        print("MinimaxTicTacToeAgent choosing action...")
        action = None
        best_Move = float('-inf')
        for move in range(len(state)):
            if state[move] == None:
                try:
                    new_state = self.game.result(state, move)
                except (AttributeError, TypeError) as e:
                    print(f"Error: game not properly instantiated - {e}")
                    return None  # or raise an exception
                move_value = self.minimax(self.game, new_state, human)
                if move_value > best_Move:
                    best_Move = move_value
                    action = move
        return action
        




    def minimax(self, game, state, player):
        """
        recursively checks the game tree for all possible moves and returns the minimax value of the current state
        """
        if (game.no_moves_left(state)):
            if (game.is_win(state, self.symbol)):
                return 1
            elif (game.is_win(state, self.opponent_symbol)):
                return -1
            else:
                return 0
        
        if (player == ai):
            best_score = float('-inf')
            for move in range(len(state)):
                if state[move] == None:
                    new_state = game.result(state, move)
                    score = self.minimax(game, new_state, human)
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in range(len(state)):
                if state[move] == None:
                    new_state = game.result(state, move)
                    score = self.minimax(game, new_state, ai)
                    best_score = min(score, best_score)
        return best_score
        

    def max_value(self, game, state):
        """
        TODO: replace this with an appropriate docstring comment
        """
        pass

    def min_value(self, game, state):
        """
        TODO: replace this with an appropriate docstring comment
        """
        pass
