# Main
# A demonstration of the WumpusWorld and WumpusWorldAgent.
# Lucas Swanson

from wumpus_world import WumpusWorld
from wumpus_world_agent import WumpusWorldAgent
from knowledge_base import KnowledgeBase

wumpus_world = WumpusWorld(
    agent_location = (1, 1),
    agent_direction = 'East',
    agent_alive = True,
    wumpus_alive = True,
    wumpus_location = (3, 1),
    gold_location = (4, 4),
    pit_locations = [ (2, 2), (3, 3), (4, 3) ]
    )

kb = KnowledgeBase()

agent = WumpusWorldAgent(kb)
 

action = agent.action(wumpus_world.percept((1, 1)))
action(agent, wumpus_world)
print(wumpus_world.agent_location)
"""
Currently the default action from "action" is to climb out of the cave.
In the future this will be expanded to include more complex behavior, and the KnowledgeBase will be used to determine which action to take.
"""