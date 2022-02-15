# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
import random

import util

class Structura:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def getName(self):
        return self.name

    def getCost(self):
        return self.cost

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.expand(problem.getStartState()))

    for successor in  problem.expand(problem.getStartState()):
        next_pos, action, cost = successor
        print("Next position is:", next_pos, "with action", action, "and cost", cost)
    """
    "*** YOUR CODE HERE ***"
    "util.raiseNotDefined()"
    """
    from game import Directions
    w = Directions.WEST
    successor1 = problem.expand(problem.getStartState())[0]
    next_pos1, next_action1, cost1 = successor1
    successor2 = problem.expand(next_pos1)[0]
    next_pos2, next_action2, cost2 = successor2
    return [next_action1, next_action2]
    """
    """
    component1 = Structura("nume1", 10)
    component2 = Structura("nume2", 11)
    stiva = util.Stack()
    stiva.push(component1)
    stiva.push(component2)
    first = stiva.pop()
    print("COMPONENTE: ")
    print("nume:", first.getName(), "cost:", first.getCost())
    first = stiva.pop()
    print("nume:", first.getName(), "cost:", first.getCost())
    util.raiseNotDefined()
    """

    from util import Stack

    frontier = Stack()
    expended = []

    initial_state = problem.getStartState()
    frontier.push((initial_state, []))

    while(not frontier.isEmpty()):
        poppped_element = frontier.pop()
        current_state, actions = poppped_element

        if(current_state not in expended):
            expended.append(current_state)

            if(problem.isGoalState(current_state)):
                return actions

            for successor in problem.expand(current_state):
                next_pos, next_action, cost = successor
                frontier.push((next_pos, actions + [next_action]))
"""
DFS foloseste ca frontiera o stiva. Cat timp frontiera nu e vida:
luam primul element, il despachetam, daca nu e in lista nodurilor
expandate, il adaugam. Daca am ajuns la Goal returnam actiunile.
Pentru "nodul" curent, cautam succesorul si il aduagam in frontiera
"""

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    from util import Queue

    frontier = Queue()
    expended = []

    initial_state = problem.getStartState()
    frontier.push((initial_state, []))

    while (not frontier.isEmpty()):
        poppped_element = frontier.pop()
        current_state, actions = poppped_element

        if (current_state not in expended):
            expended.append(current_state)

            if (problem.isGoalState(current_state)):
                return actions

            for successor in problem.expand(current_state):
                next_pos, next_action, cost = successor
                frontier.push((next_pos, actions + [next_action]))
    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    from util import PriorityQueue

    frontier = PriorityQueue()
    expended = []

    initial_state = problem.getStartState()
    #node = (initial_state, actions, cost)
    #frontier.push(node, 0)
    frontier.push((initial_state, [], 0), 0)

    while(not frontier.isEmpty()):
        popped_element = frontier.pop()
        current_state, actions, total_cost = popped_element

        if current_state not in expended:
            expended.append(current_state)

            if(problem.isGoalState(current_state)):
                return actions

            for successor in problem.expand(current_state):
                next_pos, next_action, next_cost = successor
                new_cost = total_cost + next_cost
                #f(successor) = g(successor) + h(successor)
                #g(s) = cost total pt a ajuge la successor
                #h(s) = valoarea euristicii in nodul s
                f = new_cost + heuristic(next_pos, problem)
                frontier.push((next_pos, actions + [next_action], new_cost), f)


def randomSearchAgent(problem):

    current = problem.getStartState()
    solution = []
    while(not(problem.isGoalState(current))):
        successor = problem.expand(current)
        no_of_successors = len(successor)
        random_succ_index = int(random.random()*no_of_successors)
        next = successor[random_succ_index]
        current = next[0]
        solution.append(next[1])
    print ("SOLUTION: ", solution)
    return solution


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
rs = randomSearchAgent