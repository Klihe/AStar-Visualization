# state.py

# imports of libraries
from enum import Enum

# State class to store the states of the game
class State(Enum):
    PLANNER = 1
    CALC = 2
    RESULT = 3