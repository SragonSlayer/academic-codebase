# Wumpus World Scratchpad
# Use this as a "scratchpad" to tinker with your code.
# There are no rules here, and this code will not be evaluated. This file is a
# place for you to experiment.


from wumpus_world import WumpusWorld
from wumpus_world_agent import WumpusWorldAgent
from knowledge_base import KnowledgeBase

"""
Scenario 1: An agent in the initial location, surrounded by pits, should
climb out of the cave.
. . . .
W G . .
P . . .
A P . .
"""
wumpus_world = WumpusWorld(
    agent_location = (1, 1),
    agent_direction = 'East',
    wumpus_location = (1, 3),
    gold_location = (2, 3),
    pit_locations = [ (1, 2), (2, 1) ]
    )

kb = KnowledgeBase()
# Hint: tell the kb the initial given facts, such as the initial location
# of the agent, and its initial direction.

agent = WumpusWorldAgent(kb)
action = agent.action(wumpus_world.percept(wumpus_world.agent_location))
action(agent, wumpus_world) # climb?


"""
Scenario 2: An agent in the initial location, with pits to every immediate
location to the north, would *at least* move once to the east.
. . . .
W G . .
P P P P
A . . .
"""
wumpus_world = WumpusWorld(
    agent_location = (1, 1),
    agent_direction = 'East',
    wumpus_location = (1, 3),
    gold_location = (2, 3),
    pit_locations = [ (1, 2), (2, 2), (3, 2), (4, 2) ]
    )

kb = KnowledgeBase()
# Hint: tell the kb the initial given facts, such as the initial location
# of the agent, and its initial direction.

agent = WumpusWorldAgent(kb)
action = agent.action(wumpus_world.percept(wumpus_world.agent_location))
action(agent, wumpus_world) # move_forward?

"""
Scenario 2: An agent in the initial location, with pits to every immediate
location to the north, would *at least* move once to the east.
. . . .
W G . .
P P P P
A . . .
"""
wumpus_world = WumpusWorld(
    agent_location = (1, 1),
    agent_direction = 'East',
    wumpus_location = (1, 3),
    gold_location = (2, 3),
    pit_locations = [ (2, 2), (3, 2), (4, 2) ]
    )

kb = KnowledgeBase()
# Hint: tell the kb the initial given facts, such as the initial location
# of the agent, and its initial direction.

agent = WumpusWorldAgent(kb)
action = agent.action(wumpus_world.percept(wumpus_world.agent_location))
action(agent, wumpus_world) # move_forward?