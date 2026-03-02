# KnowledgeBase
# A knowledge base for a knowledge-based agent.
# YOUR NAME

from wumpus_world_agent import WumpusWorldAgent

class KnowledgeBase:

    def __init__(self):
        """
        A KnowledgeBase has a `sentences` property, which is a list of sentences
        """
        self.sentences = []
        self.time = 0

    def tell(self, sentence):
        """
        Add a sentence to the knowledge base.
        """
        self.sentences.append(sentence)

    def ask(self, query=None):
        """
        Given a query, return an action for the WumpusWorldAgent to perform. The default action is to climb out of the cave.
        """
        output = WumpusWorldAgent.climb

        """
        Logic for the knownledge base will go here in the future
        """
        
        return output