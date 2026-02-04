# SimpleReflexVacuum: A robot vacuum cleaner modeled as a simple reflex agent.
# Your implementation should pass the tests in test_simple_reflex_vacuum.py.
# YOUR NAME


class SimpleReflexVacuum:

    def suck(self):
        print('side effect: cause hardware to suck')

    def move_left(self):
        print('side effect: cause hardware to move left')
    
    def move_right(self):
        print('side effect: cause hardware to move right')

    def action(self, location_id, dirt):
        if (dirt == 'Dirt'):
            return self.suck
        elif location_id == 'A':
            return self.move_right
        else:
            return self.move_left