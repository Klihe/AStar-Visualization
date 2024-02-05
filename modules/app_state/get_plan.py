# get_plan

# imports of modules
from modules.config import Config
from modules.color import Color

# function get_plan is used to get the barriers, start and end point of the grid
def get_plan(all_nodes: list) -> list[int]:
    # list to store the barriers
    nodes_barriers: list = []
    node_start: tuple[int] = None
    node_end: tuple[int] = None

    # Loop through the grid and get the barriers, start and end point
    for i in range(Config.COLUMNS):
            for j in range(Config.ROWS):
                if all_nodes[i, j].color == Color.BLACK:
                    nodes_barriers.append(all_nodes[i][j].point)
                if all_nodes[i, j].color == Color.YELLOW:
                    node_start = all_nodes[i][j].point
                if all_nodes[i][j].color == Color.BLUE:
                    node_end = all_nodes[i][j].point
                    
    # return the barriers, start and end point
    return nodes_barriers, node_start, node_end
