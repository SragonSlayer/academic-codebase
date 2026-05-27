# Main
# A demonstration of the WumpusWorldAgent and KnowledgeBase.
# Lucas Swanson

from wumpus_world import WumpusWorld
from wumpus_world_agent import WumpusWorldAgent
from knowledge_base import KnowledgeBase

"""
Scenario 1: An agent in the initial location, with no pits nearby, would pick the first safe direction to move.
. . . .
W G . .
. P P P
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

"""
Scenario 1: An agent in the initial location, with gold at the same location, would grab the gold.
. . . .
W . . .
. P P P
G . . .
"""
wumpus_world = WumpusWorld(
    agent_location = (1, 1),
    agent_direction = 'East',
    wumpus_location = (1, 3),
    gold_location = (1, 1),
    pit_locations = [ (2, 2), (3, 2), (4, 2) ]
    )

kb = KnowledgeBase()
# Hint: tell the kb the initial given facts, such as the initial location
# of the agent, and its initial direction.

agent = WumpusWorldAgent(kb)
action = agent.action(wumpus_world.percept(wumpus_world.agent_location))
action(agent, wumpus_world) # grab?

"""
Scenario 2: An agent in the initial location, with a pit to either side. Would climb out of the cave.
. . . .
W G . .
P P P P
A P . .
"""
wumpus_world = WumpusWorld(
    agent_location = (1, 1),
    agent_direction = 'East',
    wumpus_location = (1, 3),
    gold_location = (2, 3),
    pit_locations = [ (1, 2), (2, 1), (2, 2), (3, 2), (4, 2) ]
    )

kb = KnowledgeBase()
# Hint: tell the kb the initial given facts, such as the initial location
# of the agent, and its initial direction.

agent = WumpusWorldAgent(kb)
action = agent.action(wumpus_world.percept(wumpus_world.agent_location))
action(agent, wumpus_world) # climb

"""
Scenario 3: An agent in the initial location, with a pit to the north. Would climb out of the cave because the agent is dumb and cannot tell which direction the pit is in.
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
action(agent, wumpus_world) # climb