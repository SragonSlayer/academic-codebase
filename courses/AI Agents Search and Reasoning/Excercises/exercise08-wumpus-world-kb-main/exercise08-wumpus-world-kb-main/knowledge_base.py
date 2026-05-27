# KnowledgeBase
# A knowledge base for a knowledge-based agent.

from wumpus_world_agent import WumpusWorldAgent

class KnowledgeBase:

    def __init__(self):
        """
        A KnowledgeBase has a `sentences` property, which is a list of sentences
        """
        self.sentences = []
        self.safe_squares = []              # ← use self.
        self.possible_pit_squares = []
        self.possible_wumpus_squares = []
        self.time = 0

    def tell(self, sentence):
        """
        Add a sentence to the knowledge base.
        """
        self.sentences.append(sentence)
        # Iterate through all sentences in the query and update the lists of safe squares, possible pit squares, and possible wumpus squares based on the percepts.
        for percept in sentence:
            type = percept[0]
            location = percept[1]
            if type == "NoBreeze":
                for square in self.adjacent_squares(location):
                    if square not in self.safe_squares:
                        self.safe_squares.append(square)
                    if square in self.possible_pit_squares:
                        self.possible_pit_squares.remove(square)
            elif type == "Breeze":
                for square in self.adjacent_squares(location):
                    if square not in self.safe_squares and square not in self.possible_pit_squares:
                        self.possible_pit_squares.append(square)
        print(f"Possible Pits: {self.possible_pit_squares}")
        print(f"Safe Squares: {self.safe_squares}")

    def ask(self, query=None):
        """
        Given a query, return an action for the WumpusWorldAgent to perform. The default action is to climb out of the cave.
        """
        output = WumpusWorldAgent.climb

        if query:
            # Process the query and determine the appropriate action based on the knowledge base.
            # For example, if there are safe squares available, the agent might choose to move to one of them instead of climbing.
            if self.safe_squares:
                output = f"MOVE to {self.safe_squares[0]}"  # Move to the first safe square in the list

        return output
    
    def adjacent_squares(self, location):
        """
        return a list of all squares directly adjacent (N, S, E, W) to
        `location`.  Coordinates are tuples (x,y); only positive
        coordinates are kept (you can add an upper bound check if your
        world has a fixed size).
        """
        x, y = location                 # line 49 is here
        adjacent_squares = []
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if nx > 0 and ny > 0:       # drop invalid squares
                adjacent_squares.append((nx, ny))
        return adjacent_squares