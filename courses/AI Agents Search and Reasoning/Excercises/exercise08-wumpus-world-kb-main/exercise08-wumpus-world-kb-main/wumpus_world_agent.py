# WumpusWorldAgent
# An agent designed to perform in the wumpus world environment.


class WumpusWorldAgent:

    # Replace this class with your WumpusWorldAgent from Part 1.
    def __init__(self, kb):
        """
        Initialize the Wumpus World agent
        """
        self.kb = kb
        self.time = 0
        self.has_arrow = True
        self.has_gold = False
        self.alive = True
        self.location = (1, 1)
        self.direction = 'E'
        self.visited = {self.location}
        self.action_history = []
    
    def turn_left(self, world):
        """
        Turn the agent left (counter-clockwise).
        """
        print("Turning left...")
        world.turned_left()
        self.action_history.append('TurnLeft')

    def turn_right(self, world):
        """
        Turn the agent right (clockwise).
        """
        print("Turning right...")
        world.turned_right()
        self.action_history.append('TurnRight')

    def move_forward(self, world):
        """
        Move the agent forward in the direction it is currently facing.
        """
        print("Moving forward...")
        world.moved_forward()
        self.action_history.append('MoveForward')
    
    def shoot(self, world):
        """
        Shoot the arrow in the direction the agent is currently facing. The agent can only shoot once, and will not shoot if it has already used its arrow.
        """
        if self.has_arrow:
            print("Shooting arrow!")
            world.shot()
            self.has_arrow = False
            self.action_history.append('Shoot')
        else:
            print("No arrow left to shoot!")

    def grab(self, world):
        """
        Grab the gold if it is in the same location as the agent.
        """
        print("Grabbing gold if it's here...")
        world.grabbed()
        self.action_history.append('Grab')
    
    def climb(self, world):
        """
        Climb out of the cave if the agent is in the same location as the exit (1, 1).
        """
        print("Climbing out if i'm at the exit...")
        world.climbed()
        self.action_history.append('Climb')
    
    def action(self, percept):
        """
        Given a percept, decide and perform an action.
        """
        percept_sentences = self.make_percept_sentence(percept)
        self.kb.tell(percept_sentences)

        if ("Glitter", self.location) in percept_sentences and not self.has_gold:
            return WumpusWorldAgent.grab
        
        safe_squares = self.make_action_query()

        if safe_squares:
            next_square = safe_squares[0]
            self.move_forward
            return WumpusWorldAgent.move_forward
        print("No safe moves available, agent will wait or take risk")
        return WumpusWorldAgent.climb  # Default action if no safe moves are available
    
    def make_percept_sentence(self, percept):
        """
        Converts a percept tuple into structured KB facts.
        """
        percepts = []
        x, y = self.location

        percepts.append(("Stench", self.location) if percept[0] else ("NoStench", self.location))
        percepts.append(("Breeze", self.location) if percept[1] else ("NoBreeze", self.location))
        percepts.append(("Glitter", self.location) if percept[2] else ("NoGlitter", self.location))
        if percept[3]:
            percepts.append(("Bump", self.location))
        if percept[4]:
            percepts.append(("Scream", self.location))

        percepts.append(("Visited", self.location))
        percepts.append(("Safe", self.location))
        
        print(f"Percept sentence: {percepts}")
        return percepts
    
    def make_action_query(self):
        """
        Return all adjacent safe squares that have not been visited.
        """
        adjacent = self.kb.adjacent_squares(self.location)
        safe_unvisited = [
            square for square in adjacent
            if square in self.kb.safe_squares and square not in self.visited
        ]
        return safe_unvisited
