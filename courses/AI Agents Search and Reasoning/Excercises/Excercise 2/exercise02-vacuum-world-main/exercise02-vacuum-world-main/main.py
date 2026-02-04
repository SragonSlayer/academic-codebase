# Main
# YOUR NAME
# The start of your overall agent program.
# Demonstrate the use of your SimpleReflexVacuum and your ModelReflexVacuum.
# The code for using a SimpleReflexVacuum is provided for you.


# Part 1

from simple_reflex_vacuum import SimpleReflexVacuum

simple_reflex_vacuum = SimpleReflexVacuum()
action = simple_reflex_vacuum.action('A', 'Dirt')
action()


# Part 2

from model_reflex_vacuum import ModelReflexVacuum

