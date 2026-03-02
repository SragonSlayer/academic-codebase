# WumpusWorldAgent
# An agent designed to perform in the wumpus world environment.
# YOUR NAME

class WumpusWorldAgent:
    
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
        Given a percept, decide on an action to take. The percept will be a tuple of the form ('Stench', 'Breeze', 'Glitter', 'Bump', 'Scream'). Any of the elements within the percept tuple can be None.
        """
        tell_sentence = self.make_percept_sentence(percept)
        self.kb.tell(tell_sentence)
        query_sentence = self.make_action_query()
        action_sentence = self.kb.ask(query_sentence)
        self.make_action_sentence(action_sentence)
        self.kb.tell(f"Action taken: {action_sentence}")
        self.time += 1
        return action_sentence

    def make_percept_sentence(self, percept):
        """
        This will be used in a further exercise. For now, it can be passed
        """
        pass

    def make_action_query(self):
        """
        This will be used in a further exercise. For now, it can be passed
        """
        pass

    def make_action_sentence(self, action):
        """
        This will be used in a further exercise. For now, it can be passed
        """
        pass