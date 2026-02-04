# ModelReflexVacuum: A robot vacuum cleaner modeled as a model-based reflex agent.
# Your implementation should pass the tests in test_model_reflex_vacuum.py.
# YOUR NAME

# State constants
# IDLE = 1
# MOVE = 2
# CLEAN = 3

from transition_model import TransitionModel
from sensor_model import SensorModel

class ModelReflexVacuum:

    # Initialize the state of the action function
    def __init__(self, state, transition_model, sensor_model):
        self.state = state
        self.transition_model = transition_model
        self.sensor_model = sensor_model
        self.most_recent_action = None
        self.location_id = None
        try:
            if self.sensor_model and hasattr(self.sensor_model, 'sense_location_id'):
                self.location_id = self.sensor_model.sense_location_id()
        except (AttributeError, TypeError):
            self.location_id = None

    # Support functions the agent will use to cause side effects
    def suck(self):
        print('side effect: cause hardware to suck')
        if self.transition_model:
            self.transition_model.apply_suction()
        # else:
        #     print("No transition model available to apply suction.")
        self.most_recent_action = self.suck

    def move_left(self):
        print('side effect: cause hardware to move left')
        if self.transition_model:
            self.transition_model.move_left()
        self.most_recent_action = self.move_left
    
    def move_right(self):
        print('side effect: cause hardware to move right')
        if self.transition_model:
            self.transition_model.move_right()
        self.most_recent_action = self.move_right

    def update_state(self):
        # print(f'Updating state from most recent action: {self.most_recent_action}')
        match self.most_recent_action:
            case self.suck:
                self.state = 'CLEAN'
                self.suck()
            case self.move_left:
                self.state = 'MOVE'
                self.move_left()
            case self.move_right:
                self.state = 'MOVE'
                self.move_right()

        # print(f'Current state: {self.state}, Location ID: {self.location_id}')
        match self.state:
            case 'IDLE':
                if self.sensor_model and self.sensor_model.sense_dirt():
                    self.state = 'CLEAN'
                    self.suck()
                    return self.suck
                    
                else:
                    self.state = 'MOVE'
                pass
            case 'MOVE':
                if self.location_id == 'B':
                    return self.move_left
                else:
                    return self.move_right
                self.state = 'IDLE'
            case 'CLEAN':
                self.state = 'IDLE'
                return self.suck
            case _:
                if self.sensor_model and self.sensor_model.sense_dirt():
                    self.state = 'CLEAN'
                    self.suck()
                    return self.suck
                elif self.location_id == 'B':
                    return self.move_left
                elif self.location_id == 'A':
                    return self.move_right
                self.state = 'IDLE'

    # State machine for controlling the vacuum
    def action(self):
        print("ModelReflexVacuum action called")
        return self.update_state()
        # pass
