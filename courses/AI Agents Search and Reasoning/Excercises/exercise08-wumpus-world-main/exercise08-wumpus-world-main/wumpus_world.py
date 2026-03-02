# WumpusWorld
# A simulated representation of a real Wumpus World, aligned with the specified
# characteristics in the AIMA text.
# Note: This is not a state model. It _is_ the real world / environment within
# which the agent operates. Think of it as actual, physical, reality.
# Note 2: This simulation will not include the modeling of time, for the sake of
# simplicity. This only affects the 'Bump' and 'Scream' percepts. In the case of
# 'Bump', we assume that when an agent is in a room facing a wall, it should receive
# the 'Bump' percept. For 'Scream', when the wumpus is killed we let the scream
# linger throughout the cave indefinitely.
# YOUR NAME

class WumpusWorld:

    EXIT_LOCATION = (1, 1)

    def __init__(self, agent_location = (1, 1), agent_direction = 'East',
                       agent_alive = True, wumpus_alive = None,
                       wumpus_location = None, gold_location = None,
                       pit_locations = []):
        self.agent_location = agent_location
        self.agent_direction = agent_direction
        self.agent_alive = agent_alive
        self.wumpus_alive = wumpus_alive
        self.wumpus_location = wumpus_location
        self.gold_location = gold_location
        self.pit_locations = pit_locations
        self.has_arrow = True

    def percept(self, location):
        """
        The current five-element percept in the `location`. Returns a tuple in the
        form of ('Stench', 'Breeze', 'Glitter', 'Bump', 'Scream'). Any of the elements
        within the returned percept tuple can be None.
        """
        if location is None:
            return (None, None, None, None, None)
        stench = 'Stench' if (self.adjacent(location, self.wumpus_location) or location == self.wumpus_location) else None
        breeze = 'Breeze' if any(self.adjacent(location, pit_location) for pit_location in self.pit_locations) else None
        glitter = 'Glitter' if location == self.gold_location else None
        bump = 'Bump' if self.agent_bumped_wall() else None
        scream = 'Scream' if self.wumpus_alive == False else None
        return (stench, breeze, glitter, bump, scream)

    """
    Physical side effects of agent actions
    """

    def turned_left(self):
        if self.agent_direction == 'East':
            self.agent_direction = 'North'
        elif self.agent_direction == 'North':
            self.agent_direction = 'West'
        elif self.agent_direction == 'West':
            self.agent_direction = 'South'
        elif self.agent_direction == 'South':
            self.agent_direction = 'East'

    def turned_right(self):
        if self.agent_direction == 'East':
            self.agent_direction = 'South'
        elif self.agent_direction == 'South':   
            self.agent_direction = 'West'
        elif self.agent_direction == 'West':
            self.agent_direction = 'North'
        elif self.agent_direction == 'North':
            self.agent_direction = 'East'

    def moved_forward(self):
        if self.agent_direction == 'East' and self.agent_can_move_east():
            self.agent_location = (self.agent_location[0] + 1, self.agent_location[1])
        elif self.agent_direction == 'West' and self.agent_can_move_west():
            self.agent_location = (self.agent_location[0] - 1, self.agent_location[1])
        elif self.agent_direction == 'North' and self.agent_can_move_north():
            self.agent_location = (self.agent_location[0], self.agent_location[1] + 1)
        elif self.agent_direction == 'South' and self.agent_can_move_south():
            self.agent_location = (self.agent_location[0], self.agent_location[1] - 1)
        
        if self.agent_location in self.pit_locations:
            self.agent_alive = False
        if self.agent_location == self.wumpus_location and self.wumpus_alive:
            self.agent_alive = False

    def grabbed(self):
        if self.agent_location == self.gold_location:
            self.gold_location = None
            self.agent_has_gold = True

    def climbed(self):
        if self.agent_location == self.EXIT_LOCATION:
            self.agent_has_climbed = True
            self.agent_location = None

    def shot(self):
        if self.has_arrow:
            self.has_arrow = False
            if self.agent_direction == 'East' and self.wumpus_east_of_agent():
                self.wumpus_alive = False
            elif self.agent_direction == 'West' and self.wumpus_west_of_agent():
                self.wumpus_alive = False
            elif self.agent_direction == 'North' and self.wumpus_north_of_agent():
                self.wumpus_alive = False
            elif self.agent_direction == 'South' and self.wumpus_south_of_agent():
                self.wumpus_alive = False

    """
    Helper methods
    """

    def adjacent(self, location, target):
        if location and target:
            return (abs(location[0] - target[0]) == 1 and location[1] == target[1]) or (abs(location[1] - target[1]) == 1 and location[0] == target[0])
        return False

    def agent_can_move_east(self):
        if self.agent_location[0] < 4:
            return True
        return False

    def agent_can_move_west(self):
        if self.agent_location[0] > 1:
            return True
        return False

    def agent_can_move_north(self):
        if self.agent_location[1] < 4:
            return True
        return False

    def agent_can_move_south(self):
        if self.agent_location[1] > 1:
            return True
        return False

    def agent_bumped_wall(self):
        if self.agent_direction == 'East' and not self.agent_can_move_east():
            return True
        if self.agent_direction == 'West' and not self.agent_can_move_west():
            return True
        if self.agent_direction == 'North' and not self.agent_can_move_north():
            return True
        if self.agent_direction == 'South' and not self.agent_can_move_south():
            return True
        return False

    def wumpus_east_of_agent(self):
        if self.wumpus_location and self.agent_location:
            return (self.wumpus_location[0] > self.agent_location[0]) and (self.wumpus_location[1] == self.agent_location[1])
        return False

    def wumpus_west_of_agent(self):
        if self.wumpus_location and self.agent_location:
            return (self.wumpus_location[0] < self.agent_location[0]) and (self.wumpus_location[1] == self.agent_location[1])
        return False

    def wumpus_north_of_agent(self):
        if self.wumpus_location and self.agent_location:
            return (self.wumpus_location[0] == self.agent_location[0]) and (self.wumpus_location[1] > self.agent_location[1])
        return False

    def wumpus_south_of_agent(self):
        if self.wumpus_location and self.agent_location:
            return (self.wumpus_location[0] == self.agent_location[0]) and (self.wumpus_location[1] < self.agent_location[1])
        return False
