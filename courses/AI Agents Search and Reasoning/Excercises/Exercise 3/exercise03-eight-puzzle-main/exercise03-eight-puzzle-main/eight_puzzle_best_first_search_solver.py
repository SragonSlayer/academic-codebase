# EightPuzzleBestFirstSearchSolver: A problem solver for the eight-puzzle problem
# that can apply best-first search to find a solution node. This class encapsulates
# a best-first search algorithm and an evaluation function. It encapsulates the
# application of the algorithm to the problem, and in the end can produce a
# solution, which is a list of actions.
# YOUR NAME


from queue import PriorityQueue
from eight_puzzle_node import EightPuzzleNode
from eight_puzzle_agent import EightPuzzleAgent

class EightPuzzleBestFirstSearchSolver:

    def solution(self, problem):
        """
        Return a list of EightPuzzleAgent actuator methods. If the problem
        initial state is the same as the goal state, return an empty list.
        """
        solution_node = self.best_first_search(problem,
            self.cost_so_far_plus_estimated_cost_remaining)
        if solution_node == []:
            return []
        elif solution_node:
            return self.actions_to_reach_solution_node(solution_node)
        else:
            return None

    def best_first_search(self, problem, evaluation_function):
        """
        Return a solution EightPuzzleNode, or None to indicate failure.
        """
        if (problem.initial_state == problem.goal_state):
            return []
        elif (problem.initial_state != problem.goal_state):
            node = EightPuzzleNode(problem.initial_state, None, None, 0)
            frontier = PriorityQueue()
            frontier.put((evaluation_function(problem, node), node))
            explored = set()
            counter = 0

            while not frontier.empty():
                counter += 1
                _, current_node = frontier.get()

                if problem.is_goal(current_node.state):
                    print( f"Goal state reached in this number of moves: {current_node.path_cost} and this number of nodes explored: {counter}" )
                    return current_node

                explored.add(current_node.state)

                for child in self.expand(problem, current_node):
                    if child.state not in explored:
                        frontier.put((evaluation_function(problem, child), child))

            return None
        else:
            return None

    def expand(self, problem, node):
        """
        Return a list of EightPuzzleNodes that are reachable from `node`.
        """
        returnlist = []

        for action in problem.actions(node.state):
            new_state = problem.result(node.state, action)
            new_node = EightPuzzleNode(new_state, node, action, node.path_cost + 1)
            returnlist.append(new_node)

        return returnlist

    def cost_so_far_plus_estimated_cost_remaining(self, problem, node):
        """
        The evaluation function, f(n) = g(n) + h(n).
        """
        g_n = node.path_cost
        # Calculate h(n) - Manhattan distance
        h_n = 0
        for i in range(len(node.state)):
            if node.state[i] is not None:  # Skip the blank tile
                # Find where this tile is now
                current_row, current_col = divmod(i, 3)
                
                # Find where this tile should be (in goal state)
                goal_index = problem.goal_state.index(node.state[i])
                goal_row, goal_col = divmod(goal_index, 3)
                
                # Add Manhattan distance for this tile
                h_n += abs(current_row - goal_row) + abs(current_col - goal_col)
        return g_n + h_n

    def actions_to_reach_solution_node(self, solution_node):
        """
        Given an EightPuzzleNode goal node, produce a list of in-order actions
        that lead from the initial state to the goal state.
        """
        # print(solution_node.state)
        if (solution_node == []):
            return []
        else:
            actions = []
            if solution_node.parent is None:
                return solution_node.action
            current_node = solution_node
            while current_node.parent is not None:
                actions.append(current_node.action)
                current_node = current_node.parent
            actions.reverse()
            return actions